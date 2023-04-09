from app import db
from common.models.User import TUser
from common.models.Music import TMusic

class TBlogComment(db.Model):
    __tablename__ = 't_collection'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.SmallInteger,
                       db.ForeignKey(TUser.id, ondelete="CASCADE"), nullable=False)
    collection_name = db.Column(db.String(64, 'utf8_bin'), nullable=False, default='collect')
    video_Id = db.Column(db.String(32, 'utf8_bin'),
                       db.ForeignKey(TMusic.video_Id, ondelete="CASCADE"), nullable=False)
    update_time = db.Column(db.DateTime, server_default=db.FetchedValue())