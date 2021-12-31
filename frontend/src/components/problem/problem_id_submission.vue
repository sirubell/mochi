<template>
<div>
    <h1>this is id dashboard page</h1>
    <!-- <p>Problem id = {{ problemID }}</p> -->
    <ul v-for="item in problemTable" :key="item.id">
      <p>{{ item.status }}</p>
      <p>{{ item.language }}</p>
      <p>{{ item.submission_id }}</p>
      <p>{{ item.upload_date }}</p>
      <p>-----------------------------------------------------------------------------</p>
    </ul>

</div>
</template>

<script>
var current = window.location.pathname;
import axios from 'axios'

export default {
  data() {
    return {
      problemTable: {},
    }
  },

  created() {
    axios.get('http://192.168.122.231:5000/'+'problem/'+current.substr(9,1)+'/submission')
    .then( response => {
      this.problemTable = response.data.returnset
      this.problemID=current.substr(9,1)
      console.log(response.data)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>