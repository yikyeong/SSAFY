<template>
  <div>
    <div class="panel-body">
      <ul class="list-group">
        <li v-for="comment in comments" :key="comment.id" class="list-group-item">
          <div class="row">
            <div class="col-lg-1 col col-md-2">
              <img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" width="70px" height="70px" class="img-circle img-responsive" alt="" />
            </div>
            <div class="col-lg-11 col-md-10">
              <div>
                <span>{{comment.content}}</span>
                <div class="mic-info">
                      By: <span>{{comment.user.username}} | {{$moment(comment.updated_at).format("YYYY-MM-DD A hh:mm:ss")}}</span>
                </div>
              </div>
              <div class="action">                
                <button type="button" @click="deleteComment(comment.id)" class="btn btn-danger btn-sm mt-1" title="Delete">
                    삭제
                </button>
              </div>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CommentsView',
  props:{
    selectedArticle: Object,
    comments: Array,
  },
  methods:{
    readComments() {
      this.$emit("read-comments", this.selectedArticle.id)
    },
    deleteComment(commentID) {
      this.$emit("delete-comment", commentID)
    }
  },
  created() {
    this.readComments()
  },
}
</script>

<style scoped>
.mic-info { color: #666666;font-size: 12px; }
</style>