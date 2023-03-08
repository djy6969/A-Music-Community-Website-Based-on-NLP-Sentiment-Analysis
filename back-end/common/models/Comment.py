# coding: utf-8
from app import db

t_comment = db.Table(
    't_comment',
    db.Column('video_Id', db.ForeignKey('t_music.video_Id'), nullable=False, index=True),
    db.Column('author', db.String(64, 'utf8mb4_unicode_ci'), nullable=False),
    db.Column('publish_time', db.DateTime, nullable=False),
    db.Column('likeCount', db.Integer, nullable=False),
    db.Column('comment', db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
)

