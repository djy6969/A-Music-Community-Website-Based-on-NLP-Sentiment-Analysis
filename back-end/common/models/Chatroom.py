from app import db
from common.models.User import TUser

class TChatroom(db.Model):
    __tablename__ = 't_chatroom'

    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True
    )
    # foreignKey需要放到nullable之前
    user_id = db.Column(
        db.SmallInteger,
        db.ForeignKey(TUser.id, ondelete="CASCADE"),
        nullable=False
    )
    friend_id = db.Column(
        db.SmallInteger,
        db.ForeignKey(TUser.id, ondelete="CASCADE"),
        nullable=False
    )
    room = db.Column(
        db.String(128, 'utf8_bin'),
        nullable=False,
        default=''
    )
    send_time = db.Column(
        db.DateTime,
        server_default=db.FetchedValue()
    )