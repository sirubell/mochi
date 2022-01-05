<template>
    <div class="footer" style="margin:10px">
      <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
        <p class="col-md-3 mb-0 text-muted">&copy; 2022 Mochi</p>

        <router-link to="/home" class="col-md-5 d-flex align-items-center justify-content-center mb-3 mb-md-0 me-md-auto link-dark text-decoration-none">
          <img src="../assets/mochi_icon.png">
        </router-link>

        <ul class="nav col-md-4 justify-content-end">
          <li class="nav-item"><router-link to="/home" class="nav-link px-2 text-muted">Home</router-link></li>
          <li class="nav-item"><a href="#" class="nav-link px-2 text-muted">Features</a></li>
          <li class="nav-item"><a href="https://sites.google.com/view/ntpuprog" class="nav-link px-2 text-muted">Website</a></li>
          <li class="nav-item"><a href="https://www.facebook.com/NTPUProgClub" class="nav-link px-2 text-muted">FB</a></li>
        </ul>
      </footer>
    </div>
</template>

<script>
export default {
    name: 'footer'
}
</script>
