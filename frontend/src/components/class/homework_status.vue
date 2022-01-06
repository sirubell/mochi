<template>
<div>
    <h1>課程名稱: {{class_id}}</h1>
    <p >作業名稱: {{name}}</p>
  <table class="table">
    <thead>
      <tr>
        <th scope="col" style="width: 10%">StudentID</th>
        <th scope="col" v-for="(item, index) in problem_count" :key="index">Problem: {{ item }}</th>
      </tr>
    </thead>

    <tbody>
      <tr v-for="item in statusTable" :key="item.student_id">
        <th scope="row">{{ item.student_id }}</th>
        <td v-for="p in item.status" :key="p.sequence">
          <div v-if="p.status === 0" class="alert alert-danger" role="alert">未解</div>
          <div v-if="p.status === 1" class="alert alert-warning" role="alert">寫了但沒過</div>
          <div v-if="p.status === 2" class="alert alert-success" role="alert">已通過</div>
        </td>
      </tr>
    </tbody>

  </table>
  <!-- <p>
    <button v-if ="currentPage > 1 "  v-on:click="page_minus">Previous</button> 
    <l1>第{{currentPage}}頁</l1>
    <button v-if ="maxpage > currentPage "  v-on:click="page_plus">Next</button>
  </p> -->
  
  <div v-if="error">
    {{ error }}
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Status',
  data() {
    return {
      //currentPage:1,
      statusTable: {},
      problem_count: 0,
      class_id: "",
      name: "",
      error: "",
      user_id :this.$store.getters.userId,
      current: this.$route.params.id,
    }
  },
  created() {
    axios.get('/homework_status/'+this.current)
    .then( response => {
      this.statusTable = response.data.status_table
      this.problem_count = response.data.problem_count
      this.name = response.data.name
      this.class_id = response.data.class_id
    //   this.maxpage=response.data.maxpage
      console.log(this.status_detail)
    })
    .catch( error => {
      this.error = error
    });
  },
}
</script>
