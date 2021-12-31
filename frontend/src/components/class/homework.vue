<template>
  <div>
    <table class="table" >
      <th>#</th>
      <th>Problem name</th>
      <th>Difficulty</th>
      <tr v-for="item,counter in problemTable" :key="item.id" >
        <td><a v-bind:href="'http://192.168.122.121:8080/problem/'+item.id">{{counter+1}}</a></td>
        <td>{{ item.name }}</td>
        <td>{{ item.username }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Homework',
  data() {
    return {
      problemTable: {},
    }
  },

  created() {
    axios.get('https://jsonplaceholder.typicode.com/users'/*+current.substr(-1,1)*/)
    .then( response => {
      this.problemTable = response.data
      console.log(this.problemTable)
    })
    .catch( error => {
      this.error = error
    });
  }
}

</script>
