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
                    <span class="count">({{ musicCommentData.length }})</span>
                </p>
                <div
                    class="comment"
                    v-for="(comment,index) in musicCommentData"
                    :key="index"
                >
                    <div class="content">
                        <p class="comment-text">
                            <span class="username">{{ comment.author }}:</span>
                            <span class="text">{{ comment.comment }}</span>
                        </p>
                        <div class="bottom">
                            <span class="date">{{ $utils.formatDate(comment.publish_time) }}</span>
                            <div class="actions">
                                <Icon :size="12" type="good"/>
                                {{ comment.likeCount }}
                            </div>
                        </div>
                    </div>
                </div>
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
import Empty from "../../../base/empty.vue";
import * as $utils from "../../../utils";
import {newRequest} from "../../../utils";
import Icon from "../../../base/icon.vue";

export default {
    name: "musicComment",
    computed: {
        $utils() {
            return $utils
        }
    },
    components: {Icon, Empty, Loading},
    data() {
        return {
            loading: true,
            musicCommentData: [],
            currentPage: 0,
            pageNumber: 50
        }
    },
    methods: {
        onPageChange() {
            newRequest.post(
                '/comment/',
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
    }
}
</script>

<style scoped>

</style>