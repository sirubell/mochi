<template>
<div style="background:#ffff">
  <table class="table" >
    <th>#</th>
    <th>Exam</th>
    <th>Time left</th>
    <tr v-for="item in ExamTable" :key="item.id" >
      <td><a v-bind:href="'exam/'+item.id">{{ item.id }}</a></td>
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

import axios from 'axios'

export default {
  name: 'Exam',
  data() {
    return {
      ExamTable: {}
    }
  },
  created() {
    axios.get('http://192.168.122.231:5000/'+'1/exam')
    .then( response => {
      this.ExamTable = response.data
      console.log(response.data)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>

