from app import app
from flask import request, g
from flask_httpauth import HTTPBasicAuth
from common.models.User import TUser
from common.service import UserHelper

auth = HTTPBasicAuth()


# 请求前验证
@app.before_request
def before_request():
    user_info = check_login()
    g.current_user = user_info
    app.logger.info(user_info)
    app.logger.info('before_request')
    return

@app.after_request
def after_request(response):
    # 允许跨域请求的地址 (*代表所有地址)
    response.headers['Access-Control-Allow-Origin'] = '*'
    # 允许跨域请求的类型
    response.headers['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type, XMLHttpRequest"
    # 允许跨域请求的方式
    response.headers['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
    # 允许跨域请求携带cookie
    response.headers['Access-Control-Allow-Credentials'] = "true"
    response.headers['Access-Control-Max-Age'] = '1800'
    app.logger.info("after_request")
    return response

@app.after_request
def after_request(response):
    # 允许跨域请求的地址 (*代表所有地址)
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:8888'
    # 允许跨域请求的类型
    response.headers['Access-Control-Allow-Headers'] = "X-Requested-With, Content-Type, XMLHttpRequest"
    # 允许跨域请求的方式
    response.headers['Access-Control-Allow-Methods'] = "PUT,POST,GET,DELETE,OPTIONS"
    # 允许跨域请求携带cookie
    response.headers['Access-Control-Allow-Credentials'] = "true"
    app.logger.info("after_request")
    return response


@auth.verify_password
def verify_password(account, password):
    user_info = check_login()
    g.current_user = None
    if not user_info:
        return False
    else:
        g.current_user = user_info
        return True


'''
判断用户是否登录
'''


# 更改
def check_login():
    cookies = request.cookies
    cookie_name = app.config['AUTH_COOKIE_NAME']
    auth_cookie = cookies[cookie_name] if cookie_name in cookies else None

    if auth_cookie is None:
        app.logger.debug(1)
        return False

    # 后边可能需要增加信息，注意修改
    auth_info = auth_cookie.split('#')
    if len(auth_info) != 3:
        app.logger.debug(2)
        return False

    # 根据id查找用户
    try:
        user_info = TUser.query.filter_by(id=auth_info[1]).first()
    except Exception:
        app.logger.debug(3)
        return False

    if user_info is None:
        app.logger.debug(4)
        return False

    if auth_info[0] != UserHelper.geneAuthCode(user_info):
        app.logger.debug(5)
        return False

    app.logger.info(True)
    return user_info
