<template>
<div>
  <h1>dashboard page</h1>
  <!--
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
  -->
  <table class="table">
    <th>#</th>
    <th v-for="(item, index) in problem_count" :key="index">Problem: {{item}}</th>

    <tbody>
      <tr v-for="item in DashboardTable" :key="item.name">
        <th>
          {{ item.name }}
          <br/>
          total_solved: {{ item.solved }}
          <br/>
          total_time: {{ item.total_time }}
        </th>
        <td v-for="p in item.problem" :key="p.sequence">
          solved_time: {{ p.solved_time }}
          <br/>
          status: {{p.status}}
          <br/>
          try_count: {{p.try_count}}
        </td>
      </tr>
    </tbody>

  </table>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Exam',
  data() {
    return {
      current: this.$route.params.Exam_id,
      DashboardTable: {},
      problem_count: 0

    }
  },
  created() {
    axios.get("/exam/"+this.current+"/dashboard")
    .then( response => {
      this.DashboardTable = response.data.return_set
      this.problem_count = response.data.problem_count
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