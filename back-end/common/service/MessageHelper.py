'''
这个类用于写消息服务类，提供消息帮助信息
'''

from flask import jsonify


# 对消息进行封装
# 正常消息默认code = 200
# 将消息转换成json形式
def ops_renderJSON(code=200, msg="operation succeed!", data={}):
    response = {"code": code, 'msg': msg, "data": data}
    return jsonify(response)


# 系统出错消息封装，code=-1
# 默认消息联系管理员
def ops_renderErrJSON(msg="Failed to get data, please contact the staffs~", data={}):
    return ops_renderJSON(code=-1, msg=msg, data=data)