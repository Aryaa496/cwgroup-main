import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useUserStore = defineStore('user', () => {
  const user = ref(null);
  const accessToken = ref(localStorage.getItem('access_token') || null);

  // Login function
  const login = async (email, password) => {
    try {
      const response = await fetch('http://localhost:8000/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (!response.ok) {
        throw new Error('Invalid credentials');
      }

      const data = await response.json();
      accessToken.value = data.access;
      localStorage.setItem('access_token', accessToken.value);
    } catch (error) {
      console.error('Login failed:', error);
    }
  };

  // Fetch user profile
  const fetchUserProfile = async () => {
    try {
      const response = await fetch('http://localhost:8000/profile/', {
        method: 'GET',
        headers: {
          'Authorization': `Bearer ${accessToken.value}`,
        },
      });

      if (!response.ok) {
        throw new Error('Failed to fetch user profile');
      }

      const data = await response.json();
      user.value = data;
    } catch (error) {
      console.error('Error fetching user profile:', error);
    }
  };

  return {
    user,
    accessToken,
    login,
    fetchUserProfile,
  };
});
