<template>
  <ul>
    <ProductListItem 
      v-for="product in products" 
      :key="product.id" 
      :product="product"
      @addCart="addEmitHandler"
    />
  </ul>
</template>

<script setup>
import ProductListItem from '@/components/ProductListItem.vue'

defineProps({
  products: Array
})

const emit = defineEmits(['addCart1']);

const addEmitHandler = (product) => {
  emit('addCart1', product);
}
</script>
