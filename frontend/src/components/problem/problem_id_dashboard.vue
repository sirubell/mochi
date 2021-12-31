<template>
<div>
    <h1>this is id dashboard page</h1>
    <p>Problem id = {{ problemID }}</p>
    <ul v-for="item in problemTable" :key="item.id">
      <!-- <p><em>題目敘述 : </em>{{ item.info }}</p>
      <p><em>範例輸入 : </em>{{ item.sample_input }}</p>
      <p><em>範例輸出 : </em>{{ item.sample_output }}</p> -->
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
    axios.get('http://127.1.1.1:8000/'/*+current.substr(-11,1)*/)
    .then( response => {
      this.problemTable = response.data
      this.problemID=current.substr(-11,1)
      // console.log(current.substr(-1,1))
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>