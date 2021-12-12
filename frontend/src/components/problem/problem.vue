<template>
  <h1>Problem is not implemented.</h1>
  <v-ace-editor
    v-model:value="content"
    @init="editorInit"
    style="height: 300px"
  />
  <p>{{ content }}</p>
</template>

<script>
import { VAceEditor } from 'vue3-ace-editor'
import 'ace-builds/src-noconflict/theme-chrome'

export default {
  name: 'Problem',
  data() {
    return {
      content: ""
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
