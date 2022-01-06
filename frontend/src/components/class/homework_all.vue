<template>
  <div>
    <table class="table" >
      <th>#</th>
      <th>作業名稱</th>
      <th>繳交期限</th>
      <th>查看同學繳交情形</th>
      <tr v-for="item,counter in HomeworkTable" :key="item.id" >
        <td>
          <a v-if="checkTime(item.deadline)" v-bind:href="item.homework_id">{{counter+1}}</a>
          <p>{{ counter + 1 }}</p>
        </td>
        <td>{{ item.name }}</td>
        <td>{{ item.deadline }}</td>
        <td><a v-bind:href="'/class/homework_status/'+item.homework_id">查看</a></td>
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
  methods: {
    checkTime(deadline) {
      const end = new Date(deadline)
      const current = new Date()

      return current < end
    }
  },

  created() {
    axios.get('class/1/homework')
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
