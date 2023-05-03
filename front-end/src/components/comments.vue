<template>
    <div class="comment">
        <template v-if="loading">
            <Loading :loading="loading"/>
        </template>
        <template v-else>
            <div
                    class="block"
                    v-if="shouldCommentShow"
            >
                <p
                        class="title"
                        ref="commentTitle"
                >
                    最新评论
                    <span class="count">({{ commentsSumNumber }})</span>
                </p>
                <Comment
                    v-for="(comment, index) in comments"
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
        <div style="display: flex">
            <el-input v-model="commentData"/>
            <el-button @click="addCommentData">Add</el-button>
        </div>
        <empty v-if="!loading && !shouldHotCommentShow && !shouldCommentShow">还没有评论哦~</empty>
    </div>
</template>

<script type="text/ecmascript-6">

import {newRequest} from "@/utils"
import Comment from "./comment"
import * as $utils from "@/utils";

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
                console.log('get music comment number')
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
                console.log('Gte music comments')
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
        shouldHotCommentShow() {
            return this.hotComments.length > 0 && this.currentPage === 1
        },
        shouldCommentShow() {
            return this.comments.length > 0
        }
    },
    components: {
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
