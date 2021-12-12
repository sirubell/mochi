<template>
  <h1>Problem is not implemented.</h1>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-2">
          <button class="btn btn-success">Sumit</button>
      </div>
      <div class="col-lg">description</div>
      <div class="col-lg-6">
        <v-ace-editor
          v-model:value="content"
          @init="editorInit"
          style="height: 600px;"
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
      content: "",
    }
  },
  methods: {
    editorInit() {
      console.log("creating ace editor")
    }
  },
  components: {
    VAceEditor
  }
}
</script>
