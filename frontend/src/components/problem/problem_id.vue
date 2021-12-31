<template>
<div>
    <h1>this is problem id page</h1>
    <p>Problem id = {{ problemID }}</p>
      <p><em>題目敘述 : </em>{{ ProblemContent.content }}</p>
      <p><em>範例輸入 : </em>{{ ProblemContent.difficulty }}</p>
      <p><em>範例輸出 : </em>{{ ProblemContent.name }}</p>
    <button ><a v-bind:href="problemID+'/dashboard'">通過紀錄</a></button>
    <!-- <ul v-for="item in ProblemContent" :key="item.id">
      <p><em>題目敘述 : </em>{{ item.content }}</p>
      <p><em>範例輸入 : </em>{{ item.difficulty }}</p>
      <p><em>範例輸出 : </em>{{ item.name }}</p>
    </ul>-->

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
    axios.get('http://192.168.122.231:5000/'+'problem/'+current.substr(9))
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
