<template>
  <div>
    <form>
      <div class="form-group">
        <label for="comment" class="text-warning font-weight-bold">Your Comment</label>
        <textarea v-model="commentData.content" id="comment" class="form-control" rows="3"></textarea>
      </div>
    </form> 
    <button @click="sendCommentData" class="btn btn-primary">등록</button>
  </div>
</template>

<script>
export default {
    name: 'CreateCommentView',
    props: {
      selectedArticle: Object,
    },
    data() {
      return {
        commentData: {
          content: null,
          article: this.selectedArticle.id,
        },
      }
    },
    methods: {
      sendCommentData() {
        this.$emit('send-commentdata', this.commentData)
      }
    },
    created() {
    }
}
</script>

<style>

</style>