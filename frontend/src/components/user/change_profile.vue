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
                <li><router-link to="/reset" class="link-dark rounded">Overview</router-link></li>
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
    <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
      <!-- <div class="justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom"> -->
        <h2 class="d-flex border-bottom">Change Profile</h2>
        <div class="edit">
          <div class="edit-item">
            <span class="label d-flex">Change email :</span>
            <input type="email" class="create-input d-flex" v-model="email" placeholder="Edit email"/>
          </div>
          <div class="edit-item">
            <span class="label d-flex">Change password :</span>
            <input type="password" class="create-input d-flex" v-model="password" placeholder="Edit password"/>
          </div>
          <div>
            <button class="send d-flex btn btn-primary btn-block" style="margin-top:10px" @click="save">save</button>
          </div>
        </div>
      <!-- </div> -->
    </main>
  </div>
</div>
</template>

<script>
export default {
    name: 'Change_Profile',
    data() {
      return {
        email: "",
        password: ""
      }
    }
}
</script>

<style>

</style>
