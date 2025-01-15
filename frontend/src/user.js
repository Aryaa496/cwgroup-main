import { defineStore } from 'pinia';
import { ref } from 'vue';

export const useUserStore = defineStore('user', () => {
  const user = ref(null);
  const accessToken = ref(localStorage.getItem('access_token') || null);

  // Login function
  const login = async (email, password, csrfToken) => {
    try {
      const response = await fetch('http://localhost:8000/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken,  
        },
        body: JSON.stringify({ email, password }), // Send email and password as JSON
        credentials: 'include',
      });
  
      const data = await response.json();
      
      if (response.ok) {
        accessToken.value = data.access; // Assuming the backend returns a field named 'access'
        localStorage.setItem('access_token', accessToken.value); // Store the token in localStorage
        console.log('Login successful:', data.success);
      } else {
        console.log('Login failed:', data.error);
      }
    } catch (error) {
      console.error('Login failed:', error);
    }
  };
  

  // Fetch user profile
  const fetchUserProfile = async () => {
    try {
      const response = await fetch('http://localhost:8000/profile/', {
        method: 'GET',
        credentials:'include',
        headers: {
          'Authorization': `Bearer ${accessToken.value}`, // Include the token here
        },
      });
      
  
      if (!response.ok) {
        throw new Error('Failed to fetch user profile');
      }
      
  
      const data = await response.json();
      user.value = data;
      const hobbies = data.hobbies || [];
        console.log('Hobbies:', hobbies);
    } catch (error)
     {
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
