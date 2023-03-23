import functools
from app import app, db

from common.models.User import TUser
from flask import Blueprint, request, make_response
from common.service import MessageHelper, UserHelper


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


    # username = request.values['username']
    # email = request.values['email']
    # password = request.values['password']
    # password2 = request.values['password2']

    if username is None or len(username) < 3:
        return MessageHelper.ops_renderErrJSON(msg='please input right format username~')

    if password is None or len(password) < 6:
        return MessageHelper.ops_renderErrJSON(msg='please input right format password, the length should not less than 6~')

    if password2 is None or len(password2) < 6 or password != password2:
        return MessageHelper.ops_renderErrJSON(msg='please input right format confirm password~')

    if len(tel) != 11:
        return MessageHelper.ops_renderErrJSON(msg='please input right format telephone number (11)~')

    if nickname is None:
        return MessageHelper.ops_renderErrJSON(msg="please input a nickname!")

    user_info = TUser.query.filter_by(username=username).first()
    if user_info:
        return MessageHelper.ops_renderErrJSON(msg="the username is existed, please change another one")

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

    return MessageHelper.ops_renderJSON(msg='registration success!')


# 用户登录
@account.route("/login", methods=['get', 'post'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or len(username) < 3:
        return MessageHelper.ops_renderErrJSON(msg="please input right format username.")

    if password is None or len(password) < 6:
        return MessageHelper.ops_renderErrJSON(msg="please input right format password")

    # user_info = {"id": "1", "username": "liuzijian", "password": "123456",
    #              "password_salt": "lzj"}

    try:
        user_info = TUser.query.filter_by(username=username).first()
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="")

    if user_info is None:
        return MessageHelper.ops_renderErrJSON("please input correct username and password")

    if user_info.password != UserHelper.genePwd(password, user_info.password_salt):
        return MessageHelper.ops_renderErrJSON("please input correct username and password")

    # cookie身份识别
    response = make_response(MessageHelper.ops_renderJSON(msg="login success!"))
    try:
        # user last number is 1, staff is 2
        response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                            value="%s#%s#1" % (UserHelper.geneAuthCode(user_info), user_info.id),
                            max_age = 60 * 60 * 24 * 7)
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="flask edition too low, please upgrade flask edition.")

    return response


# user logout
@account.route('/logout', methods=["GET"])
def logout():
    response = make_response(MessageHelper.ops_renderJSON(msg="logout success."))
    response.delete_cookie(app.config['AUTH_COOKIE_NAME'])
    return response






