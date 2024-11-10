<template>
  <div>
    <h1>쇼핑 애플리케이션</h1>
    <ProductList :products="products" @addCart1="addCartProduct"/>
  </div>
  <div>
    <p>총 가격: {{ totalPrice }}</p>
    <h1>장바구니</h1>
    <Cart :cartProducts="carts" @deleteItem="deleteItemEvent" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import ProductList from '@/components/ProductList.vue'
import Cart from './components/Cart.vue';

let id = 0

const products = ref([
  { id: id++, name: '사과', price: 1000 },
  { id: id++, name: '바나나', price: 1500 },
  { id: id++, name: '딸기', price: 2000 },
  { id: id++, name: '포도', price: 3000 },
  { id: id++, name: '복숭아', price: 2000 },
  { id: id++, name: '수박', price: 5000 }
])

const carts = ref([]);

const addCartProduct = (product) => {
  carts.value.push(product);
}

const deleteItemEvent = (cartProduct) => {
  const id = cartProduct.id;

  // for(const i in carts.value) {
  //   const currentId = carts.value[i].id;
  //   if(id === currentId) {
  //     carts.value.splice(i, 1);
  //     break;
  //   }
  // }

  carts.value.forEach((item, idx) => {
    const currentId = item.id;
    if(id === currentId) carts.value.splice(idx, 1);
  });
}

const totalPrice = computed(() => {
  let sumPrice = 0;
  carts.value.forEach(item => {
    sumPrice += item.price;
  })
  return sumPrice
})
</script>
