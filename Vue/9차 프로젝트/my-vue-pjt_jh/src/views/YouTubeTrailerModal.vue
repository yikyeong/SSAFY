<template>
  <div class="modal">
    <div class="modal-content">
      <button @click="$emit('close')">Close</button>
      <iframe :src="'https://www.youtube.com/embed/' + movie.trailer" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script>
export default {
  props: ['movie'],
};
</script>
