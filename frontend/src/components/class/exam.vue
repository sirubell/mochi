<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>Name</th>
    <th>Start time</th>
    <th>End time</th>
    <tr v-for="item,index in ExamTable" :key="item.id" >
      <td><router-link :to="'exam/'+item.exam_id"> {{ index+1 }} </router-link></td>
      <td>{{ item.name }}</td>
      <td>{{ item.start_time }}</td>
      <td>{{ item.end_time }}</td>
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
    axios.get('class/1/exam')
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

