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
    <button @click="pageMinus()">Previous</button> 
    <button @click="pagePlus()">Next</button>
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
  methods: {
    pagePlus() {
      this.currentPage += 1
      this.reloadTable()
      console.log(this.currentPage)
    },
    pageMinus (){
      if (this.currentPage > 1) {
        this.currentPage -= 1
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
    axios.get('problem?page='+this.currentPage)
    .then( response => {
      this.problemTable = response.data.returnset
      console.log(this.currentPage)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
