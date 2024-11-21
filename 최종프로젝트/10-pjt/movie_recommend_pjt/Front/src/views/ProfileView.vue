<template>
    <div>
        프로필
    </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useUserStore } from '@/stores/user.js'
import { RouterLink, useRouter } from 'vue-router'

const userStore = useUserStore()
const userdata = ref(null)

</script>


<style scoped>

</style>