<template>
    <div>
        <h1>this is the exam all page</h1>
        <div id="nav" style="background-color:rgb(108, 159, 184)">
            <router-link to="/class/class_id/homework">Homework</router-link>|
            <router-link to="/class/class_id/exam">Exam</router-link>|
            <router-link to="/class/class_id/member">Member</router-link>
        </div>
        <div id="nav" style="background-color:rgb(108, 159, 184)">
            <router-link to="/class/class_id/exam/exam_id">Exam_id</router-link>|
            <router-link to="/class/class_id/exam/edit">Edit</router-link>|
        </div>
        <router-view/>
    </div>
</template>