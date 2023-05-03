<template>
    <div v-if="comment" class="comment">
        <div :class="{ border }" class="content">
            <p class="comment-text">
                    <span class="username" @click="dialogVisible=true">
                        {{ comment.author }}:
                    </span>
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
        <el-dialog
            title="Hint"
            :visible.sync="dialogVisible"
            width="30%">
            <span>Add this person as your friend?</span>
            <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">Cancel</el-button>
                <el-button type="primary" @click="addFriend">Sure</el-button>
            </span>
        </el-dialog>
    </div>
</template>

<script type="text/ecmascript-6">
import * as $utils from "../utils";
import Icon from "@/base/icon.vue";
import {newRequest} from "@/utils";

export default {
    components: {Icon},
    computed: {
        $utils() {
            return $utils
        }
    },
    props: ["comment", "border"],
    data() {
        return {
            dialogVisible: false
        }
    },
    methods: {
        addLikeAccount() {
            newRequest.post(
                '/comment/likeComment',
                {
                    commentId: this.comment.comment_id
                }
            ).then(res => {
                console.log(res)
                if (res.code === 200) {
                    this.$message({
                        message: 'Like Success!',
                        type: "success"
                    })
                    this.comment.likeCount += 1
                }
            })
        },
        addFriend() {
            this.getIdByUsername()
            console.log(this.comment.userid)
            newRequest.post(
                '/friend/addFriend',
                {
                    user_id: this.$cookies.get('auth').userid,
                    friend_id: this.comment.userid
                }
            ).then(res => {
                this.$message.success(res.msg)
                this.dialogVisible = false
            })
        },
        getIdByUsername(){
            newRequest.post(
                '/friend/getIdByUsername',
                {
                    username: this.comment.author
                }
            ).then(res=>{
                this.comment.userid = res.data.user_id
                console.log(this.comment.userid)
            })
        }
    }
}
</script>

<style lang="scss" scoped>
.comment {
  display: flex;
  padding-top: 20px;

  .avatar {
    @include img-wrap(40px);
    margin-right: 12px;

    img {
      border-radius: 50%;
    }
  }

  .content {
    padding-bottom: 20px;
    width: 100%;
    font-size: $font-size-sm;

    &.border {
      border-bottom: 1px solid var(--border);
    }

    .replied {
      padding: 8px;
      margin-top: 8px;
      background: var(--song-shallow-grey-bg);
      border-radius: 4px;
    }

    .comment-text {
      .username {
        display: inline-block;
        margin-right: 4px;
        color: $blue;
      }

      .text {
        line-height: 1.5;
      }
    }

    .bottom {
      display: flex;
      justify-content: space-between;
      margin-top: 8px;

      .date {
        color: var(--font-color-grey-shallow);
      }

      .actions {
        color: var(--font-color-grey-shallow);
      }
    }
  }
}
</style>
