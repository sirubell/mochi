<template>
    <div class="alert alert-warning" role="alert">
        {{ loading }}
    </div>
</template>
<script>

export default {
    name: 'Loading',
    props: ['loading']
}
</script>
