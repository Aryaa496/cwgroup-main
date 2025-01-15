<template>
    <div v-if="userStore.user">
      <h2>User Profile</h2>
      <p>Name: {{ userStore.user.name }}</p>
      <p>Email: {{ userStore.user.email }}</p>
      <p>Date of Birth: {{ userStore.user.date_of_birth }}</p>
      <h2>Hobbies</h2>
        <ul>
            <li v-for="hobby in userStore.user.hobbies" :key="hobby">
                {{ hobby }}


                
            </li>
        </ul>
    </div>
    <div v-else>
      <p>Loading...</p>
    </div>
  </template>
  
  <script setup>
  import { onMounted } from 'vue';
  import { useUserStore } from '@/user.js';
  
  const userStore = useUserStore();
  
  onMounted(() => {
    userStore.fetchUserProfile();
  });
  </script>
  