<template>
<div>
    <h1>this is id dashboard page</h1>
    <!-- <p>Problem id = {{ problemID }}</p> -->
    <table class="table" >
    <th>#</th>
    <th>Problem name</th>
    <th>language</th>
    <th>status</th>
    <th>upload_date</th>
    <tr v-for="item,index in problemTable" :key="item.id" >
      <td>
        <!-- <router-link :to="'/problem/' + item.id"> {{ index+1 }} </router-link> -->
          {{ index+1 }}
        </td>
      <td>{{ item.name }}</td>
      <td>{{ item.language }}</td>
      <td>{{ item.status }}</td>
      <td>{{ item.upload_date }}</td>
    </tr>
  </table>

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
    axios.get('status?page='+1+"&&problem_id="+current.substr(20))
    .then( response => {
      this.problemTable = response.data.returnset
      this.code=response.data.code
      this.problemID=current.substr(20)
      // console.log(current.substr(20))
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>