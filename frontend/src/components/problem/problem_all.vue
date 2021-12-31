<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>Problem name</th>
    <th>Difficulty</th>
    <tr v-for="item in problemTable" :key="item.title" >
      <td><a v-bind:href="item.id">{{ item.id }}</a></td>
      <td>{{ item.name }}</td>
      <td>{{ item.username }}</td>
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
      problemTable: {}
    }
  },
  created() {
    axios.get('https://jsonplaceholder.typicode.com/users')
    .then( response => {
      this.problemTable = response.data
      console.log(response.data)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
