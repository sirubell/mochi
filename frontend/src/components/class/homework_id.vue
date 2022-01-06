<template>
  <div>
    <table class="table" >
      <th>#</th>
      <th>題目名稱</th>
      <th>Sequence</th>
      <tr v-for="item,counter in HomeworkTable" :key="item.id" >
        <td><a v-bind:href="current+'/problem/'+item.problem_id">{{counter+1}}</a></td>
        <td>{{ item.problem_name }}</td>
        <td>{{ item.sequence }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Homework',
  data() {
    return {
      current: this.$route.params.id,
      HomeworkTable: {},
    }
  },

  created() {
    axios.get('/homework/'+this.current)
    .then( response => {
      this.HomeworkTable = response.data.problem_set
      console.log(this.current)
    })
    .catch( error => {
      this.error = error
    });
  }
}

</script>
