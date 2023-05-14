from app import app, db
from flask import Blueprint, request
from common.models.Friend import TFriend
from common.models.User import TUser
from common.service import MessageHelper, UserHelper, CommonHelper
from controllers import account

friend = Blueprint("friend", __name__)

# add friends methods
@friend.route("/addFriend", methods=['Post'])
def addFriend():
    # get user_id and friend_id
    user_id = request.json.get('user_id')
    print(user_id)
    friend_id = request.json.get('friend_id')
    print(friend_id)
    # add a new friend
    if TFriend.query.filter_by(user_id=user_id, friend_id=friend_id).first() is not None:
        # code = -1
        return MessageHelper.ops_renderErrJSON(msg="add new friend failed")
    friend = TFriend()
    friend.user_id = user_id
    friend.friend_id = friend_id
    db.session.add(friend)
    db.session.commit()

    return MessageHelper.ops_renderJSON(msg="add new friend success.")


# get all friends
@friend.route("/getFriends", methods=['Post'])
def getFriends():
    # get user_id
    user_id = request.json.get('user_id')
    # get all friends
    friends = TFriend.query.filter_by(user_id=user_id).all()
    # 返回所有好友id
    friendList = []
    for friend in friends:
        friendList.append(friend.friend_id)
    # return friend_id list
    # the front-end need get user information by user_id
    return MessageHelper.ops_renderJSON(data=friendList)


@friend.route("/deleteFriend", methods=['Post'])
def deleteFriend():
    # get user_id and friend_id
    user_id = request.json.get('user_id')
    friend_id = request.json.get('friend_id')
    # get friend
    friend = TFriend.query.filter_by(user_id=user_id, friend_id=friend_id).first()
    db.session.delete(friend)
    db.session.commit()
    return MessageHelper.ops_renderJSON(msg="Delete friend from friend list success.")


@friend.route("/sendMessage", methods=['Post'])
def sendMessage():
    # get user_id and friend_id
    user_id = request.json.get('user_id')
    friend_id = request.json.get('friend_id')

@friend.route("/getIdByUsername", methods=['POST'])
def getIdByUsername():
    username = request.json.get('username')
    return MessageHelper.ops_renderJSON(data={"user_id": TUser.query.filter_by(username=username).first().id})