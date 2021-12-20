<template>
    <form @submit.prevent="handleSubmit">
        <h3>Reset Password</h3>

        <div class="form-group">
            <label>Password</label>
            <input type="password" class="form-control" v-model="password" placeholder="Password"/>
        </div>

        <div class="form-group">
            <label>Password Confirm</label>
            <input type="password" class="form-control" v-model="password_confirm" placeholder="Password Confirm"/>
        </div>

        <button class="btn btn-primary btn-block">Submit</button>
    </form>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Reset',
    data() {
        return {
            password: '',
            password_confirm: '',
        }
    },
    methods: {
        async handleSubmit() {
            const response = await axios.post('reset',{
                password: this.password,
                password_confirm: this.password_confirm,
                token: this.$route.params.token
            });

            console.log(response);
            this.$router.push('/login');
        }
    }
}
</script>