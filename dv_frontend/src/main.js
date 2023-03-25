import * as ElementPlusIconsVue from "@element-plus/icons-vue"
import { createPinia } from "pinia"
import { createApp } from "vue"
import App from "./App.vue"
import router from "./routers"

const pinia = createPinia()
const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component)
}
app.use(pinia).use(router).mount("#app")
