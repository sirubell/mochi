<template>
<div>
  <table class="table" >
    <th>#</th>
    <th>Problem name</th>
    <th>Difficulty</th>
    <th>Questioner_id</th>
    <th>Delete</th>
    <tr v-for="item in problemTable" :key="item.id" >
      <td><router-link :to="'/problem/' + item.id">{{ item.id }}</router-link></td>
      <td>{{ item.name }}</td>
      <td>{{ item.difficulty }}</td>
      <td>{{ item.questioner_id }}</td>
      <td v-if="user_id==item.questioner_id"><button v-on:click="delete_question(item.id,user_id)">{{user_id}}</button></td>
    </tr>
  </table>

  <p>
    <button v-if ="currentPage > 1 "  v-on:click="page_minus">Previous</button> 
    <button v-if ="maxpage > currentPage "  v-on:click="page_plus">Next</button>
  </p>
  <h1>{{currentPage}}</h1>
  <div v-if="error">
    {{ error }}
  </div>
  
</div>

</template>

<script>
// import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  data() {
    return {
      currentPage:1,
      problemTable: {},
      error: "",
      user_id :this.$store.getters.userId
    }
  },
  methods:{
    page_plus (){
      this.currentPage+=1
      this.reloadtable()
      // console.log(this.currentPage)
    },
    page_minus (){
      this.currentPage-=1
      this.reloadtable()
    },
    delete_question :function(id,user){
      console.log(user)
      axios.delete('problem/'+id+'?user'+user,{
        data: {
           user:user
         },
      });
    },
    reloadtable (){
      axios.get('problem?page='+this.currentPage)
      .then( response => {
        this.problemTable = response.data.returnset
        console.log(this.currentPage)
      })
      .catch( error => {
        this.error = error
      });
    },
  },
  created() {
    axios.get('problem?page='+this.currentPage)
    .then( response => {
      this.problemTable = response.data.returnset
      this.maxpage=response.data.maxpage
      console.log(response.data.maxpage)
    })
    .catch( error => {
      this.error = error
    });
  },
}

</script>

