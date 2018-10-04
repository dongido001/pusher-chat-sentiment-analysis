<template>
    <div class="message-input">
        <b-form-input 
          v-model="message_input"
          type="text"
          placeholder="Enter your message"
          v-on:keyup.enter.native="send_message"
        >
        </b-form-input>
    </div>
</template>

<script>
export default {
  name: "MessageInput",
  data() {
    return {
      message_input: ""
    };
  },
  methods: {
    send_message() {
      this.$emit("send_message", this.message_input);
      this.message_input = "";
    }
  }
};
</script>

<style scoped>
.message-input {
  position: absolute;
  bottom: 0px;
  width: 100%;
}
</style>