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
          <textarea v-model="info.problemDesc" class="form-control" :id="problemDescription" placeholder="" rows="10" style="resize: none;"></textarea>
        </div>
        <div class="row mb-3">
          <div class="col">
            <div class="mb-3">
              <label for="timeLimit" class="form-label">Max Time (s)</label>
              <input v-model="info.time_limit" type="text" class="form-control" id="timeLimit">
            </div>
            <select v-model="selectedLanguage" class="form-select mb-2" aria-label="language">
              <option disabled>language</option>
              <option v-for="l in languages" :key="l">{{ l }}</option>
            </select>
          </div>
          <div class="col">
            <div class="mb-3">
              <label for="memoryLimit" class="form-label">Max Memory (MB)</label>
              <input v-model="info.memory_limit" type="text" class="form-control" id="memoryLimit">
            </div>
            <select v-model="selectedDifficulty" class="form-select mb-2" aria-label="difficulty">
              <option disabled>difficulty</option>
              <option v-for="(d, index) in difficulties" :key="index">{{ d }}</option>
            </select>
          </div>
        </div>
        <button type="button" class="btn btn-warning m-2" @click="onTest">Test All Testcases</button>
        <button type="button" class="btn btn-success m-2" @click="onSumit">Sumit</button>
      </div>
      <div class="col-6">
        <v-ace-editor
          v-model:value="code"
          @init="editorInit"
          style="height: 600px;"
          id="editor"
        />
      </div>
    </div>
    <div class="row" v-for="(testcase, index) in testcases" :key="index">
      <div class="col-2 m-auto">
        <button type="button" class="btn btn-danger" @click="onDelete(index)">Delete</button>
        <button type="button" class="btn btn-success" @click="onPrint(index)">Print</button>
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
    <div class="my-2">
      <button type="button" class="btn btn-success" @click="onNewTestcase">New Testcase</button>
    </div>
  </div>
</template>

<script>
import { VAceEditor } from 'vue3-ace-editor'
import 'ace-builds/src-noconflict/theme-chrome'
// import axios from 'axios'

export default {
  name: "NewProblem",
  data() {
    return {
      info: {
        name: "",
        problemDesc: "",
        difficulty: "",
        time_limit: 1,
        memory_limit: 256,
      },
      testcases: [
        {input: "123", output: "456"},
        {input: "111", output: "222"}
      ],
      code: "",
      languages: ["c", "cpp", "python"],
      difficulties: ["easy", "medium", "hard"],
      selectedLanguage: "language",
      selectedDifficulty: "difficulty",

      error: ""
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

      const language = this.selectedLanguage
      if (language === "language") {
        this.error = "Language is not selected."
        return
      }

      const testcase = this.testcases.map( x => x.input )
      if (testcase.length < 1) {
        this.error = "You need to enter at least one testcase."
        return
      }

      let body = {
        user_id: user_id,
        language: language,
        testcase: testcase,
        code_content: this.code
      }
      console.log(body)
    },
    onDelete(index) {
      this.testcases.splice(index, 1)
    },
    onPrint(index) {
      let temp = this.testcases[index].input
      temp = JSON.stringify(temp)
      console.log(temp)
    },
    onNewTestcase() {
      this.testcases.push({})
    }
  },
  components: {
    VAceEditor
  }
}
</script>

<style>
#editor *{
  font-family : monospace !important;font-size: 20px !important;direction:ltr !important;text-align:left !important;
}
</style>
