<template>
  <error v-if="error" :error="error" />
  <div class="fs-3">
    <h1>SubmissionID: {{ submission_id }}</h1>
    <div class="container text-start">

      <div class="mb-3">
        <label for="codeContent" class="form-label">Source Code</label>
        <textarea readonly v-model="code_content" class="form-control" id="codeContent" rows="15" style="resize: none;"></textarea>
      </div>

      <div v-if="status" class="text-center alert" :class="status === 'AC' ? 'alert-success' : 'alert-danger'" role="alert">
        Status: {{ status }}
      </div>
      <div v-if="error_hint" class="alert-warning" role="alert">
        Error Line: {{ error_line }}
        <br/>
        {{ error_hint }}
      </div>


      <div class="mb-3 row">
        <label for="userId" class="col-sm-2 col-form-label">UserID</label>
        <div class="col-sm-10">
          <input type="text" readonly class="form-control-plaintext" id="userId" :value="user_id">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="problemId" class="col-sm-2 col-form-label">ProblemID</label>
        <div class="col-sm-10">
          <input type="text" readonly class="form-control-plaintext" id="problemId" :value="problem_id">
        </div>
      </div>
      <div v-if="exam_id" class="mb-3 row">
        <label for="examId" class="col-sm-2 col-form-label">ExamID</label>
        <div class="col-sm-10">
          <input type="text" readonly class="form-control-plaintext" id="examId" :value="exam_id">
        </div>
      </div>
      <div v-if="homework_id" class="mb-3 row">
        <label for="homeworkId" class="col-sm-2 col-form-label">HomeworkID</label>
        <div class="col-sm-10">
          <input type="text" readonly class="form-control-plaintext" id="homeworkId" :value="homework_id">
        </div>
      </div>
      <div class="mb-3 row">
        <label for="uploadDate" class="col-sm-2 col-form-label">Upload Date</label>
        <div class="col-sm-10">
          <input type="text" readonly class="form-control-plaintext" id="uploadDate" :value="upload_date">
        </div>
      </div>


      <div v-if="showTimeMemory">
        <div class="mb-3 row">
          <label for="timeUsed" class="col-sm-2 col-form-label">Time Used</label>
          <div class="col-sm-10">
            <input type="text" readonly class="form-control-plaintext" id="timeUsed" :value="time_used + ' ms'">
          </div>
        </div>
        <div class="mb-3 row">
          <label for="memoryUsed" class="col-sm-2 col-form-label">Memory Used</label>
          <div class="col-sm-10">
            <input type="text" readonly class="form-control-plaintext" id="memoryUsed" :value="parseInt(memory_used / 1024) + ' MB'">
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Error from './error.vue'

export default {
  name: 'Submission',
  components: {
    Error
  },
  data() {
    return {
      code_content: "",
      error_hint: null,
      error_line: "",
      language: "",
      status: null,
      upload_date: "",

      time_used: "",
      memory_used: "",

      user_id: "",
      problem_id: "",
      submission_id: "",
      exam_id: null,
      homework_id: null,

      error: null
    }
  },
  computed: {
    showTimeMemory() {
      return this.status && (this.status === "AC" || this.status === "WA")
    }
  },
  created() {
    const user = this.$store.getters.userInfo
    if (user === null) {
      this.$router.push('/login')
      return
    }
    axios.get('/submission/' + this.$route.params.submission_id, {
      params: {
        user_id: user.user_id
      }
    })
    .then( res => {
      if (res.data.message === "you haven't solved this problem") {
        this.error = res.data.message
        return
      }
      this.code_content = res.data.code_content

      if (res.data.error_hint !== "") {
        this.error_hint = res.data.error_hint
      }
      this.error_line = res.data.error_line

      this.language = res.data.language
      this.status = res.data.status
      this.upload_date = res.data.upload_date

      this.time_used = res.data.time_used
      this.memory_used = res.data.memory_used

      this.user_id = res.data.user_id
      this.problem_id = res.data.problem_id
      this.submission_id = res.data.submission_id

      if (res.data.exam_id !== "0") {
        this.exam_id = res.data.exam_id
      }
      if (res.data.homework_id !== "0") {
        this.homework_id = res.data.homework_id
      }
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
