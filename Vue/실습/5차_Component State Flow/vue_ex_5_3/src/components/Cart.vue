<template>
  <div v-for="cartProduct in cartProducts" :key="cartProduct.id">
    <ul>
      <li>
        {{ cartProduct.name }} - {{ cartProduct.price }}원
        <button @click="deleteCartItem(cartProduct)">삭제</button>
      </li>
    </ul>
  </div>
</template>

<script setup>
  const props = defineProps({
    cartProducts : Array
  });

  const emit = defineEmits(['deleteItem']);

  const deleteCartItem = (cartProduct) => {
    emit('deleteItem', cartProduct);
  }
</script>

<style scoped>
ul {
  margin: 0;
}
</style>