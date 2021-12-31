<template>
  <div>
    <table class="table" >
      <th>#</th>
      <th>作業名稱</th>
      <th>繳交期限</th>
      <tr v-for="item,counter in HomeworkTable" :key="item.id" >
        <td><a v-bind:href="'http://192.168.122.231:5000/'+'homework/'+item.id">{{counter+1}}</a></td>
        <td>{{ item.name }}</td>
        <td>{{ item.username }}</td>
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
      HomeworkTable: {},
    }
  },

  created() {
    axios.get('http://192.168.122.231:5000/'+'1/homework')
    .then( response => {
      this.HomeworkTable = response.data
      console.log(this.HomeworkTable)
    })
    .catch( error => {
      this.error = error
    });
  }
}

</script>
