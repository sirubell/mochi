<template>
  <br/><br/>
  <div class="d-flex flex-row mb-6">
    <div class = "col-1">
      <button>Practice</button>
    </div>
    <div class = "col-1">
      <button>CPE</button>
    </div>
    <div class = "col-1">
      <button>Test</button>
    </div>
  </div>
  <div class="d-flex flex-row-reverse">
    <div class = "col-1">
      <button>新增題目</button>
    </div>
    <form class = "d-flex">
      <input
        class = "form-control me-2"
        type = "search"
        placeholder = "Search"
        aria-label = "Search"
      />
      <button class = "btn btn-outline-success" type = "submit"> Search </button>
    </form>
  </div>
  <h1 class = "display-1 text-bold"> Problem </h1>
  <h1 class = "text-gray-soft text-regular"> Problem page </h1>
</template>

<script>
export default {
};
</script>

<style>

</style>