<template>
    <div class="auth-inner">
        <form @submit.prevent="handleSubmit">
            <h3>Reset Password</h3>
            
            <!-- <div class="form-group">
                <label>token</label>
                <input v-model="token" type="text" class="form-control" placeholder="Token"/>
            </div>
            <button class="btn btn-primary btn-block" ><router-link :to="'/reset/'+token">Submit</router-link></button> -->
            <div class="form-group">
                <label>Password</label>
                <input type="password" class="form-control" v-model="password" placeholder="Password"/>
            </div>

            <div class="form-group">
                <label>Password Confirm</label>
                <input type="password" class="form-control" v-model="password_confirm" placeholder="Password Confirm"/>
            </div>

            <button class="btn btn-outline-primary" style="margin-top:10px">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Reset_token',
    data() {
        return {
            password: '',
            password_confirm: '',
        }
    },
    methods: {
        async handleSubmit() {
            try{
                const response = await axios.put('/forgot_password/new_password/' + this.$route.params.token ,{
                    password: this.password,
                    confirm_password: this.password_confirm,
                    // token: this.$route.params.token
                });

                console.log(response);
                this.$router.push('/login');
            }
            catch(e){
                this.error = e;
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
  .router-link-active{
      text-decoration: none;
      color: white;
  }
</style>
