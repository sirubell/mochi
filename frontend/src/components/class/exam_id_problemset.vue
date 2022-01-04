<template>
<div>
  <h1>{{ Exam_name }}</h1>
  <li>Start Time : {{ Examstarttime }}</li>
  <table class="table" >
    <th>#</th>
    <th>題目名稱</th>
    <th>sequence</th>
    <tr v-for="item,index in ExamTable" :key="item.id" >
      <td><a v-bind:href="'/problem/' + item.problem_id">{{ index+1 }}</a></td>
      <td>{{ item.problem_name }}</td>
      <td>{{ item.sequence }}</td>
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
    axios.get(current.substr(6))
    .then( response => {
      this.ExamTable = response.data.problem_set
      this.ExamID=current.substr(6)
      this.Examstarttime = response.data.start_time
      this.Exam_name = response.data.name
      console.log(response.data)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>