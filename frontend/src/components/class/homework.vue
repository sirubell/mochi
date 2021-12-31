<template>
  <div>
    <table class="table" >
      <th>#</th>
      <th>題目名稱</th>
      <th>繳交情況</th>
      <tr v-for="item,counter in HomeworkTable" :key="item.id" >
        <td><a v-bind:href="'http://192.168.122.231:5000/'+'problem/'+item.id">{{counter+1}}</a></td>
        <td>{{ item.name }}</td>
        <td>{{ item.username }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
var current = window.location.pathname;
import axios from 'axios'

export default {
  name: 'Homework',
  data() {
    return {
      HomeworkTable: {},
    }
  },

  created() {
    axios.get('http://192.168.122.231:5000/'+'1/homework/'+current)
    .then( response => {
      this.HomeworkTable = response.data
      console.log(this.HomeworkTable)
    })
    .catch( error => {
      this.error = error
    });
  }
}

</script>
