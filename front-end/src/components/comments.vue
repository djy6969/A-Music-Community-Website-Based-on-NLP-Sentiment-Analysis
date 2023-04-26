<template>
    <div class="comment">
        <template v-if="loading">
            <Loading :loading="loading"/>
        </template>
        <template v-else>
            <div
                v-if="comments.length >= 0"
                class="block"
            >
                <p
                    ref="commentTitle"
                    class="title"
                >
                    Newest Comment
                    <span class="count">({{ commentsSumNumber }})</span>
                </p>
                <Comment
                    v-for="(comment,index) in comments"
                    :key="comment.id"
                    :border="!$utils.isLast(index, comments)"
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
        <div>
            <el-input v-model="commentData"/>
            <el-button @click="addCommentData">Add</el-button>
        </div>
        <empty v-if="loading">Do not have any comment yet~</empty>
    </div>
</template>

<script type="text/ecmascript-6">
import Comment from "./comment"
import Empty from "../base/empty.vue";
import * as $utils from "../utils";
import {newRequest} from "../utils";
import Loading from "../base/loading.vue";

const SONG_TYPE = "song"

export default {
    props: {
        id: {
            type: String,
            required: true
        },
        type: {
            // SONG_TYPE, PLAYLIST_TYPE, MV_TYPE 之一
            type: String,
            default: SONG_TYPE
        }
    },
    data() {
        return {
            loading: false,
            hotComments: [],
            comments: [],
            total: 0,
            currentPage: 1,
            pageNumber: 0,
            commentsSumNumber: 0,
            commentData: ''
        }
    },
    methods: {
        addCommentData() {

            this.loading = true
            newRequest.post(
                '/comment/add_music_comment',
                {
                    video_Id: this.id,
                    comment_content: this.commentData,
                    username: this.$cookies.get('auth').username
                }
            ).then(res => {
                if (res.code === 200) {
                    this.$message.success('Add Your New Comment Successfully!')
                    this.loading = false
                    this.getCommentPageNumber()
                    this.onPageChange()
                }
            })
        },
        getCommentPageNumber() {
            this.loading = true
            newRequest.post(
                '/comment/get_music_comments_number',
                {
                    video_Id: this.id
                }
            ).then(res => {
                this.pageNumber = res.data.page
                this.commentsSumNumber = res.data.comments_num
                console.log(this.pageNumber)
            })
        },
        onPageChange() {
            newRequest.post(
                '/comment/get_music_comments',
                {
                    video_Id: this.id,
                    page: this.currentPage
                },
            ).then(res => {
                console.log(res)
                this.comments = res.data
                this.loading = false
            })
        }
    },
    computed: {
        $utils() {
            return $utils
        },
    },
    components: {
        Loading,
        Empty,
        Comment
    },
    mounted() {
        this.getCommentPageNumber()
        this.onPageChange()
    }
}
</script>

<style lang="scss" scoped>
.block {
  margin-bottom: 48px;

  .title {
    font-size: $font-size-lg;
    font-weight: $font-weight-bold;
    margin-bottom: 4px;

    .count {
      font-size: $font-size;
    }
  }
}

.pagination {
  text-align: right;
}
</style>
