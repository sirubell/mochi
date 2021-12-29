<template>
  <h1>Problem is not implemented.</h1>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-2">
        <div class="row mb-3">
          <div class="col">
            <div class="mb-3">
              <label for="maxTime" class="form-label">Max Time</label>
              <input type="text" class="form-control" id="maxTime" disabled readonly>
            </div>
            <div class="mb-3">
              <label for="maxMem" class="form-label">Max Memory</label>
              <input type="text" class="form-control" id="maxMem" disabled readonly>
            </div>
            <select v-model="selectedLanguage" class="form-select" aria-label="language">
              <option disabled>language</option>
              <option v-for="l in languages" :key="l">{{ l }}</option>
            </select>
          </div>
          <div class="col">
            <button type="button" @click="onClickDescBtn" class="btn my-3" :class="showDesc() ? 'btn-primary' : 'btn-outline-primary'">Desciption</button>
            <button type="button" @click="onClickInfoBtn" class="btn my-3" :class="showInfo() ? 'btn-secondary' : 'btn-outline-secondary'">Info</button>
            <div>
              <label for="uploadCode" class="form-label">Upload Code</label>
              <input class="form-control" type="file" id="uploadCode" @change="uploadFile">
            </div>
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
      <div class="col-lg-4 text-start" v-show="showDesc()">{{ description }}</div>
      <div class="col-lg-4 text-start" v-show="showInfo()">{{ info }}</div>
      <div class="col-lg">
        <v-ace-editor
          v-model:value="code"
          @init="editorInit"
          style="height: 800px;"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { VAceEditor } from 'vue3-ace-editor'
import 'ace-builds/src-noconflict/theme-chrome'

export default {
  name: 'Problem',
  data() {
    return {
      selectedLanguage: "language",
      languages: ["c", "cpp", "python"],
      panel: "description",
      description: "temp desc",
      info: "temp info",
      code: ""
    }
  },
  methods: {
    editorInit() {
      console.log("creating ace editor")
    },
    showDesc() {
      return this.panel === "description"
    },
    showInfo() {
      return this.panel === "info"
    },
    onClickDescBtn() {
      this.panel = "description"
    },
    onClickInfoBtn() {
      this.panel = "info"
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
    VAceEditor
  }
}
</script>
