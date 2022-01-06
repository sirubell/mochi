<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>Name</th>
    <th>Start time</th>
    <th>End time</th>
    <tr v-for="item,index in ExamTable" :key="item.id">
      <td>
        <router-link v-if="checkTimeInRange(item.start_time, end_time)" :to="'exam/'+item.exam_id"> {{ index+1 }}</router-link>
        <p v-else>{{ index + 1 }}</p>
      </td>
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
  methods: {
    checkTimeInRange(start_time, end_time) {
      const start = new Date(start_time)
      const end = new Date(end_time)
      const current = new Date()

      return start <= current && current <= end
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

