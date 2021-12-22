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
      <div class="col-2">
        <button></button>
        <button></button>
      </div>
      <div class="col">
        <div class="form-floating">
          <textarea v-model="inputs[index]" class="form-control" placeholder="Enter your input here" :id="'input' + index" style="height: 200px; resize: none;"></textarea>
          <label :for="'input' + index">Input {{ index + 1 }}</label>
        </div>
      </div>
      <div class="col">
        <p>{{ input }}</p>
      </div>
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
    }
  },
  components: {
    VAceEditor
  }
}
</script>
