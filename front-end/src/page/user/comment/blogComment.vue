<template>
  <div class="comment">
        <template v-if="loading">
            <Loading :loading="loading"/>
        </template>
        <template v-else>
            <div
                v-if="musicCommentData.length >= 0"
                class="block"
            >
                <p
                    ref="commentTitle"
                    class="title"
                >
                    最新评论
                    <span class="count">({{ commentsSumNumber }})</span>
                </p>
                <div v-if="comment" class="comment">
        <div :class="{ border }" class="content">
            <p class="comment-text">
                <span class="username">{{ comment.author }}:</span>
                <span class="text">{{ comment.comment }}</span>
            </p>
            <div class="bottom">
                <span class="date">{{ $utils.formatDate(comment.publish_time) }}</span>
                <div class="actions" @click="addLikeAccount">
                    <Icon :size="12" type="good"/>
                    {{ comment.likeCount }}
                </div>
            </div>
        </div>
    </div>
                <Comment
                    v-for="(comment,index) in musicCommentData"
                    :key="comment.id"
                    :border="!$utils.isLast(index, musicCommentData)"
                    :comment="comment"
                />
            </div>
            <el-pagination
                :current-page.sync="currentPage"
                :page-count="pageNumber"
                layout="prev, pager, next"
                v-bind="$attrs"
                v-on="$listeners"
                @current-change="onPageChange"
            />
        </template>
        <empty v-if="!loading">Do not have any comments now~</empty>
    </div>
</template>

<script>
import Loading from "../../../base/loading.vue";
import Comment from "../../../components/comment.vue";
import Empty from "../../../base/empty.vue";
import Icon from "../../../base/icon.vue";

export default {
    name: "blogComment",
    components: {Icon, Empty, Comment, Loading}
}
</script>

<style scoped>

</style>