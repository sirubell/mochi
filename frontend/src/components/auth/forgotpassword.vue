<template>
    <div class="container m-5">
        <form @submit.prevent="forgetpassword">
            <h3>忘記密碼</h3>

            <div class="form-group">
                <label>信箱</label>
                <input type="email" class="form-control form-control-lg" v-model="user.email" />
            </div>

            <button type="submit" class="btn btn-dark btn-lg btn-block">重新設定密碼</button>
        </form>
    </div>
</template>

<script>
import { firebaseAuth } from "@firebase/auth";

export default {
  data() {
    return {
      user: {   
        email: ''
      }
    };
  },
  methods: {
    forgetpassword() {
        firebaseAuth
        .sendPasswordResetEmail(this.user.email)
        .then(() => {
            alert('請查看您的信箱以重設密碼')
            this.user = {   
              email: ''
            }
        }).catch((error) => {
          alert(error)
        })
    }
  }
};
</script>
