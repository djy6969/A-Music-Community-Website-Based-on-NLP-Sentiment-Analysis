# coding: utf-8
from app import db
import datetime


class TComment(db.Model):
    __tablename__ = 't_comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    video_Id = db.Column(nullable=False, index=True, default='')
    author = db.Column(db.String(64, 'utf8mb4_unicode_ci'), nullable=False, default='')
    publish_time = db.Column(db.DateTime, nullable=False)
    likeCount = db.Column(db.Integer, nullable=False, default=0)
    comment = db.Column(db.Text(collation='utf8mb4_unicode_ci'), nullable=False)

