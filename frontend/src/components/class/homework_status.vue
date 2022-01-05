<template>
<div>
    <h1>{{status_detail.class_id}}</h1>
    <p >{{status_detail.name}}</p>
  <table class="table" >
    <th>#</th>
    <th>status</th>
    <th>student_id</th>
    <tr v-for="item,index in statusTable" :key="item.id" >
      <td>{{ index+1 }}</td>
      <td>{{ item.status }}</td>
      <td>{{ item.student_id }}</td>
      <!-- <td>{{ item.status }}</td>
      <td>{{ item.upload_date }}</td> -->
    </tr>
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
      status_detail:{},
      error: "",
      user_id :this.$store.getters.userId,
      current: this.$route.params.id,
    }
  },
  created() {
    axios.get('/homework_status/'+this.current)
    .then( response => {
      this.statusTable = response.data.status_table
      this.status_detail = response.data
    //   this.maxpage=response.data.maxpage
      console.log(this.status_detail)
    })
    .catch( error => {
      this.error = error
    });
  },
}
</script>
