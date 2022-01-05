<template>
    <div>
        <h1> Submission</h1>
        <!-- <table class="table" >
            <th>#</th>
            <th>User Name</th>
            <th>language</th>
            <th>status</th>
            <th>upload_date</th> -->
            <tr v-for="item,index in statusTable" :key="item.submission_id" >
            <td><router-link :to="'/submission/' + item.submission_id"> {{ index+1 }}</router-link></td>
            <h3>{{ item.time_used }}</h3>
            <h3>{{ item.code_content }}</h3>
            </tr>
        <!-- </table> -->
        <!-- <div v-if="error">
            {{ error }}
        </div> -->
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Submission',
    data() {
        return {
            statusTable: {},
            // error: "",
        }
    },
    created() {
    axios.get('status?page='+this.currentPage)
    .then( response => {
      this.statusTable = response.data.returnset
      this.maxpage=response.data.maxpage
      console.log(response.data.maxpage)
    })
    .catch( error => {
      this.error = error
    });
  },
}
</script>
