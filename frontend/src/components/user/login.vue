<template>
  <div class="auth-inner">
    <form @submit.prevent="handleSubmit">
        <error v-if="error" :error="error"/>
        <h3>Login</h3>
        <div class="form-group">
            <label>Email</label>
            <input type="email" class="form-control" v-model="email" placeholder="Email"/>
        </div>

        <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" v-model="password" placeholder="Password"/>
        </div>

        <button class="btn btn-primary btn-block" style="margin-top:10px">Login</button>

        <p class="forgot-password text-right">
            <router-link to="/forgot">Forgot password?</router-link>
        </p>
        <p class="forgot-password text-right">
            <router-link to="/signup">Register an account?</router-link>
        </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import Error from './error.vue'
import { mapGetters } from 'vuex'

export default {
    name: 'Login',
    components: {
        Error
    },
    data(){
        return{
            email: '',
            password: '',
            error: ''
        }
    },
    methods: {
        async handleSubmit(){
            try{
                const response = await axios.post('login', {
                    email: this.email,
                    password: this.password,
                });

                localStorage.setItem('token', response.data.token);
                this.$store.dispatch('login', response.data.userId);
                this.$router.push('/home');
            }catch (e) {
                this.error = 'Invalid username/password!'
            }
        }
    },
    computed: {
      ...mapGetters([
        'userId'
      ])
    }
}
</script>

<style>
  .auth-inner {
    position: relative;
    /* top: 10%; */
    width: 450px;
    margin: auto;
    background: #ffffff;
    box-shadow: 0px 14px 80px rgba(34, 35, 58, 0.2);
    padding: 40px 35px 45px 55px;
    border-radius: 15px;
    transition: all .3s;
  }
</style>
