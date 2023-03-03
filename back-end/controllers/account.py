import functools
from app import app

from flask import Blueprint, request, make_response
from common.service import MessageHelper, UserHelper


account = Blueprint('account', __name__)

'''
前后端使用axios通信，传递json
前端传递消息包含username, password
后端给前端传递cookie
'''
@account.route("/login", methods=['get','post'])
def login():
    username = request.values['username']
    password = request.values['password']

    if username is None or len(username) < 3:
        return MessageHelper.ops_renderErrJSON(msg="请输入正确格式的用户名")

    if password is None or len(password) < 6:
        return MessageHelper.ops_renderErrJSON(msg="请输入正确格式的登陆密码")

    user_info = {"id": "1", "username": "liuzijian", "password": "123456",
                 "password_salt": "lzj"}

    # cookie身份识别
    response = make_response(MessageHelper.ops_renderJSON(msg="登录成功！"))
    response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                        value="%s#%s" % (UserHelper.geneAuthCode(user_info), user_info.get("id")),
                        max_age = 60 * 60 * 24 * 7)

    return response


@account.route("/register")
def register():
    return "register page!"
