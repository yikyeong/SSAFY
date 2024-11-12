<template>
  <li>
    {{ product.id }} - {{ product.title }} - {{ product.body }}
    <!-- 삭제 버튼을 클릭하면 선택된 상품의 id를 전달하며 함수 'deleteProduct'를 호출한다. -->
    <button @click="deleteProduct(product.id)">Delete</button>
  </li>
</template>

<script setup>
import { useProductStore } from "@/stores/product"

// ProductList 컴포넌트로부터 개별 상품 객체를 prop 데이터로 전달받는다.
defineProps({
  product: Object
})

// 함수 'deleteProduct'는 store의 'deleteProduct' action를 호출한다.
const store = useProductStore()

const deleteProduct = function(id) {
  store.deleteProduct(id)
}

</script>

<style scoped></style>
