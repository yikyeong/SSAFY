<template>
  <div>
    <h2>Product List</h2>
    <ul>
      <ProductListItem v-for="product in store.products" :key="product.id" :product="product"/>
    </ul>
  </div>
</template>

<script setup>
import { useProductStore } from '@/stores/product'
// ProductListItem 컴포넌트는 ProductList 컴포넌트의 하위 컴포넌트이다.
import ProductListItem from "@/components/ProductListItem.vue"

const store = useProductStore()
</script>
