<template>
  <div class="auth-inner">
    <form @submit.prevent="handleSubmit">
        <div class="alert alert-info" role="alert">如果是第一次註冊帳號請先去信箱認證帳號！</div>
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
            <router-link to="/forgot_password">Forgot password?</router-link>
        </p>
        <p class="forgot-password text-right">
            <router-link to="/signup">Register an account?</router-link>
        </p>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
import Error from '../error.vue'

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
                await axios.post('login', {
                    email: this.email,
                    password: this.password,
                });

                axios.get('/user/myprofile')
                .then( res => {
                  this.$store.dispatch('login', res.data);
                })
                .catch (e => {
                  this.error = e
                })
                this.$router.push('/home');
            }catch (e) {
                this.error = 'Invalid username/password!'
            }
        }
    },
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
