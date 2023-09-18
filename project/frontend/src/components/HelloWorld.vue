<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul>
      <li v-for="post in posts" :key="post.id">{{ post.title }}</li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data() {
    return {
      posts: []
    };
  },
  mounted() {
    axios.get('/api/posts/?format=json')
      .then(response => {
        this.posts = response.data;
      })
      .catch(error => {
        console.error("There was an error fetching the posts", error);
      });
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
