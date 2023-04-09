import functools
from app import app, db

from common.models.User import TUser
from flask import Blueprint, request, make_response
from common.service import MessageHelper, UserHelper, CommonHelper
from common.nlp import nlp

account = Blueprint('account', __name__)

'''
前后端使用axios通信，传递json
前端传递消息包含username, password
后端给前端传递cookie
'''


# 注册账号
@account.route("/register", methods=['POST', 'GET'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    password2 = request.json.get('password2')
    email = request.json.get('email')
    tel = request.json.get('tel')
    nickname = request.json.get('nickname')

    # test data
    # username = '111111'
    # password = "111111"
    # password2 = "111111"
    # tel = '11111111111'
    # email = ''
    # nickname = "111111"

    # username = request.values['username']
    # email = request.values['email']
    # password = request.values['password']
    # password2 = request.values['password2']

    if username is None or len(username) < 3:
        return MessageHelper.ops_renderErrJSON(msg='请输入正确格式的用户名~')

    if password is None or len(password) < 6:
        return MessageHelper.ops_renderErrJSON(msg='请输入正确格式的密码，且长度不小于六个字符~')

    if password2 is None or len(password2) < 6 or password != password2:
        return MessageHelper.ops_renderErrJSON(msg='请输入正确格式的确认密码~')

    if len(tel) != 11:
        return MessageHelper.ops_renderErrJSON(msg='请输入正确格式的电话号码（11位）~')

    if nickname is None:
        return MessageHelper.ops_renderErrJSON(msg="请输入一个昵称！")

    user_info = TUser.query.filter_by(username=username).first()
    if user_info:
        return MessageHelper.ops_renderErrJSON(msg="您输入的用户名已存在，请换一个")

    # try:
    # system generated password encryption string
    pwd_salt = UserHelper.geneSalt(32)
    user = TUser()
    user.username = username
    user.password = UserHelper.genePwd(password, pwd_salt)
    user.password_salt = pwd_salt
    user.email = email
    user.tel = tel
    user.nickname = nickname
    user.role = 1
    # info = {
    #     'username': username,
    #     'password_salt': pwd_salt,
    #     'password': UserHelper.genePwd(password, pwd_salt),
    #     'email': email,
    #     'tel': tel,
    #     'nickname': nickname
    # }
    db.session.add(user)
    db.session.commit()
    # except Exception as e:
    #     db.session.rollback()
    #     return MessageHelper.ops_renderErrJSON(msg="注册信息储存出现问题，请联系管理员解决。")

    return MessageHelper.ops_renderJSON(msg='注册成功')


# 用户登录
@account.route("/login", methods=['get', 'post'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    # username = request.values['username']
    # password = request.values['password']
    print(username)

    if username is None or len(username) < 3:
        return MessageHelper.ops_renderErrJSON(msg="请输入正确格式的用户名")

    if password is None or len(password) < 6:
        return MessageHelper.ops_renderErrJSON(msg="请输入正确格式的登陆密码")

    # user_info = {"id": "1", "username": "liuzijian", "password": "123456",
    #              "password_salt": "lzj"}
    try:
        user_info = TUser.query.filter_by(username=username).first()
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="")
    if user_info is None:
        return MessageHelper.ops_renderErrJSON("请输入正确的登录用户名和密码")

    if user_info.password != UserHelper.genePwd(password, user_info.password_salt):
        return MessageHelper.ops_renderErrJSON("请输入正确的登录用户名和密码")
    # cookie身份识别
    response = make_response(
        MessageHelper.ops_renderJSON(
            msg="登录成功！",
            data={
                'id': user_info.id,
                'url': user_info.head,
                'role': user_info.role
            }
        )
    )
    try:
        print("%s#%s#%s" % (UserHelper.geneAuthCode(user_info), user_info.id, user_info.role))
        # user last number is 1, staff is 2
        response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                            value="%s#%s#%s" % (UserHelper.geneAuthCode(user_info), user_info.id, user_info.role),
                            max_age=60 * 60 * 24 * 7, samesite='None')
        # , secure = True
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="flask 版本过低，请升级flask版本")

    return response


# 用户退出
@account.route('/logout', methods=["GET"])
def logout():
    response = make_response(MessageHelper.ops_renderJSON(msg="退出成功"))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response


# user upload head portrait
# need the front-end upload user_id and head portrait
# update head portrait image still use this api
@account.route("/upload_head_portrait", methods=["POST"])
def upload_head_protrait():
    user_id = request.values['user_id']
    image = request.files.get('head')
    user = TUser.query.filter_by(id=user_id).first()
    user.head = "https://ipa-012.ucd.ie/image/" + CommonHelper.uploadServerPic(image, user_id)
    db.session.commit()
    return MessageHelper.ops_renderJSON(msg="upload successfully")


# get user id from the front-end
# return the user information
@account.route("/get_user_info", methods=["POST"])
def get_user_info():
    user_id = request.json.get('user_id')
    user = TUser.query.filter_by(id=user_id).first()
    # email, tel, nickname, head
    user_info = {
        "email": user.email,
        'tel': user.tel,
        'nickname': user.nickname,
        'head_protrait': user.head
    }
    return MessageHelper.ops_renderJSON(msg="personal information", data=user_info)


# update user information
# need the front-end tell us user_id and which information they want to update
@account.route("/update_user_information", methods=["POST"])
def update_user_information():
    user_id = request.json.get('user_id')
    name = request.json.get('name')
    info_content = request.json.get('content')
    user = TUser.query.filter_by(id=user_id).first()
    if user is not None:
        if name == 'email':
            user.email = info_content
        elif name == 'tel':
            user.tel = info_content
        elif name == 'nickname':
            user.nickname = info_content
        elif name == 'description':
            user.description = info_content
        db.session.commit()
        return MessageHelper.ops_renderJSON(msg="update successfully!")
    else:
        return MessageHelper.ops_renderErrJSON(msg="error happened.")
