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
  const csrfToken = document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1];  
    console.log('Sending login request:', { email: email.value, password: password.value, csrfToken });
    // console.log("CSRF Token:", csrfToken);
  try {
    await userStore.login(email.value, password.value, csrfToken);  // Call login function from store
    if (userStore.accessToken) {
      console.log('Login successful');
      window.location.href = 'http://localhost:5731/profile';// Redirect or show user profile after successful login
    }
  } catch (error) {
    console.error('Login failed:', error);
  }
};
</script>
