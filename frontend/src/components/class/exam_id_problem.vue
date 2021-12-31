<template>
<div>
    <h1>this is exam id page</h1>
    <p>Problem id = {{ ExamID }}</p>
      
    <button ><a v-bind:href="ExamID+'/dashboard'">通過紀錄</a></button>
    <ul v-for="item in ProblemContent" :key="item.id">
      <p><em>題目敘述 : </em>{{ item.info }}</p>
      <p><em>範例輸入 : </em>{{ item.sample_input }}</p>
      <p><em>範例輸出 : </em>{{ item.sample_output }}</p>
    </ul>

</div>
</template>

<script>
var current = window.location.pathname;
import axios from 'axios'

export default {
  data() {
    return {
      ProblemContent: {},
    }
  },

  created() {
    axios.get('http://192.168.122.231:5000/'+current.substr(12))
    .then( response => {
      this.ProblemContent = response.data
      this.ExamID = current.substr(12)
      console.log(current.substr(12))
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
