from app import app

'''
拦截处理器和错误处理器
'''
from interceptors import Auth

'''
蓝图
'''
from controllers.homepage import homepage
from controllers.account import account
from controllers.music import music
from controllers.blog import blog


app.register_blueprint(homepage, url_prefix="/")
app.register_blueprint(account, url_prefix="/account")
app.register_blueprint(blog, url_prefix="/blog")
app.register_blueprint(music, url_prefix="/music")


