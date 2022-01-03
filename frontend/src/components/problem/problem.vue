<template>
<div>
  <error v-if="error" :error="error" />
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
          <button class="btn btn-success m-2">Sumit</button>
          <button class="btn btn-success m-2" @click="test()">Test</button>
        </div>
        <div class="mb-3">
          <label for="testInput" class="form-label">Test Input</label>
          <textarea class="form-control" id="testInput" rows="3" style="resize: none;"></textarea>
        </div>
        <div class="mb-3">
          <label for="testOutput" class="form-label">Test Output</label>
          <textarea class="form-control" id="testOutput" rows="3" style="resize: none;" disabled readonly></textarea>
        </div>
      </div>
      <div class="col-lg-4 text-start" v-show="showDesc()">
        {{ info.content }}
      </div>
      <div class="col-lg-4 text-start" v-show="showSub()">{{  }}</div>
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

      error: null
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
    },
    uploadFile(evt) {
      const reader = new FileReader()
      reader.onload = (evt) => {
        this.code = evt.target.result
      }
      reader.readAsText(evt.target.files[0])
    },
    test() {
    }
  },
  components: {
    VAceEditor,
    Error
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
