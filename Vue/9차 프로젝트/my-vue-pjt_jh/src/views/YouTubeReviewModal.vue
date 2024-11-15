<template>
  <div class="modal" v-if="isVisible">
    <div class="modal-content">
      <button @click="closeModal">Close</button>
      <iframe
        :src="videoUrl"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
        allowfullscreen
      ></iframe>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    videoId: {
      type: String,
      required: true
    },
    isVisible: {
      type: Boolean,
      default: false
    }
  },
  computed: {
    videoUrl() {
      return `https://www.youtube.com/embed/${this.videoId}`;
    }
  },
  methods: {
    closeModal() {
      this.$emit('close');
    }
  }
};
</script>

<style scoped>
.modal {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  position: relative;
}

button {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 5px 10px;
  background-color: red;
  color: white;
  border: none;
  border-radius: 4px;
}

iframe {
  width: 600px;
  height: 400px;
}
</style>
