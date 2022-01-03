<template>
    <div class="auth-inner">
        <form @submit.prevent="handleSubmit">
            <error v-if="error" :error="error"/>
            <h3>Sign Up</h3>

            <div class="form-group">
                <label>Name</label>
                <input type="name" class="form-control" v-model="name" placeholder="Name"/>
            </div>

            <div class="form-group">
                <label>Email</label>
                <input type="email" class="form-control" v-model="email" placeholder="Email"/>
            </div>

            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control" v-model="password" placeholder="Password"/>
            </div>

            <div class="form-group">
                <label>Confirm Password</label>
                <input type="password" class="form-control" v-model="confirm_password" placeholder="Confirm Password"/>
            </div>

            <button class="btn btn-primary btn-block" style="margin-top:10px">Sign Up</button>
        </form>
    </div>
</template>
<script>
import axios from 'axios'
import Error from '../error.vue'
export default {
    name: 'Signup',
    components: {
        Error
    },
    data() {
        return {
            name: '',
            email: '',
            password: '',
            confirm_password: '',
            error: ''
        }
    },
    
    methods: {
        async handleSubmit(){
            try{
                await axios.post('signup', {
                    name: this.name,
                    email: this.email,
                    password: this.password,
                    confirm_password: this.confirm_password,
                });
                this.$router.push('/login');
            }catch(e){
            this.error = 'Error occurred!';
            }
        }
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
