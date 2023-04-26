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
from controllers.search import search
from controllers.comment import comment
from controllers.collection import collection
from controllers.friend import friend
from controllers.chat import chat


app.register_blueprint(homepage, url_prefix="/api")
app.register_blueprint(account, url_prefix="/api/account")
app.register_blueprint(blog, url_prefix="/api/blog")
app.register_blueprint(music, url_prefix="/api/music")
app.register_blueprint(search, url_prefix="/api/search")
app.register_blueprint(comment, url_prefix="/api/comment")
app.register_blueprint(collection, url_prefix="/api/collection")
app.register_blueprint(friend, url_prefix="/api/friend")
app.register_blueprint(chat, url_prefix="/api/chat")



