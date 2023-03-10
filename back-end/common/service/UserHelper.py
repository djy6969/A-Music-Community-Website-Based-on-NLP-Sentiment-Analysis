'''

有关用户密码加密的用户账户服务类

'''

import base64
import random
import string
import hashlib

def genePwd(pwd, salt):
    m = hashlib.md5()
    str = "%s-%s" % (base64.encodebytes(pwd.encode("utf-8")), salt)
    m.update(str.encode("utf-8"))
    return m.hexdigest()

def geneSalt(length=16):
    key_list = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
    return ("".join(key_list))

def geneAuthCode(user_info=None):
    m = hashlib.md5()
    infor = "%s-%s-%s-%s" % (
        user_info.id, user_info.username, user_info.password,
        user_info.password_salt)
    m.update(infor.encode("utf-8"))
    return m.hexdigest()

