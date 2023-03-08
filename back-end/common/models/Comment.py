# coding: utf-8
from app import db

t_t_comment = db.Table(
    't_comment',
    db.Column('video_Id', db.ForeignKey('t_music.video_Id'), nullable=False, index=True),
    db.Column('author', db.String(64, 'utf8mb4_unicode_ci'), nullable=False),
    db.Column('publish_time', db.DateTime, nullable=False),
    db.Column('likeCount', db.Integer, nullable=False),
    db.Column('comment', db.Text(collation='utf8mb4_unicode_ci'), nullable=False)
)



class TMusic(db.Model):
    __tablename__ = 't_music'

    video_Id = db.Column(db.String(32, 'utf8mb4_unicode_ci'), primary_key=True, unique=True)
    publish_time = db.Column(db.DateTime, nullable=False)
    title = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = db.Column(db.Text(collation='utf8mb4_unicode_ci'))
    like_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    image_url = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False)
    tags = db.Column(db.JSON)
