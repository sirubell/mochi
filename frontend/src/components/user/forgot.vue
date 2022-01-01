<template>
    <div class="auth-inner">
        <form @submit.prevent="forgotPassword">
            <div v-if="message" class="alert alert-success" role="alert">
                {{message}}
            </div>

            <error v-if="error" :error="error" />
            
            <h3>Forgot Password</h3>
            <div class="form-group">
                <label>Email</label>
                <input type="email" class="form-control" v-model="email" placeholder="Email"/>
            </div>

            <button type="submit" variant="info" class="btn btn-primary btn-block" style="margin-top:10px">Reset Password</button>
            <div id="result">
                <p>{{ resetText }}</p>
            </div>
        </form> 
    </div>
</template>

<script>
import axios from 'axios'
import Error from './error.vue'

export default {
    name: 'Forgot',
    components: {
        Error
    },
    data() {
        return {
            email: '',
            message: ''
        }
    },
    methods: {
        async forgotPassword(){ //利用 try catch 作錯誤偵測
            try{
                await axios.post('forgot', {
                    email: this.email
                }); // 資料由後方物件帶入 
                this.message = 'The email was sent!';
                this.error = '';
            }
            catch(e){
                this.error = 'Error occurred!';
                this.message = '';
            }
        }
    }
}
</script>