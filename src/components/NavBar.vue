<template>
    <b-navbar toggleable="md" type="dark" variant="info" class="nav-bar">
        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
        <b-navbar-brand href="#">ChitChat</b-navbar-brand>
        <b-collapse is-nav id="nav_collapse">
            <b-navbar-nav class="ml-auto logged_user" >
                Welcome back {{logged_user}}
            </b-navbar-nav>
        </b-collapse>
    </b-navbar>
</template>

<script>
export default {
  name: "NavBar",
  props: {
    logged_user: String
  }
};
</script>

<style scoped>
.nav-bar {
  border-bottom: 1px solid #17a2b8;
}
</style>