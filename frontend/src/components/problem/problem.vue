<template>
  <h1>Problem is not implemented.</h1>
  <div class="container-fluid">
    <div class="row">
      <div class="col-lg-2">
          <button class="btn btn-success m-2">Sumit</button>
          <button class="btn btn-success m-2" @click="toggleDesc()">toggle description</button>
      </div>
      <div class="col-lg-4 text-start" v-show="showDesc">description</div>
      <div class="col-lg">
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
      showDesc: true
    }
  },
  methods: {
    editorInit() {
      console.log("creating ace editor")
    },
    toggleDesc() {
      this.showDesc = !this.showDesc
    }

  },
  components: {
    VAceEditor
  }
}
</script>
