import { createApp } from 'vue'
import { createPinia } from 'pinia'

import Notifications from '@kyvg/vue3-notification'
import './assets/main.css'

import router from './router'
import App from './App.vue'


const app = createApp(App)

app.use(Notifications);
app.use(createPinia())
app.use(router)

app.mount('#app')
