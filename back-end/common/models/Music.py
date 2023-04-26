# coding: utf-8

from app import db


class TMusic(db.Model):
    __tablename__ = 't_music'

    music_Id = db.Column(db.String(32, 'utf8mb4_unicode_ci'), primary_key=True, unique=True, default='')
    publish_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    title = db.Column(db.String(255, 'utf8mb4_unicode_ci'), nullable=False)
    description = db.Column(db.Text(collation='utf8mb4_unicode_ci'))
    like_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    view_count = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue())
    image_url = db.Column(db.String(128, 'utf8mb4_unicode_ci'), nullable=False)
    tags = db.Column(db.JSON)
    duration = db.Column(db.String(8), nullable=False)
    artist = db.Column(db.String(64), nullable=False)
    # 1 is usable, 0 is unusable
    usable = db.Column(db.SmallInteger, nullable=False, default=1)
