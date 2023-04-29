<template>
    <div class="container">
        <div class="leftSide">
            <div class="search_chat">
                <div style="display: flex">
                    <input placeholder="Add New Friend" type="text" v-model="friendId">
                    <el-button @click="addFriend">Add</el-button>
                </div>
            </div>
            <div class="search_chat">
                <div style="display: flex">
                    <input placeholder="Add New Friend" type="text" v-model="friendId">
                    <el-button @click="addFriend">Chat</el-button>
                </div>
            </div>
            <!--ChatList-->

            <chat-list v-for="(item, index) in this.friendList" :key="index" :id="item"/>
        </div>


        <div class="rightSide">
            <div class="header">
                <div class="imgText">
                    <div class="userimg">
                        <img class="cover" src="img1.jpg">
                    </div>
                    <h4>开心果<br><span>在线</span></h4>
                </div>
                <ul class="nav_icons">
                    <li><img src="消息.png"></li>
                    <li><img src="更多.png"></li>
                </ul>
            </div>
            <!--chatbox-->
            <div class="chatBox">
                <div class="message my_message">
                    <p>你在干嘛呢？<br><span>10:15</span></p>
                </div>
                <div class="message frnd_message">
                    <p>在写作业<br><span>10:15</span></p>
                </div>
                <div class="message frnd_message">
                    <p>天气太热了天气太热了天气太热了天气太热了天气太热了天气太热了天气太热了天气太热了天气太热了天气太热了天气太热了天气太热了<br><span>10:15 </span>
                    </p>
                </div>
                <div class="message my_message">
                    <p>对啊 也不下雨<br><span>10:15</span></p>
                </div>
                <div class="message my_message">
                    <p>希望以后凉快点<br><span>10:15</span></p>
                </div>
            </div>

            <!--chat input-->
            <div class="chatbox_input">
                <div class="instrument">
                    <img src="表情.png">
                    <img src="语音.png">
                </div>
                <div>
                    <input type="text">
                </div>

            </div>
        </div>

    </div>
</template>

<script>
import {newRequest} from "../../utils";
import ChatList from "./chatList.vue";

export default {
    name: "index",
    components: {ChatList},
    data(){
        return{
            friendId: 0,
            friendList: []
        }
    },
    methods:{
        addFriend(){
            newRequest.post(
                '/friend/addFriend',
                {
                    user_id: this.$cookies.get('auth').userid,
                    friend_id: this.friendId
                }
            ).then(res=>{
                if (res.code === 200){
                    this.$message({
                        message: 'Add new Friend Success!',
                        type: 'success'
                    })
                    this.friendId = 0
                }
            })
        },
        getFriends(){
            newRequest.post(
                '/friend/getFriends',
                {
                    user_id: this.$cookies.get('auth').userid,
                }
            ).then(res=>{
                if (res.code === 200){
                    this.friendList = res.data
                    console.log(this.friendList)
                }
            })
        }
    },
    mounted() {
        this.getFriends()
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com css2?family-Open+Sans:wght@300;400;00;600;700&display=swap');
*
{
    margin: 0;padding: 0;
    box-sizing: border-box;
    font-family: 'Open Sans' ,sans-serif;
}
body
{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background: linear-gradient(#009688 0%,#009688 130px,#d9dbd5 130px,#d9dbd5 100%)
}
.container
{
    position: relative;
    width: 1396px;
    max-width: 100%;
    height: calc( 100vh - 40px);
    background:#fff;
    box-shadow: 0 1px 1px 0 rgba(0,0,0,0.06),0 2px 5px 0 rgba(0,0,0,0.06);
    display: flex;
}
.container .leftSide
{
    position: relative;
    flex:30%;
    background:#fff;
    border-right: 1px solid rgba(0, 0, 0, 0.2);
}
.container .rightside
{
    position: relative;
    flex: 70%;
    background:#e5ddd5;
}
.container .rightside::before
{
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;

    opacity: 0.06;
}
.header
{
    position: relative;
    width: 100%;
    height: 60px;
    background: #ededed;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 15px;
}
.userimg
{
    position: relative;
    width: 40px;
    height: 40px;
    overflow: hidden;
    border-radius: 50%;
    cursor: pointer;
}
.cover
{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
.nav_icons
{
    display: flex;
}
.nav_icons li
{
    display: flex;
    list-style: none;
    cursor: pointer;
    color: #51585c;
    font-size: 1.5em;
    margin-left: 22px;
}
.search_chat
{
    position: relative;
    width: 100%;
    height: 50px;
    background: #f6f6f6;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 0 15px;
}
.search_chat div
{
    width: 100%;
}
.search_chat div input
{
    width:100%;
    outline: none;
    border: none;
    background: #fff;
    padding: 6px;
    height: 38px;
    border-radius: 30px;
    font-size: 14px;
    padding-left: 40px;
}
.search_chat div input::placeholder
{
    color: #bbb;
}
.search_chat div img
{
    position: absolute;
    left: 30px;
    top: 14px;
    font-size: 1.5em;
}


.message_p
{
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.message_p p
{
    color: #aaa;
    display: -webkit-box;
    font-size: 0.9em;
    overflow: hidden;
    text-overflow: ellipsis;
}
.message_p b
{
    background-color: red;
    color: #fff;
    min-width: 20px;
    height: 20px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.75em;
}
.imgText
{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}
.imgText h4
{
    font-weight: 500;
    line-height: 1.2em;
    margin-left: 15px;
}
.imgText h4 span
{
    font-size: 0.8em;
    color: #555;
}
.chatBox
{
    position: relative;
    width: 100%;
    padding: 50px;
    overflow-y: auto;
}
.message
{
    position: relative;
    display: flex;
    width: 100%;
    margin: 5px 0;
}
.message p
{
    position: relative;
    right: 0;
    text-align: right;
    max-width: 65%;
    padding: 12px;
    background: #dcf8c6;
    border-radius: 10px;
    font-size: 0.9em;
}
.message p::before
{
    content: '';
    position: absolute;
    top: 0;
    right: -12px;
    width: 20px;
    height: 20px;
    background: linear-gradient(135deg,#dcf8c6 0%,#dcf8c6 50%,transparent 50%,transparent);
}
.message p span
{
    display: block;
    margin-top: 5px;
    font-size: 0.85em;
    opacity: 0.5;
}
.my_message
{
    justify-content: flex-end;
}
.frnd_message
{
    justify-content: flex-start;
}
.frnd_message p
{
    background: #fff;
    text-align: left;
}
.message.frnd_message p::before
{
    content: '';
    position: absolute;
    top: 0;
    left: -12px;
    width: 20px;
    height: 20px;
    background: linear-gradient(225deg,#fff 0%,#fff 50%,transparent 50%,transparent);
}
.chatbox_input
{
    position: relative;
    width: 100%;
    height: 150px;
    background: #f0f0f0;
    padding: 15px;
    justify-content: space-between;
    align-items: center;
}
.chatbox_input input
{
    position: relative;
    width: 90%;

    margin: 0 20px;
    padding: 10px 20px;
    border: none;
    outline: none;
    border-radius: 30px;
    font-size: 1em;
}
</style>