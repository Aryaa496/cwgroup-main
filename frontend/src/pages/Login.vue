<template>
  <div class="login-container">
    <h2>Login</h2>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="password">Password</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <div>
        <button type="submit">Login</button>
      </div>
    </form>
    <div v-if="error" class="error">
      <p>{{ error }}</p>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "Login",
  setup() {
    const username = ref("");
    const password = ref("");
    const error = ref("");

    const login = async () => {
      try {
        // Make a POST request to your Django API endpoint for login
        const response = await fetch("http://localhost:8000//", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: username.value,
            password: password.value,
          }),
        });

        if (!response.ok) {
          throw new Error("Invalid credentials");
        }

        const data = await response.json();
        
        // Store JWT tokens in localStorage
        localStorage.setItem("access_token", data.access);
        localStorage.setItem("refresh_token", data.refresh);

        // Redirect or show success message
        alert("Login successful!");
      } catch (err) {
        error.value = "Invalid credentials";
      }
    };

    return {
      username,
      password,
      error,
      login,
    };
  },
});
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.error {
  color: red;
  margin-top: 10px;
}
</style>
