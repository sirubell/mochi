<template>
    <div id="app">
        <p>題目名稱<input v-model.lazy="message" placeholder="edit me"></p>
        <p>題目敘述<input v-model.lazy="message" placeholder="edit me"></p>
        <p>題目難度<input v-model.lazy="message" placeholder="edit me"></p>
        <p>時間限制<input v-model.lazy="message" placeholder="edit me"></p>
        <p>記憶體限制<input v-model.lazy="message" placeholder="edit me"></p>
        <p>隱藏題目直到<input v-model.lazy="message" placeholder="edit me"></p>
    </div>
</template>
<style >
#app{
    font-size: 30px;
}

</style>