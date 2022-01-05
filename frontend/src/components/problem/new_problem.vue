<template>
  <div class="container">
    <div class="row">
      <div class="col-6 test-start">
        <div class="mb-3">
          <label for="problemName" class="form-label">Problem Name</label>
          <input v-model="info.name" type="text" class="form-control" id="problemName">
        </div>
        <div class="mb-3">
          <label for="problemDescription" class="form-label">Problem Description</label>
          <textarea v-model="info.problemDesc" class="form-control" id="problemDescription" placeholder="" rows="10" style="resize: none;"></textarea>
        </div>
        <div class="row mb-3">
          <div class="col">
            <div class="mb-3">
              <label for="timeLimit" class="form-label">Max Time (s)</label>
              <input v-model="info.time_limit" type="text" class="form-control" id="timeLimit">
            </div>
            <select v-model="info.language" class="form-select mb-2" aria-label="language">
              <option disabled>language</option>
              <option v-for="l in languages" :key="l">{{ l }}</option>
            </select>
          </div>
          <div class="col">
            <div class="mb-3">
              <label for="memoryLimit" class="form-label">Max Memory (MB)</label>
              <input v-model="info.memory_limit" type="text" class="form-control" id="memoryLimit">
            </div>
            <select v-model="info.difficulty" class="form-select mb-2" aria-label="difficulty">
              <option disabled>difficulty</option>
              <option v-for="(d, index) in difficulties" :key="index">{{ d }}</option>
            </select>
          </div>
        </div>
      </div>
      <div class="col-6">
        <v-ace-editor
          v-model:value="info.code"
          @init="editorInit"
          style="height: 600px;"
          id="editor"
        />
      </div>
    </div>
    <div class="row" v-for="(testcase, index) in testcases" :key="index">
      <div class="col-2 m-auto">
        <button type="button" class="btn btn-danger" @click="onDelete(index)">Delete</button>
      </div>
      <div class="col">
        <div class="mb-3 text-start">
          <label for="'input' + index" class="form-label">Input {{ index + 1 }}</label>
          <textarea v-model="testcases[index].input" class="form-control" :id="'input' + index" placeholder="" rows="3" style="resize: none;"></textarea>
        </div>
      </div>
      <div class="col">
        <div class="mb-3 text-start">
          <label for="'output' + index" class="form-label">Output {{ index + 1 }}</label>
          <textarea v-model="testcases[index].output" class="form-control " :id="'output' + index" placeholder="" rows="3" style="resize: none;" readonly></textarea>
        </div>
      </div>
    </div>
    <div>
      <error v-if="error" :error="error"/>
      <loading v-if="loading" :loading="'Testcases is running'"/>
      <Info v-if="return_status" :info="return_status"/>
    </div>
    <div class="my-2">
      <button type="button" class="btn btn-primary m-2" @click="onNewTestcase">New Testcase</button>
      <button type="button" class="btn btn-warning m-2" @click="onTest">Test All Testcases</button>
      <button type="button" class="btn btn-success m-2" @click="onSumit">Submit</button>
    </div>
  </div>
</template>

<script>
import { VAceEditor } from 'vue3-ace-editor'
import 'ace-builds/src-noconflict/theme-chrome'
import axios from 'axios'
import Error from '../error.vue'
import Loading from '../loading.vue'
import Info from '../info.vue'

export default {
  name: "NewProblem",
  data() {
    return {
      info: {
        name: "",
        problemDesc: "",
        language: "language",
        difficulty: "difficulty",
        time_limit: 1,
        memory_limit: 256,
        code: ""
      },
      testcases: [],
      languages: ["c", "c++", "python"],
      difficulties: ["easy", "medium", "hard"],

      source_id: null,

      error: null,
      loading: null,
      return_status: null
    }
  },
  methods: {
    editorInit() {
      // do nothing
    },
    onTest() {
      const user_id = this.$store.getters.userId
      if (user_id === null) {
        this.error = "You need to login to create a new problem."
        return
      }

      const language = this.info.language
      if (language === "language") {
        this.error = "Language is not selected."
        return
      }

      const test_case = this.testcases.map( x => x.input );
      if (test_case.length < 1) {
        this.error = "You need to enter at least one testcase."
        return
      }

      this.error = null
      this.return_status = null

      let postData = {
        user_id: user_id,
        language: language,
        test_case: test_case,
        code_content: this.info.code,
        time_limit: this.info.time_limit,
        memory_limit: this.info.memory_limit
      }

      axios.post('/problem/new/test_run', postData)
      .then( res => {
        if (res.data.code === 500) {
          this.error = res.data.message
          return
        }
        
        this.source_id = res.data.source_id
        this.loading = true

        let get_testcase_interval = setInterval( () => {
          axios.get('problem/new/test_run', {
            params: {
              source_id: this.source_id,
              user_id: user_id
            }
          })
          .then( (res) => {
            const message = res.data.message
            if (message === "pending") {
              return
            }

            clearInterval(get_testcase_interval)
            this.loading = false

            if (message === "Error, source_id is required" || message === "Error, user_id is required" || message === "source_id is not found") {
              this.error = message
              return
            }


            this.return_status = res.data.status
            if (this.return_status === "AC") {
              for (let i = 0; i < this.testcases.length; i++) {
                this.testcases[i].output = res.data.return_set[i]
              }
            } else {
              this.error = message
            }
          })
        }, 1000)
      })
      .catch( error => {
        this.error = error
      })

    },
    onSumit() {
      if (this.loading !== false || this.source_id === null) {
        this.error = "You need to run testcases and wait until it is finished."
        return
      }

      const postData = {
        questioner_id: this.$store.getters.userId,
        source_id: this.source_id,
        name: this.info.name,
        difficulty: this.info.difficulty,
        content: this.info.problemDesc,
        time_limit: this.info.time_limit,
        memory_limit: this.info.memory_limit,
        is_hidden: 0
      }

      axios.post('/problem', postData)
      .then( res => {
        const code = res.data.code
        
        if (code === 200) {
          this.return_status = res.data.message
        } else {
          this.error = res.data.message
        }
      })

    },
    onDelete(index) {
      this.testcases.splice(index, 1)
    },
    onNewTestcase() {
      this.testcases.push({ input: "", output: ""})
    }
  },
  components: {
    VAceEditor,
    Error,
    Loading,
    Info
  }
}
</script>

<style>
#editor *{
  font-family : monospace !important;font-size: 20px !important;direction:ltr !important;text-align:left !important;
}
</style>
