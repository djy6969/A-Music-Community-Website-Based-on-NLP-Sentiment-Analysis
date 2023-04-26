from app import db
from common.models.User import TUser


class TMessage(db.Model):
    __tablename__ = 't_friend'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # foreignKey需要放到nullable之前
    user_id = db.Column(db.SmallInteger,
                        db.ForeignKey(TUser.id, ondelete="CASCADE"), nullable=False)
    friend_id = db.Column(db.SmallInteger,
                          db.ForeignKey(TUser.id, ondelete="CASCADE"), nullable=False)
    message = db.Column(db.String(256, 'utf8_bin'), nullable=False, default='')
    state = db.Column(db.SMALLINT, nullable=False, server_default="1")
    send_time = db.Column(db.DateTime, server_default=db.FetchedValue())
