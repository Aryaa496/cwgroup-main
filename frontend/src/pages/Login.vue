

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
        const response = await axios.post("http://localhost:8000/api/login/", {
          username: username.value,
          password: password.value,
        });
        // Store JWT tokens in localStorage or Vuex
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);

        // Redirect to another page or show success message
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
