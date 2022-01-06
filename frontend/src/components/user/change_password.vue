<template>
<div class="container-fluid" >
  <div class="row">
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light collapse">
      <div class="list-unstyled ps-0">
        <ul class="nav flex-column">
          <li class="mb-1">
              <router-link to="/user" class="btn btn-toggle align-items-center rounded collapsed" data-bs-target="#home-collapse" aria-expanded="true">
                My profile
              </router-link>
          </li>
          <!-- <li class="mb-1">
            <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse" aria-expanded="false">
              Tried Problem
            </button>
            <div class="collapse" id="dashboard-collapse">
              <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                <li><router-link to="/" class="link-dark rounded">Overview</router-link></li>
                <li><a href="#" class="link-dark rounded">Weekly</a></li>
                <li><a href="#" class="link-dark rounded">Monthly</a></li>
                <li><a href="#" class="link-dark rounded">Annually</a></li>
              </ul>
            </div>
          </li> -->
          <li class="mb-1">
            <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#account-collapse" aria-expanded="false">
              Change Profile
            </button>
            <div class="collapse" id="account-collapse">
              <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                <li><router-link to="/change_email" class="link-dark rounded">Change Name / Email</router-link></li>
                <li><router-link to="/change_password" class="link-dark rounded">Change Password</router-link></li>
              </ul>
            </div>
          </li>
          <li class="border-top my-3"></li>
        </ul>
      </div>
    </nav>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <!-- <div class="justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"> -->
      <form @submit.prevent="ChangePassword"> 
        <h2 class="d-flex border-bottom">Change Password</h2>
        <div class="edit">    
          <div class="edit-item">
            <span class="label d-flex">Change password :</span>
            <input type="password" class="form-control create-input d-flex" v-model="password" placeholder="Edit password"/>
          </div>
          <div class="edit-item">
            <span class="label d-flex" style="margin-top:10px">Confirm password :</span>
            <input type="password" class="form-control create-input d-flex" v-model="confirm_password" placeholder="Confirm password"/>
          </div>
          <button class="send d-flex btn btn-primary btn-block" style="margin-top:10px" @click="save">save</button>
        </div>
      </form>
    </main>
  </div>
</div>
</template>

<script>
import axios from 'axios'
// import Error from '../error.vue'

export default {
    name: 'Change_Password',
    data() {
      return {
        password: '',
        confirm_password: '',
        error: ''
      }
    },
    components: {
        // Error
    },
    methods: {
        async ChangePassword(){ //利用 try catch 作錯誤偵測
            try{
                const response = await axios.put('user/change_profile_password', {
                    password: this.password,
                    confirm_password: this.confirm_password
                }); // 資料由後方物件帶入 
                console.log(response);
                this.$router.push('/user');
            }
            catch(e){
                this.error = e;
            }
        }
    },
    created(){
        axios.get('http://192.168.122.134:5000/user/change_profile_password')
      .then( response => {
        this.data = response.data
        console.log(this.data)
      })
      .catch( () => {
        this.error = 'Invalid password!'
      });
    },
}
</script>

<style>

</style>
