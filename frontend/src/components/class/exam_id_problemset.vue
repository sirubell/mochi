<template>
<div>
  <h1>{{ Exam_name }}</h1>
  <li>Start Time : {{ Examstarttime }}</li>
  <table class="table" >
    <th>#</th>
    <th>題目名稱</th>
    <th>sequence</th>
    <tr v-for="item,index in ExamTable" :key="item.id" >
      <td><a v-bind:href=" item.exam_id  + '/' + item.problem_id">{{ index+1 }}</a></td>
      <td>{{ item.problem_name }}</td>
      <td>{{ item.sequence }}</td>
      <!-- <td>{{ ExamID }}</td> -->
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
      current: this.$route.params.id,
      ExamTable: {}
    }
  },
  created() {
    axios.get("/exam/"+this.current)
    .then( response => {
      this.ExamTable = response.data.problem_set
      this.ExamID=this.current
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