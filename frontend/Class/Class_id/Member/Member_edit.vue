<template>
    <div>
        <h1>this is the member edit page</h1>
        <div id="nav" style="background-color:rgb(108, 159, 184)">
            <router-link to="/class/class_id/homework">Homework</router-link>|
            <router-link to="/class/class_id/exam">Exam</router-link>|
            <router-link to="/class/class_id/member">Member</router-link>
        </div>
        <router-view/>
    </div>
</template>