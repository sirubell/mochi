<template>
<div style="background:#ffff">
  <h1>dashboard page</h1>
  <table class="table" >
    <th>名字</th>
    <th>題目</th>
    <th>Solved</th>
    <th>Total time</th>
    <tr v-for="item in DashboardTable" :key="item.name" >
      <td>{{ item.name }}</td>
      <!-- <td>{{ item.problem }}</td> -->
      <td>{{ item.solved }}</td>
      <td>{{ item.total_time }}</td>
    </tr>
  </table>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Exam',
  data() {
    return {
      current: this.$route.params.id,
      DashboardTable: {}
    }
  },
  created() {
    axios.get("/exam/"+this.current+"/dashboard")
    .then( response => {
      this.DashboardTable = response.data.return_set
      console.log(this.current)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>

<style>

</style>