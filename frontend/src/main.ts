import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'

// Function to fetch the CSRF token cookie
const fetchCSRFToken = () => {
  fetch('http://localhost:8000/api/some-endpoint/')  // This could be any endpoint that returns the CSRF cookie
    .then(response => {
      if (response.ok) {
        console.log('CSRF token cookie set!');
      } else {
        console.error('Failed to set CSRF token cookie');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
};

// Fetch CSRF token when the app is created
fetchCSRFToken();

const app = createApp(App)

app.use(router)

app.mount('#app')
