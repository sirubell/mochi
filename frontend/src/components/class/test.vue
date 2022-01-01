<template>
<div>
  <h1></h1>
  <table class="table" >
    <th>#</th>
    <th>Problem name</th>
    <th>Difficulty</th>
    <v-data-table>
    </v-data-table>
    <tr v-for="item in problemTable" :key="item.id" >
      <td><a v-bind:href="item.id">{{ item.id }}</a></td>
      <td>{{ item.name }}</td>
      <td>{{ item.difficulty }}</td>
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
    axios.get('http://192.168.122.231:5000/'+'problem?page='+1)
    .then( response => {
      this.problemTable = response.data.returnset
      console.log(response.data.returnset)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
