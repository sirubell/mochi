<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>題目名稱</th>
    <th>作答狀況</th>
    <tr v-for="item in ExamTable" :key="item.id" >
      <td><a v-bind:href="'exam/'+ExamID+'/'+item.id">{{ item.id }}</a></td>
      <td>{{ item.title }}</td>
      <td>{{ item.userId }}</td>
    </tr>
  </table>
  <div v-if="error">
    {{ error }}
  </div>
  
</div>

</template>

<script>
var current = window.location.pathname;
import axios from 'axios'

export default {
  name: 'Exam',
  data() {
    return {
      ExamTable: {}
    }
  },
  created() {
    axios.get('http://192.168.122.231:5000/')
    .then( response => {
      this.ExamTable = response.data
      this.ExamID=current.substr(9,1)
      console.log(response.data)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>