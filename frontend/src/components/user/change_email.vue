<template>
<div class="container-fluid">
  <div class="row">
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="position-sticky pt-3">
        <ul class="nav flex-column">
          <li class="mb-1">
              <router-link to="/user" class="btn btn-toggle align-items-center rounded collapsed" data-bs-target="#home-collapse" aria-expanded="true">
                My profile
              </router-link>
          </li>
          <li class="mb-1">
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
          </li>
          <li class="mb-1">
            <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#account-collapse" aria-expanded="false">
              Change Profile
            </button>
            <div class="collapse" id="account-collapse">
              <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                <li><router-link to="/change_email" class="link-dark rounded">Change Email</router-link></li>
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
      <form @submit.prevent="ChangeEmail"> 
        <h2 class="d-flex border-bottom">Change Profile</h2>
        <div class="edit">    
          <div class="edit-item">
            <span class="label d-flex">Change name :</span>
            <input type="text" class="form-control create-input d-flex" v-model="name" placeholder="Edit name"/>
          </div>
          <div class="edit-item">
            <span class="label d-flex" style="margin-top:10px">Confirm email :</span>
            <input type="email" class="form-control create-input d-flex" v-model="email" placeholder="Edit email"/>
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

export default {
  name: 'Change_Email',
  data() {
    return {
      name: "",
      email: "",
      error: null
    }
  },
  methods: {
    save() {
      const payload = {
        name: this.name,
        email: this.email
      }
      axios.put('/user/change_profile_name_email', payload)
      .then( () => this.$router.push('/user'))
      .catch ( error => {
        this.error = error
      })
    }
  },
  created() {
    if (this.$store.getters.userInfo === null) {
      this.$router.push('/login')
    }
    this.name = this.$store.getters.userInfo.name
    this.email = this.$store.getters.userInfo.email
  }
}
</script>

<style>

</style>
