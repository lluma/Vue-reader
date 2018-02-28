<template>
  <div class="">

    <div class="list-group" v-for="(chapter, index) in contents" :key="index">
        <router-link class="list-group-item"  :to="{ name: 'chapter', params: { 'href': chapter['href']} }" :key="index">{{ chapter['title'] }}</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      contents: []
    }
  },
  methods: {
    getContents () {
      const path = `http://localhost:5000/api/contents`
      axios.get(path).then(res => {
        this.contents = res.data.contents
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.getContents()
  }
}
</script>

<style>
</style>
