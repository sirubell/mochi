<template>
    <div class="auth-inner">
        <form @submit.prevent="handleSubmit">
            <h3>Reset Password</h3>
            
            <div class="form-group">
                <label>token</label>
                <input v-model="token" type="text" class="form-control" placeholder="Token"/>
            </div>
            <button @click="handleSubmit" class="btn btn-primary btn-block" style="margin-top:10px">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Reset',
    data() {
        return {
            token: '',
            error: null
        }
    },
    methods: {
      handleSubmit() {
        axios.post('/forgot_password/confirm_token',{
          token: this.token,
          // token: this.$route.params.token
        })
        .then( () => {
          this.$router.push('/reset/' + this.token);
        })
        .catch( error => { this.error = error})
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
  a{
      text-decoration: none;
      color: white;
  }
</style>
