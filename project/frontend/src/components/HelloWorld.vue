<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <ul class="post-list">
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
      posts: [],
      socket: null
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

    this.initializeWebSocket();  
  },
  methods: {
      initializeWebSocket() {
          this.socket = new WebSocket('ws://localhost:8000/ws/some_path/');
          
          this.socket.onmessage = () => {
              location.reload(); // Ricarica la pagina quando ricevi un messaggio.
          };

          // Puoi anche gestire altri eventi del socket qui, come onclose, onerror, etc.
      }
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
.post-list {
    list-style-type: none;
    padding: 0;
}
.post-list li {
    padding: 10px 15px;
    border-bottom: 1px solid #42b983;
}
.post-list li:last-child {
    border-bottom: none;
}
</style>
