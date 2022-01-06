<template>
    <div class="auth-inner">
        <form @submit.prevent="handleSubmit">
            <error v-if="error" :error="error"/>

            <h3>Reset Password</h3>
            
            <div class="form-group">
                <label>token</label>
                <input v-model="token" type="text" class="form-control" placeholder="Token"/>
            </div>
            <!-- <button class="btn btn-primary btn-block" style="margin-top:10px">Submit</button> -->
            <!-- <router-link :to="'/reset/'+token">Submit</router-link> -->
            <button @click="handleSubmit" class="btn btn-primary btn-block" style="margin-top:10px">Submit</button>
        </form>
    </div>
</template>

<script>
import axios from 'axios'
import Error from '../error.vue'
export default {
    name: 'Reset',
    components: {
        Error
    },
    data() {
        return {
            token: '',
            error: null
        }
    },
    methods: {
        // async handleSubmit() {
        //     try{
        //         await axios.post('/forgot_password/confirm_token',{
        //             token: this.token,
        //             // token: this.$route.params.token
        //         });
        //         axios.get('/forgot_password/confirm_token')
        //         .then( res => {
        //             this.$store.dispatch('reset', res.data);
        //         })
        //         .catch(e => {
        //             this.error = e
        //         })
        //         // console.log(response);
        //         console.log(this.token);
        //         this.$router.push('/reset_token');
        //     }
        //     catch(e){
        //         this.error = 'Invalid token';
        //     }
        // }
        handleSubmit() {
        axios.post('/forgot_password/confirm_token',{
          token: this.token,
          // token: this.$route.params.token
        })
        // axios.get('/forgot_password/new_password/<token>')
        .then( () => {
          this.$router.push('/reset/' + this.token);
        })
        .catch( () => { this.error = 'Error:Wrong token'})
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