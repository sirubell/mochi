<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>Problem name</th>
    <th>Difficulty</th>
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
      problemTable: {},
      error: ""
    }
  },
  created() {
    axios.get('problem?page=1')
    .then( response => {
      this.problemTable = response.data.returnset
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
