<template>
  <h1>Problem is not implemented.</h1>
  <v-ace-editor
    v-model:value="content"
    @init="editorInit"
    lang="html"
    theme="chrome"
    style="height: 300px"
  />
  <p>{{ content }}</p>
</template>

<script>
import { VAceEditor } from 'vue3-ace-editor'

export default {
  name: 'Problem',
  data() {
    return {
      content: ""
    }
  },
  components: {
    VAceEditor
  }
}
</script>
