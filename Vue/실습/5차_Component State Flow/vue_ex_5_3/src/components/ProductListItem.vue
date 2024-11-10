<template>
  <li>
    {{ product.name }} - {{ product.price }}원
    <button @click="addClickHandler(product)">장바구니에 추가</button>
  </li>
</template>

<script setup>


defineProps({
  product: Object
})

const emit = defineEmits(['addCart']);

const addClickHandler = (product) => {
  emit('addCart', product);
}
</script>

<style scoped>

</style>
