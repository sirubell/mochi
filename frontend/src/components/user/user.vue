<template>
  <!-- <h1>User is not implemented.</h1> -->
<div class="container-fluid">
  <div class="row">
    <!-- <a href="/" class="d-flex align-items-center pb-3 mb-3 link-dark text-decoration-none border-bottom">
      <svg class="bi me-2" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
      <span class="fs-5 fw-semibold">Refresh</span>
    </a> -->
    <nav id="sidebarMenu" class="col-md-3 col-lg-2 d-md-block bg-light sidebar collapse">
      <div class="position-sticky pt-3">
        <ul class="nav flex-column">
          <li class="mb-1">
            <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#home-collapse" aria-expanded="true">
              My profile
            </button>
          </li>
          <li class="mb-1">
            <button class="btn btn-toggle align-items-center rounded collapsed" data-bs-toggle="collapse" data-bs-target="#dashboard-collapse" aria-expanded="false">
              Tried Problem
            </button>
            <div class="collapse" id="dashboard-collapse">
              <ul class="btn-toggle-nav list-unstyled fw-normal pb-1 small">
                <li><a href="#" class="link-dark rounded">Overview</a></li>
                <li><a href="#" class="link-dark rounded">Weekly</a></li>
                <li><a href="#" class="link-dark rounded">Monthly</a></li>
                <li><a href="#" class="link-dark rounded">Annually</a></li>
              </ul>
            </div>
          </li>
          <li class="mb-1">
              <router-link to="/change_profile" class="btn btn-toggle align-items-center rounded collapsed" data-bs-target="#orders-collapse" aria-expanded="false">
                Change Profile
              </router-link>
          </li>
          <li class="border-top my-3"></li>
        </ul>
      </div>
    </nav>
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4 fs-3">
      <!-- <div class="justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"> -->
        <h2 class="d-flex border-bottom">Profile</h2>
        <div class="d-flex mb-3 row">
          <label for="staticName" class="col-sm-2 col-form-label">Name</label>
          <div class="col-sm-10">
            <input type="text" readonly class="form-control-plaintext" id="staticName" :value="userInfo.name">
          </div>
        </div>
        <div class="d-flex mb-3 row">
          <label for="staticEmail" class="col-sm-2 col-form-label">Email</label>
          <div class="col-sm-10">
            <input type="text" readonly class="form-control-plaintext" id="staticEmail" :value="userInfo.email">
          </div>
        </div>
        <div class="d-flex mb-3 row">
          <label for="staticUserId" class="col-sm-2 col-form-label">Id</label>
          <div class="col-sm-10">
            <input type="text" readonly class="form-control-plaintext" id="staticUserId" :value="userInfo.user_id">
          </div>
        </div>
        <div class="d-flex mb-3 row">
          <label for="staticRegisterDate" class="col-sm-2 col-form-label">Register Date</label>
          <div class="col-sm-10">
            <input type="text" readonly class="form-control-plaintext" id="staticRegisterDate" :value="userInfo.register_date">
          </div>
        </div>
      <!-- </div> -->
    </main>
  </div>
</div>
</template>

<script>
import { mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'User',
  data() {
    return {
      userInfo: {},
      error: null
    }
  },
  computed: {
    ...mapGetters([
      'userId'
    ])
  },
  created() {
    axios.get('/user/myprofile')
    .then(res => {
      this.userInfo = res.data
      console.log(res.data)
    }).catch(e => { 
      this.error = e
    })
  }
}
</script>
