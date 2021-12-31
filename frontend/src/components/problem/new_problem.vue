<template>
  <h1>New Problem is not implemented.</h1>
  <div class="container">
    <div class="row">
      <div class="col-6">
      </div>
      <div class="col-6">
        <v-ace-editor
          v-model:value="code"
          @init="editorInit"
          style="height: 600px;"
        />
      </div>
    </div>
    <div class="row" v-for="(input, index) in inputs" :key="index">
      <div class="col-2 m-auto">
        <button type="button" class="btn btn-warning" @click="onTest(index)">Test</button>
        <button type="button" class="btn btn-danger" @click="onDelete(index)">Delete</button>
      </div>
      <div class="col">
        <div class="mb-3 text-start">
          <label for="'input' + index" class="form-label">Input {{ index + 1 }}</label>
          <textarea v-model="inputs[index]" class="form-control" :id="'input' + index" placeholder="" rows="3" style="resize: none;"></textarea>
        </div>
      </div>
      <div class="col">
        <div class="mb-3 text-start">
          <label for="'output' + index" class="form-label">Output {{ index + 1 }}</label>
          <textarea v-model="inputs[index]" class="form-control " :id="'output' + index" placeholder="" rows="3" style="resize: none;" readonly></textarea>
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

export default {
  name: "NewProblem",
  data() {
    return {
      info: {
        name: "",
        difficulty: "",
        time: 1000,
        memory: 256,

      },
      code: "",
      inputs: [
        "123",
        "456"
      ],
      avil_topic: ["binary search", "array"]
    }
  },
  methods: {
    editorInit() {
      // do nothing
    },
    onTest(index) {
      console.log("test " + index)
    },
    onDelete(index) {
      this.inputs.splice(index, 1)
    },
    onNewTestcase() {
      this.inputs.push("")
    }
  },
  components: {
    VAceEditor
  }
}
</script>
