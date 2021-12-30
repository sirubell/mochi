<template>
<div>
    <h1>this is problem id page</h1>

    <ul v-for="item in problemTable" :key="item.id">
      <p>{{ item.id }}</p>
      <p><em>題目敘述 : </em>{{ item.info }}</p>
      <p><em>範例輸入 : </em>{{ item.sample_input }}</p>
      <p><em>範例輸出 : </em>{{ item.sample_output }}</p>
      <button v-bind:href="item.id">通過紀錄</button>
    </ul>

</div>
</template>

<script>
var current = window.location.pathname;
console.log(current);
import axios from 'axios'

export default {
  data() {
    return {
      problemTable: {},
    }
  },
  created() {
    axios.get('http://127.1.1.1:8000/')
    .then( response => {
      this.problemTable = response.data
      console.log(this.problemTable)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
