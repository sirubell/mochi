<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>User Name</th>
    <th>language</th>
    <th>status</th>
    <th>time</th>
    <th>memory</th>
    <th>upload_date</th>
    <tr v-for="item,index in statusTable" :key="item.id" >
      <td><!--<router-link :to="'/problem/' + item.id"> {{ index+1 }} </router-link>-->{{ index+1 }}</td>
      <td>{{ item.name }}</td>
      <td>{{ item.language }}</td>
      <td>{{ item.status }}</td>
      <td>{{ item.time }} ms</td>
      <td>{{ getMemory(item.memory) }} MB</td>
      <td>{{ item.upload_date }}</td>
    </tr>
  </table>
  <p>
    <button v-if ="currentPage > 1 "  v-on:click="page_minus">Previous</button> 
    <l1>第{{currentPage}}頁</l1>
    <button v-if ="maxpage > currentPage "  v-on:click="page_plus">Next</button>
  </p>
  
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
      currentPage:1,
      maxPage: null,
      statusTable: {},
      error: "",
      user_id :this.$store.getters.userId
    }
  },
   methods:{
    page_plus (){
      this.currentPage+=1
      this.reloadtable()
    },
    page_minus (){
      this.currentPage-=1
      this.reloadtable()
    },
    reloadtable (){
      axios.get('status?page='+this.currentPage)
      .then( response => {
        this.statusTable = response.data.returnset
        console.log(this.currentPage)
      })
      .catch( error => {
        this.error = error
      });
    },
    getMemory(memory_kb) {
      return parseInt(memory_kb / 1024)
    }
  },
  created() {
    axios.get('status', {
      params: {
        page: this.currentPage
      }
    })
    .then( response => {
      this.statusTable = response.data.returnset
      this.maxpage=response.data.maxpage
      console.log(response.data.maxpage)
    })
    .catch( error => {
      this.error = error
    });
  },
}
</script>
