<template>
  <div>
    <h2>Login</h2>
    <form @submit.prevent="handleLogin">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Password" required />
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useUserStore } from '@/user.js';  // Pinia store for user management

const email = ref('');
const password = ref('');
const userStore = useUserStore();

const handleLogin = async () => {
  try {
    await userStore.login(email.value, password.value);  // Call login function from store
    if (userStore.accessToken) {
      console.log('Login successful');
      // Redirect or show user profile after successful login
    }
  } catch (error) {
    console.error('Login failed:', error);
  }
};
</script>
