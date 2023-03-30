from app import db
from common.models.User import TUser

class TBlog(db.Model):
    __tablename__ = 't_blog'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # foreignKey需要放到nullable之前
    userid = db.Column(db.SmallInteger,
                       db.ForeignKey(TUser.id, ondelete="CASCADE"), nullable=False)
    blog_content = db.Column(db.String(1024, 'utf8_bin'))
    piclist = db.Column(db.JSON)
    likes = db.Column(db.Integer, nullable=False)
    status = db.Column(db.SMALLINT, nullable=False, server_default="1")
    publish_time = db.Column(db.DateTime, server_default=db.FetchedValue())