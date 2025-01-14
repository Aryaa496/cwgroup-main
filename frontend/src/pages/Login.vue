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
import { useUserStore } from '@/user.js';

const email = ref('');
const password = ref('');
const userStore = useUserStore();

const handleLogin = async () => {
  await userStore.login(email.value, password.value);
  if (userStore.accessToken) {
    // Redirect or show user profile after successful login
    console.log('Login successful, token:', userStore.accessToken);
  }
};
</script>
