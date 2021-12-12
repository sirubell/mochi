<template>
  <h1>Problem All is not implemented</h1>
  <div v-if="problemTable">
    {{ problemTable.page }}
  </div>
  <div v-if="error">
    {{ error }}
  </div>
</template>

<script>
export default {
  name: 'ProblemAll',
  data() {
    return {
      page: 1,
      topic: ['bs', 'arr'],
      problemTable: null,
      error: null
    }
  },
  mounted() {
    const axios = require('axios');
    const url = process.env.VUE_APP_AXIOS_BASEURL + "/problem"

    axios.get(url, {
      timeout: 5000,
      params: {
        page: this.page,
        topic: JSON.stringify(this.topic)
      }
    })
    .then( (response) => {
      this.problemTalbe = response.data
    })
    .catch( error => {
      this.error = error
    });
  }
}
</script>
