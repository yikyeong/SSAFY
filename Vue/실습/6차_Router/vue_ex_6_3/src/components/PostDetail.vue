<template>
  <div>
    <p>번호 : {{ post.id }}</p>
    <p>제목 : {{ post.title }}</p>
    <p>내용 : {{ post.content }}</p>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import { useRoute } from 'vue-router';

// 게시글 목록
const posts = ref([
    {id : 1, title : "Post 1", content : "Content 1"},
    {id : 2, title : "Post 2", content : "Content 2"},
    {id : 3, title : "Post 3", content : "Content 3"},
])

const route = useRoute()
// params에서 id는 알고 있다. 위에 있는것중에 id 일치하는거 하나 찾아서 보여주기
const id = ref(route.params.id)
</script>

<style scoped>

</style>