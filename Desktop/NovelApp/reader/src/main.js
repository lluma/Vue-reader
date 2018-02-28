import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import About from './components/About.vue'
import NotFound from './components/NotFound.vue'
import Noval from './components/Noval.vue'
import Contents from './components/Contents.vue'
import Chapter from './components/Chapter.vue'

Vue.use(VueRouter)

const router = new VueRouter({
  mode: 'history',
  routes: [
    {path: '/about', name: 'about', component: About},
    {path: '*', name: 'not found', component: NotFound},
    {path: '/noval', name: 'noval', component: Noval},
    {path: '/contents', name: 'contents', component: Contents},
    {path: '/chapter', name: 'chapter', component: Chapter}
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})
