<template>
  <div class="">
    <h3>Chapter</h3>
    <div class="" v-for="(line, index) in article" :key="index">
      <p :key="index">{{ line }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data () {
    return {
      article: []
    }
  },
  methods: {
    getArticle () {
      const path = `http://localhost:5000/api/article?href=${this.$route.params.href}`
      axios.get(path).then(res => {
        this.article = res.data.article.slice(1, res.data.article.length)
      }).catch(err => {
        console.log(err)
      })
    }
  },
  created () {
    this.getArticle()
  }
}
</script>

<style>
</style>
