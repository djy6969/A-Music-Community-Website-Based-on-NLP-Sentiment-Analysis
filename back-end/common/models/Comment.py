# coding: utf-8
from app import db

from common.models.Music import TMusic


class TComment(db.Model):
    __tablename__ = 't_comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    music_Id = db.Column(db.ForeignKey(TMusic.music_Id, ondelete="CASCADE"),
                         nullable=False, index=True)
    author = db.Column(db.String(64, 'utf8mb4_unicode_ci'), nullable=False, default='')
    publish_time = db.Column(db.DateTime, nullable=False)
    like_count = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
    nlp_point = db.Column(db.Float, nullable=False, default=0.0)

