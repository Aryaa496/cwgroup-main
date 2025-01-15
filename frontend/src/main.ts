import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';
import { createPinia } from 'pinia';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

// Function to fetch the CSRF token
const fetchCSRFToken = async () => {
  try {
    // Send a GET request to a CSRF-protected route to get the token
    const response = await fetch('http://localhost:8000/login/', {
      method: 'GET',
      credentials: 'include', // Ensure cookies are included in the request
    });

    // Check if the response is OK and that the CSRF token is available in the cookies
    if (response.ok) {
      const csrfToken = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];

      if (csrfToken) {
        console.log('CSRF token fetched successfully:', csrfToken);
      } else {
        console.error('CSRF token not found in cookies');
      }
    } else {
      console.error('Failed to fetch CSRF token');
    }
  } catch (error) {
    console.error('Error fetching CSRF token:', error);
  }
};

// Fetch CSRF token when the app is created
fetchCSRFToken();

const app = createApp(App);

app.config.globalProperties.$axios = axios;

app.use(router);
app.use(createPinia());

app.mount('#app');
