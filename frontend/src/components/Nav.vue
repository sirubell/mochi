<template>
    <nav class = "navbar navbar-expand-lg navbar-light fixed-top bd-light">
        <div class = "container">
            <a class = "navbar-brand" href = "/home"> Home </a>
            <div class = "collapse navbar-collapse" id = "navbarSupportedContent">
                <ul class = "navbar-nav me-auto mb-2 mb-lg-0">
                <li class = "nav-item">
                    <router-link class = "nav-link" to = "/problem"> Problem </router-link>
                </li>
                <li class = "nav-item">
                    <router-link class = "nav-link" to = "/course"> Course </router-link>
                </li>
                <li class = "nav-item">
                    <router-link class = "nav-link" to = "/class"> Class </router-link>
                </li>
                </ul>
                <router-link class = "nav-link" to = "/login"> Login </router-link>
                <router-link class = "nav-link" to = "/register"> Register </router-link>
                <router-link class = "nav-link" to = "/logout"> Logout </router-link>
            </div>
        </div>
    </nav>
    <div class = "container">
        <router-view />
    </div>  
</template>

<script>
    export default {
        name: 'Nav'
    }
</script>