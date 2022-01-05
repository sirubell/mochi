<template>
  <div class="container">
    <div class="row">
      <div class="col-6 test-start">
        <div class="mb-3">
          <label for="problemName" class="form-label">Homework Name</label>
          <input v-model="homework_name" type="text" class="form-control" id="problemName">
        </div>
        <div class="mb-3">
          <label for="problemDescription" class="form-label">Homework information</label>
          <textarea v-model="homework_info" class="form-control" id="problemDescription" placeholder="" rows="5" style="resize: none;"></textarea>
        </div>
        <div class="row mb-3">
          <div class="col">
            <div class="mb-3">
              <label for="timeLimit" class="form-label">Upload Time</label>
            </div>
            <input type="date" id="start" name="trip-start"  min="2022-01-01" max="2022-12-31" v-model="homework_start_time_date">
            <input type="time" id="appt" name="appt" min="00:00" max="23:59" v-model="homework_start_time_time" required>
          </div>
          <div class="col">
            <div class="mb-3">
              <label for="timeLimit" class="form-label">Deadline</label>
            </div>
            <input type="date" id="start" name="trip-start"  :min="homework_start_time_date" max="2022-12-31" v-model="homework_end_time_date">
            <input type="time" id="appt" name="appt" :min="homework_start_time_time" max="23:59" v-model="homework_end_time_time" required>
          </div>
        </div>
      </div>
      <div class="col-6">
          <table class="table" >
            <th>#</th>
            <th>Problem name</th>
            <th>Difficulty</th>
            <th>Pick</th>
            <tr v-for="item,index in problemTable" :key="item.id" >
                <td><router-link :to="'/problem/' + item.id"> {{ index+1 }} </router-link></td>
                <td>{{ item.name }}</td>
                <td>{{ item.difficulty }}</td>
                <td><input type="checkbox" :id=item.id :value=item.id v-model="problem_set" /><label :for=item.id >{{item.id}}</label></td>
            </tr>
          </table>
          <p>
              <button v-if ="currentPage > 1 "  v-on:click="page_minus">Previous</button> 
              <l1>第{{currentPage}}頁</l1>
              <button v-if ="maxpage > currentPage "  v-on:click="page_plus">Next</button>
          </p>
      </div>
    </div>
    <div>
      <error v-if="error" :error="error"/>
      <loading v-if="loading" :loading="'Testcases is running'"/>
      <Info v-if="return_status" :info="return_status"/>
    </div>
    <div class="my-2">
      <button type="button" class="btn btn-success m-2" @click="onSumit">Submit</button>
    </div>
  </div>
</template>

<script>
import 'ace-builds/src-noconflict/theme-chrome'
import axios from 'axios'
import Error from '../error.vue'
import Loading from '../loading.vue'
import Info from '../info.vue'

export default {
    
  name: "NewHomework",
  data() {
    return {
      homework_name: "",
      homework_info: "",
      homework_start_time_date: "",
      homework_start_time_time: "",
      homework_end_time_date: "",
      homework_end_time_time: "",
      problem_set: [],

      //current: this.$route.params.id,
      currentPage:1,
      problemTable: {},
      source_id: null,
      error: null,
      loading: null,
      return_status: null
    }
  },
  watch: {
    homework_start_time_date() {
      this.homework_end_time_date = this.homework_start_time_date
    },
    homework_start_time_time() {
      this.homework_end_time_time = this.homework_start_time_time
    }
  },
  methods: {
    checkTime() {
      const start = new Date(this.homework_start_time_date + ' ' + this.homework_start_time_time)
      const end = new Date(this.homework_end_time_date + ' ' + this.homework_end_time_time)

      return start < end
    },
    editorInit() {
      // do nothing
    },
    onSumit() {
      if (!this.checkTime()) {
        this.error = "Time is invalid."
        return
      }
      if (this.homework_name ==null) {
        this.error = "You have to give the homework a name!"
        return
      }
      if (this.homework_info ==null) {
        this.error = "You have to give the homework an info!"
        return
      }

      const postData = {
        class_id: 1,//this.current,
        user_id: 1,//this.$store.getters.userInfo.user_id,
        homework_name: this.homework_name,
        homework_info: this.homework_info,
        upload_time: this.homework_start_time_date+" "+this.homework_start_time_time+":00",
        deadline: this.homework_end_time_date+" "+this.homework_end_time_time+":59",
        problem_set: this.problem_set,
      }

      axios.post('/homework', postData)
      .then( res => {
        const code = res.data.code
        
        if (code === 200) {
          this.return_status = res.data.message
        } else {
          this.error = res.data.message
        }
      })
      .catch( () => {
        this.error = "Homework Name is already be taken."
      })
    },
    page_plus (){
      this.currentPage+=1
      this.reloadtable()
    },
    page_minus (){
      this.currentPage-=1
      this.reloadtable()
    },
    reloadtable (){
      axios.get('problem?page='+this.currentPage)
      .then( response => {
        this.problemTable = response.data.returnset
        console.log(this.problem_set)
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
      console.log(response.data.returnset)
    })
    .catch( error => {
      this.error = error
    });
  },
  components: {
    Error,
    Loading,
    Info
  }
}
</script>

<style>
#editor *{
  font-family : monospace !important;font-size: 20px !important;direction:ltr !important;text-align:left !important;
}
</style>
