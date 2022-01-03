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


  <button @click="pageMinus" type="button" class="btn btn-outline-primary">Previous</button>
  <button @click="pagePlus" type="button" class="btn btn-outline-primary">Next</button>
  <h1>{{ currentPage }}</h1>
  <error v-if="error" :error="error" />
  
</div>

</template>

<script>
import Error from '../error.vue'

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
      })
      .catch( error => {
        this.error = error
      });
    }
  },
  created() {
    this.reloadTable()
  },
  components: [
    Error
  ]
}
</script>
