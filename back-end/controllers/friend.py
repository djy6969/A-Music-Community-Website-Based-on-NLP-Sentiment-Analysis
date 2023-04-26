from app import app, db
from flask import Blueprint, request
from common.models.Friend import TFriend
from common.service import MessageHelper, UserHelper, CommonHelper
from controllers import account

friend = Blueprint("friend", __name__)

# add friends methods
@friend.route("/addFriend", methods=['Post'])
def addFreind():
    # get user_id and friend_id
    user_id = request.json.get('user_id')
    friend_id = request.json.get('friend_id')
    print(user_id)
    print(friend_id)
    # add a new friend
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
    print(user_id)
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