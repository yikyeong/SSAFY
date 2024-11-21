<template>
  <div>
    <div class="row justify-content-between">
      <h1 class="ml-3 text-center text-white font-weight-bold">게시판</h1>
      <button @click="createArticle" v-if="nowUser" class="btn btn-primary mt-2 mb-2 mr-3">글쓰기</button>
    </div>
    <table class="table">
      <thead>
        <tr>
          <th scope="col" class="text-white font-weight-bold">#</th>
          <th scope="col" class="text-white font-weight-bold">제목</th>
          <th scope="col" class="text-white font-weight-bold">작성자</th>
        </tr>
      </thead>
      <tbody v-for="article in articles" :key="article.id">
        <tr>
          <th scope="row" class="text-white">{{ article.id }}</th>
          <td class="cursor" @click="readArticle(article.id)">{{ article.title }}</td>
          <td class="text-white">{{ article.user.username }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "ArticlesView",
  props: {
    articles: Array,
    nowUser: String,
  },
  methods: {
    readArticles() {
      this.$emit("read-articles");
    },
    createArticle() {
      if (this.$cookies.isKey("auth-token")) {
        this.$router.push({ name: "CreateArticle" });
      } else {
        this.$router.push({ name: "Login" });
      }
    },
    readArticle(articleID) {
      this.$emit("read-article", articleID)
      this.$router.push({name: 'ArticleView', params: { id: articleID }})
    }
  },
  created() {
    this.readArticles();
  }
};
</script>

<style>
.cursor{
  cursor: pointer;
  color: white;
}
.cursor:hover{
  text-decoration: underline;
  color: paleturquoise;
}

</style>