<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>Problem name</th>
    <th>Difficulty</th>
    <tr v-for="item in problemTable" :key="item.id" >
      <td><router-link :to="'/problem/' + item.id">{{ item.id }}</router-link></td>
      <td>{{ item.name }}</td>
      <td>{{ item.difficulty }}</td>
    </tr>
  </table>

  <p>
    <button v-on:click="page_minus">Previous</button> 
    <button v-on:click="page_plus">Next</button>
  </p>
  <h1>{{currentPage}}</h1>
  <div v-if="error">
    {{ error }}
  </div>
  
</div>

</template>

<script>

import axios from 'axios'

export default {
  data() {
    return {
      currentPage:1,
      problemTable: {},
      error: ""
    }
  },
  method:{
    page_plus (){
      this.currentPage+=1
      this.reloadTable()
      console.log(this.currentPage)
    },
    page_minus (){
      if (this.currentPage > 1) {
        this.currentPage-=1
        this.reloadTable()
      }
    },
    reloadTable() {
      axios.get('problem?page='+this.currentPage)
      .then( response => {
        this.problemTable = response.data.returnset
        console.log(this.currentPage)
      })
      .catch( error => {
        this.error = error
      });
    }
  },
  created() {
    this.reloadTable()
  }
}
</script>
