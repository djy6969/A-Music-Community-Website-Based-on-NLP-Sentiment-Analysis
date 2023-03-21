from app import db
import Blog, User

class TBlogComment(db.Model):
    __tablename__ = 't_blog_comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.SmallInteger,
                       db.ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    blogid = db.Column(db.Integer,
                       db.ForeignKey(Blog.id, ondelete="CASCADE"), nullable=False)
    content = db.Column(db.String(1024, 'utf8_bin'))
    publish_time = db.Column(db.DateTime, server_default=db.FetchedValue())