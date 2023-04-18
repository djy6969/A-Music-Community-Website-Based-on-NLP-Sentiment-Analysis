from app import db
from common.models.User import TUser
from common.models.Blog import TBlog

class TBlogComment(db.Model):
    __tablename__ = 't_blog_comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.SmallInteger,
                       db.ForeignKey(TUser.id, ondelete="CASCADE"), nullable=False)
    blogid = db.Column(db.Integer,
                       db.ForeignKey(TBlog.id, ondelete="CASCADE"), nullable=False)
    content = db.Column(db.String(1024, 'utf8_bin'))
    publish_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    nlp_point = db.Column(db.Float, nullable=False, default=0.0)