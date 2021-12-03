<template>
    <div id="problem">
        <div id="nav" style="background-color:rgb(60, 199, 238)">
            <router-link to="/problem/problem_id/code">Code</router-link> |
            <router-link to="/problem/problem_id/submission">Submission</router-link> |
            <router-link to="/problem/problem_id/status">Status</router-link> |
            <router-link to="/problem/problem_id/solution">Solution</router-link> |
        </div>
        <router-view/>
    </div>
</template>