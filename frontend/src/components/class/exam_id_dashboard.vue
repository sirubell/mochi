<template>
<div>
  <h1>dashboard page</h1>
  <table class="table">
    <thead>
      <tr>
        <th scope="col" style="width: 10%">#</th>
        <th scope="col" style="width: 8%">Total Solved</th>
        <th scope="col" style="width: 8%">Total Time</th>
        <th scope="col" v-for="(item, index) in problem_count" :key="index">Problem: {{item}}</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="item in DashboardTable" :key="item.name">
        <th scope="row">{{ item.name }}</th>
        <td>{{ item.solved }}</td>
        <td>{{ item.total_time }}</td>
        <td v-for="p in item.problem" :key="p.sequence">
          <div class="alert" :class="p.status === 1 ? 'alert-success' : alert-danger" role="alert">
            <h2>{{ p.solved_time }}</h2>
           {{p.try_count}} Try
          </div>
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
