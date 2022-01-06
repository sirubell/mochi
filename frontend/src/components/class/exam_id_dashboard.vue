<template>
<div>
  <h1>dashboard page</h1>
  <li v-for="item in DashboardTable" :key="item.problem" >
  <table class="table" >
    <th>名字</th>
    <th v-for="index in item.problem" :key="index.sequence" :style="{width: '100px'}">{{index.sequence}}</th>
    <th>Solved</th>
    <th>Total time</th>
    
    <tr v-for="item in DashboardTable" :key="item.name" >
      <td>{{ item.name }}</td>
      <th v-for="index in item.problem" :key="index.sequence">
        <tr>時間:{{ index.solved_time }}</tr>
        <tr>解題狀態:{{ index.status }}</tr>
        <tr>嘗試次數:{{ index.try_count }}</tr>
      </th>
      <td>{{ item.solved }}</td>
      <td>{{ item.total_time }}</td>
    </tr>
  </table>
  </li>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Exam',
  data() {
    return {
      current: this.$route.params.Exam_id,
      DashboardTable: {}
    }
  },
  created() {
    axios.get("/exam/"+this.current+"/dashboard")
    .then( response => {
      this.DashboardTable = response.data.return_set
      console.log(this.DashboardTable)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>

<style>
li {
    display: block;
}
</style>