<template>
  <ul>
    <li v-for="(product, i) in products1" :key="product.id">
      {{ (i+1) + '. ' + product.name}} - {{ product.price }}원<br>
    </li>
  </ul>
  {{ c }}
</template>

<script setup>
const props = defineProps({
  products1 : Array,
  c : String
})

console.log(props.products)
</script>

<style scoped>

</style>