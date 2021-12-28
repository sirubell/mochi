<template>
<div>
    <h1>this is problem id page</h1>
    <table class="table">
    <tr v-for="item in problemTalbe" :key="item.id">
      <td>{{ item.id }}</td>
    </tr>
    </table>
</div>
</template>

<script>
var current = window.location.pathname;
console.log(current);
import axios from 'axios'

export default {

  created() {
    axios.get('http://127.1.1.1:8000/')
    .then( response => {
      this.problemTalbe = response.data
      console.log(response.data)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
