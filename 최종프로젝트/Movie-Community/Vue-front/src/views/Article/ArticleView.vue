<template>
  <div v-if="selectedArticle&&selectedMovie">
    <h1 class="my-4 text-white">{{selectedArticle.title}}</h1>
    <hr class="bg-info">
    <!-- Portfolio Item Row -->
    <div class="row mb-3">
      <div class="col-md-4 col-sm-12">
        <img class="img-fluid" :src="selectedMovie.poster" alt="movie-poster" />
      </div>

      <div class="col-md-8">
        <h2 class="text-white font-weight-bold mb-3">{{selectedMovie.title}}</h2>

        <div class="text-white ml-3 mb-3">{{selectedMovie.overview}}</div>


        <ul>
          <li class="text-white mb-3">영화 개봉일 : {{selectedMovie.release_date}}</li>
          <li class="text-white mb-3">작성자 : {{selectedArticle.user.username}}</li>
          <li class="text-white mb-3">글 작성자의 평점 : {{selectedArticle.rank}} / 5</li>
          <li class="text-white mb-3">작성시간 : {{createdArticleDate}} | 최종수정시간 : {{updatedArticleDate}}</li>
        </ul>
      </div>
    </div>
    <div class="text-white mb-5 mt-5">{{selectedArticle.content}}</div>

    <button class="btn btn-danger" @click="deleteArticle">삭제</button>
    <hr />
    <div v-if="nowUser">
      <CreateCommentView @send-commentdata="sendCommentData" :selectedArticle="selectedArticle" />
      <hr />
    </div>
    <CommentsView
      class="mb-3"
      @read-comments="readComments"
      @delete-comment="deleteComment"
      :selectedArticle="selectedArticle"
      :comments="comments"
    />
  </div>
</template>

<script>
import CreateCommentView from "../../components/CreateCommentView.vue";
import CommentsView from "../../components/CommentsView.vue";
export default {
  name: "ArticleView",
  props: {
    selectedArticle: Object,
    comments: Array,
    selectedMovie: Object,
    nowUser: String
  },
  components: {
    CreateCommentView,
    CommentsView
  },
  methods: {
    readArticle() {
      this.$emit("read-article", this.$route.params.id);
    },
    readComments(articleID) {
      this.$emit("read-comments", articleID);
    },
    sendCommentData(commentData) {
      this.$emit("send-commentdata", commentData);
      this.readComments(this.selectedArticle.id);
    },
    deleteArticle() {
      this.$emit("delete-article", this.$route.params.id)
    },
    deleteComment(commentID) {
      this.$emit("delete-comment", {
        "articleID": this.$route.params.id,
        "commentID": commentID,
      })
    }
  },
  computed: {
    createdArticleDate() {
      return this.$moment(this.selectedArticle.created_at).format(
        "YYYY-MM-DD A hh:mm:ss"
      );
    },
    updatedArticleDate() {
      return this.$moment(this.selectedArticle.updated_at).format(
        "YYYY-MM-DD A hh:mm:ss"
      );
    }
  },
  created() {
    this.readArticle();
  }
};
</script>

<style>
</style>