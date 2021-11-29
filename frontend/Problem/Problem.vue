<template>
  <div>
    <div id="problem">
      <h1>This is a problem page</h1>
      <h1><router-link to="/problem/new">Add question</router-link></h1>
      <h1><router-link to="/problem/problem_id">題目標題</router-link></h1>
    </div>
    <div id ="app">
    <table border="1px" style="width: 400px;" class="table table-striped table-bordered table-hover table-condensed">
      <thead>
         <tr>
           <th>序號</th>
           <th>姓名</th>
           <th>性別</th>
           <th>年齡</th>
         </tr>
      </thead>
     <tr v-for="student in stuData" :key="student">
       <td>{{ student.stuId }}</td>
       <td>{{ student.stuName }}</td>
       <td>{{ student.stuSex }}</td>
       <td>{{ student.stuAge }}</td>
     </tr>
    </table>
    <!-- 用無序列表做一個頁碼導航條-->
    <ul>
      <li><a href="#" @click="prePage">  </a></li>
      <li v-for="(value,index) in pageNumber" :key="index">
       <a href="#" @click="thisPage(index)">{{ index+1 }}</a>
      </li>
      <li><a href="#" @click="nextPage"> > </a></li>
    </ul>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
//建立Vue例項,得到 ViewModel
   var app = new Vue({
    el: '#app',
    data: {
     list:[],
     pageSize:3,//每頁大小
     currentPage:0 //當前頁碼

    },/*資料*/
    mounted(){
     //非同步載入json資料
     axios.get('/json/student.json',{}).then(function(response){
      app.list=response.data;
     });
    },/*自動載入函式*/
    methods: {
      //上一頁
      nextPage: function(){
            if (this.currentPage == this.pageNumber - 1) return;
            this.currentPage++;
        },
        //下一頁
        prePage: function(){
            if (this.currentPage == 0) return;
            this.currentPage--;
        },
        //頁碼
        thisPage: function(index){
           this.currentPage = index;
        }
    },/*執行觸發函式*/
    computed: {
      //分頁資料
      stuData: function(){
            let left = this.currentPage*this.pageSize;
            let right = Math.min((this.currentPage+1)*this.pageSize, this.list.length)
            return this.list.slice(left, right);//取出一頁資料
        },
        //共有多少頁
        pageNumber: function(){
            return Math.ceil(this.list.length / this.pageSize)||1;
        }
    },/*動態計算屬性*/
   });
</script>

<style>
ul{
  list-style: none;
}
li{
  display: inline;
}
#problem {
  text-align: center;
  vertical-align: center;
  font-size: 25px;
  line-height: 50px;
  letter-spacing: 4px;
}
</style>
