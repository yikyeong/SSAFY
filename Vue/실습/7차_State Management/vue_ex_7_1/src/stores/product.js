import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useProductStore = defineStore('product', () => {
  const products = ref([
    {id:1, title:"Product 1", body: "1번 상품"},
    {id:2, title:"Product 2", body: "2번 상품"},
    {id:3, title:"Product 3", body: "3번 상품"},
  ])
  

  return {
    products
  }
})
