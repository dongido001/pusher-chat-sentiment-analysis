<template>
  <div id="app">
    <Login />
    <b-container>
      <NavBar :logged_user="logged_user_username" />
      <b-row class="main-area">
        <b-col cols="4" class="users">
          <Users />
        </b-col>
        <b-col cols="8" class="messages-area">
          <div class="messages-main">
            <div 
              v-if="!current_chat_channel" 
              class="select-chat text-center"
            >
              Select a user to start chatting... 
            </div>
            <Messages 
              v-else 
              :active_chat="active_chat_id" 
              :messages="messages[current_chat_channel]"
            /> 
          </div>
          <MessageInput />
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import MessageInput from "./components/MessageInput.vue";
import Messages from "./components/Messages.vue";
import NavBar from "./components/NavBar.vue";
import Login from "./components/Login.vue";
import Users from "./components/Users.vue";
import Pusher from "pusher-js";

// Declare pusher variable so it's global to this file.
let pusher;

export default {
  name: "app",
  components: {
    MessageInput,
    NavBar,
    Messages,
    Users,
    Login
  },
  data: function() {},
  methods: {}
};
</script>

<style>
.messages-main {
  overflow-y: scroll;
  height: 90%;
}
.users {
  padding: 0px !important;
  border: 1px solid gray;
}
.no-margin {
  margin: 0px;
}
.messages-area {
  border: 1px solid gray;
  padding: 0px !important;
  max-height: calc(100vh - 4em) !important;
}
.input-message {
  height: 40px;
}
.active {
  background: #17a2b8 !important;
  border: #17a2b8 !important;
}
.select-chat {
  margin-top: 35vh;
  padding: 8px;
}
.main-area {
  margin: 0px;
  min-height: calc(100vh - 5em) !important;
}
.logged_user {
  color: white;
}
</style>
