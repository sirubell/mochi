<template>
<div>
  <h1>{{ info.name }}</h1>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-2">
        <div class="row mb-3">
          <div class="col">
            <div class="mb-3">
              <label for="timeLimit" class="form-label">Time Limit</label>
              <input :value="info.time_limit + 's'" type="text" class="form-control" id="timeLimit" disabled readonly>
            </div>
            <div class="mb-3">
              <label for="memoryLimit" class="form-label">Memory Limit</label>
              <input :value="info.memory_limit + 'MB'" type="text" class="form-control" id="memoryLimit" disabled readonly>
            </div>
            <select v-model="selectedLanguage" class="form-select" aria-label="language">
              <option disabled>language</option>
              <option v-for="l in languages" :key="l">{{ l }}</option>
            </select>
          </div>
          <div class="col">
            <div class="mb-2">
              <label for="uploadCode" class="form-label">Upload Code</label>
              <input class="form-control" type="file" id="uploadCode" accept=".c,.cpp,.py" @change="uploadFile">
            </div>
            <span class="mb-2">Difficulty: {{ info.difficulty }}</span>
            <button type="button" @click="onClickDescBtn" class="btn my-2" :class="showDesc() ? 'btn-primary' : 'btn-outline-primary'">Desciption</button>
            <button type="button" @click="onClickSubBtn" class="btn my-2" :class="showSub() ? 'btn-secondary' : 'btn-outline-secondary'">Submission</button>
          </div>
        </div>
        <div class="mb-3">
          <button class="btn btn-success m-2" @click=onSubmit()>Submit</button>
          <button class="btn btn-success m-2" @click="onTest()">Test</button>
        </div>
        <div class="mb-3">
          <label for="testInput" class="form-label">Test Input</label>
          <textarea v-model="test_case.input" class="form-control" id="testInput" rows="3" style="resize: none;"></textarea>
        </div>
        <div class="mb-3">
          <label for="testOutput" class="form-label">Test Output</label>
          <textarea v-model="test_case.output" class="form-control" id="testOutput" rows="3" style="resize: none;" disabled readonly></textarea>
        </div>
        <error v-if="error" :error="error" />
        <loading v-if="loading" loading="Running" />
        <info v-if="return_status" :info="'Testcase status: ' + return_status" />
        <info v-if="expectOutput" :info="'Expect Output: ' + expectOutput" />
      </div>
      <div class="col-lg-4 text-start border border-3" style="white-space: pre-line;" v-show="showDesc()">
        {{ info.content }}
      </div>
      <div class="col-lg-4 text-start border border-3" v-show="showSub()">
      <table class="table">
        <thead>
          <tr>
            <th scope="col">SubmissionID</th>
            <th scope="col">Status</th>
            <th scope="col">Language</th>
            <th scope="col">Submit Time</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="sub in submissions" :key="sub.time">
            <th scope="row">
              <router-link :to="'/submission/' + sub.submission_id">{{ sub.submission_id }}</router-link>
            </th>
            <td>{{ sub.status }}</td>
            <td>{{ sub.language }}</td>
            <td>{{ sub.time }}</td>
          </tr>
        </tbody>
      </table>
      </div>
      <div class="col-lg">
        <v-ace-editor
          v-model:value="code"
          @init="editorInit"
          :lang="aceLanguage"
          theme="monokai"
          style="height: 800px;"
          id="editor"
        />
      </div>
    </div>
  </div>
</div>
</template>

<script>
import { VAceEditor } from 'vue3-ace-editor'
import 'ace-builds/src-noconflict/mode-text'
import 'ace-builds/src-noconflict/mode-c_cpp'
import 'ace-builds/src-noconflict/mode-python'
import 'ace-builds/src-noconflict/theme-monokai.js'
// import 'ace-builds/src-noconflict/theme-chrome.js'
import axios from 'axios'
import Error from '../error.vue'
import Loading from '../loading.vue'
import Info from '../info.vue'

export default {
  name: 'Problem',
  data() {
    return {
      selectedLanguage: "language",
      // when add new language to this array
      // you need to update the mode and the
      // language config(aceLanguage()) for ace editor
      languages: ["c", "c++", "python"],
      panel: "description",
      source_id: null,
      test_case: { input: "", output: ""},
      submissions: [],

      code: "",

      info: {
        id: "",
        name: "",
        questioner_id: "",
        difficulty: "",
        content: "",
        time_limit: "",
        memory_limit: "",
        sample_input: "",
        sample_ouput: "",
      },

      error: null,
      loading: false,
      return_status: null,
      expectOutput: null
    }
  },
  computed: {
    aceLanguage() {
      if (this.selectedLanguage === "language") return "text"
      if (this.selectedLanguage === "c" || this.selectedLanguage === "c++") return "c_cpp"
      return this.selectedLanguage
    }
  },
  methods: {
    editorInit() {
      // do nothing
    },
    showDesc() {
      return this.panel === "description"
    },
    showSub() {
      return this.panel === "submission"
    },
    onClickDescBtn() {
      this.panel = "description"
    },
    onClickSubBtn() {
      this.panel = "submission"
      this.load_all_submissions()
    },
    uploadFile(evt) {
      const reader = new FileReader()
      reader.onload = (evt) => {
        this.code = evt.target.result
      }
      reader.readAsText(evt.target.files[0])
    },
    onTest() {
      this.error = null
      this.return_status = null
      this.expectOutput = null

      if (this.$store.getters.userInfo === null) {
        this.$router.push("/login")
        return
      }

      if (this.selectedLanguage === "language") {
        this.error = "Please select a language."
        return
      }

      if (this.loading === true) {
        this.error = "Testcase is still running."
        return
      }
      this.loading = true
      

      const payload = {
        user_id: this.$store.getters.userInfo.user_id,
        problem_id: this.info.id,
        language: this.selectedLanguage,
        code_content: this.code,
        test_case: this.test_case.input
      }

      axios.post('/problem/test_run', payload)
      .then( res => {
        this.source_id = res.data.source_id
      })
      .catch( error => this.error = error)

      this.loading = true

      const get_test_interval = setInterval( () => {
        axios.get('/problem/test_run', {
          params: {
            source_id: this.source_id,
            user_id: this.$store.getters.userInfo.user_id
          }
        })
        .then( res => {
          const message = res.data.message
          if (message === "pending") {
            return
          }

          clearInterval(get_test_interval)
          this.loading = false

          this.return_status = res.data.status
          this.expectOutput = res.data.correct_ans_output
          this.test_case.output = res.data.output
          if (message !== "OK") this.error = message

          console.log(res.data)
        })
        .catch( error => {
          clearInterval(get_test_interval)
          this.error = error
          this.loading = false
        })
      }, 1000)
    },
    onSubmit() {
      if (this.$store.getters.userInfo === null) {
        this.router.push('/login')
        return
      }
      if (this.selectedLanguage === "language") {
        this.error = "Please select a language"
        return
      }

      if (this.loading === true) {
        this.error = "Task is still running."
        return
      }

      this.error = null
      this.loading = true
      this.return_status = null
      this.expectOutput = null
      this.onClickSubBtn()

      const payload = {
        user_id: this.$store.getters.userInfo.user_id,
        problem_id: this.info.id,
        language: this.selectedLanguage,
        code_content: this.code
      }

      axios.post('/submission/new', payload)
      .then( res => {
        this.source_id = res.data.source_id
        
        const get_submission_interval = setInterval( () => {
          axios.get('/submission/new', {
            params: {
              source_id: this.source_id
            }
          })
          .then( res => {
            const message = res.data.message
            if (message === "not ok") {
              return
            }

            this.loading = false

            clearInterval(get_submission_interval)
            if (message !== "ok") {
              this.error = message
            } else {
              this.get_new_submission(res.data.submission_id)
            }
          })
          .catch( error => {
            clearInterval(get_submission_interval)
            this.error = error
            this.loading = false
          })
        }, 1000)
      })
      .catch( error => this.error = error)
    },
    get_new_submission(submission_id) {
      axios.get('/submission/' + submission_id)
      .then( res => {
        this.submissions.unshift({
          submission_id: res.data.submission_id,
          language: res.data.language,
          status: res.data.status,
          time: res.data.upload_date
        })
      })
      .catch( error => this.error = error)
    },
    load_all_submissions() {
      const user_id = this.$store.getters.userInfo.user_id
      axios.get('/status', {
        params: {
          page: 1,
          user_id: user_id,
          problem_id: this.info.id
        }
      })
      .then( res => {
        this.submissions = res.data.returnset.map( x => { 
          return {
            submission_id: x.submission_id,
            language: x.language,
            status: x.status,
            time: x.upload_date
          }
        })
      })
      .catch( error => this.error = error )
    }
  },
  components: {
    VAceEditor,
    Error,
    Loading,
    Info
  },
  created() {
    this.info.id = this.$route.params.problemId
    axios.get('/problem/' + this.info.id)
    .then( res => {
      if (res.data.code === 404) {
        this.error = res.data.message
      } else {
        this.info.id = res.data.problem_id
        this.info.name = res.data.name
        this.info.questioner_id = res.data.questioner_id
        this.info.difficulty = res.data.difficulty
        this.info.content = res.data.content
        this.info.time_limit = res.data.time_limit
        this.info.memory_limit = res.data.memory_limit
        this.info.sample_input = res.data.sample_input
        this.info.sample_output = res.data.sample_output

        this.test_case.input = this.info.sample_input
        this.test_case.output = this.info.sample_output
      }
    })
    .catch( e => { this.error = e})
  }
}
</script>

<style>
#editor *{
  font-family : monospace !important;font-size: 20px !important;direction:ltr !important;text-align:left !important;
}
</style>
