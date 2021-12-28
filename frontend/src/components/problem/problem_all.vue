<template>
<div>
  <h1>Problem All is not implemented</h1>
  <table class="table">
    <tr v-for="item in problemTalbe" :key="item.title">
      <!-- <td><router-link :to="{ path: '/asdf', params:{id :item.id}}"> <a v-bind:href="item.id">{{ item.id }}</a></router-link></td> -->
      <td><a v-bind:href="item.id">{{ item.id }}</a></td>
      <td>{{ item.name }}</td>
      <td>{{ item.username }}</td>
      <td>{{ item.email }}</td>
      <td>{{ item.address.street }}</td>
    </tr>
  </table>
  
  <div v-if="error">
    {{ error }}
  </div>
  
</div>

</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      problemTalbe: {}
    }
  },
  created() {
    axios.get('https://jsonplaceholder.typicode.com/users')
    .then( response => {
      this.problemTalbe = response.data
      console.log(response.data)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
