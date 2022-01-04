<template>
    <div class="alert alert-info" role="alert">
        {{ info }}
    </div>
</template>
<script>

export default {
    name: 'Info',
    props: ['info']
}
</script>
