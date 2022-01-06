<template>
<div style="background:#ffff">
    <h1>this is problem id page</h1>
    <p>Problem id = {{ problemID }}</p>
      <p><em>題目敘述 : </em>{{ ProblemContent.content }}</p>
      <p><em>範例輸入 : </em>{{ ProblemContent.name }}</p>
      <p><em>範例輸出 : </em>{{ ProblemContent.sample_output }}</p>
    <button ><a v-bind:href="problemID+'/dashboard'">通過紀錄</a></button>

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
    axios.get('problem/'+current.substr(9))
    .then( response => {
      this.ProblemContent = response.data
      this.problemID = current.substr(9)
      console.log(this.ProblemContent)
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
