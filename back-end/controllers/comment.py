import math, datetime

from app import db
from flask import Blueprint, request
# from common.nlp.nlp import sentient_analysis
from common.service import MessageHelper
from common.models.Comment import TComment

comment = Blueprint("comment", __name__)

# @comment.route('/single_comment_analysis', methods=['POST'])
# def single_comment_analysis():
#     comment = request.json.get('comment')
#     score = sentient_analysis(comment)
#     return MessageHelper.ops_renderJSON(data={'score': score})

# get music comment number
# need the front-end send the video_id
@comment.route('/get_music_comments_number', methods=['POST'])
def get_music_comments_number():
    video_Id = request.json.get('video_Id')
    comments_num = TComment.query.filter_by(music_Id=video_Id).count()
    print(comments_num)
    return MessageHelper.ops_renderJSON(data={'page': math.ceil(comments_num / 50), 'comments_num': comments_num})

# get music comment by video_Id
# need the front-end send the video_id and page
@comment.route('/get_music_comments', methods=['POST'])
def get_music_comments():
    video_Id = request.json.get('video_Id')
    page = request.json.get('page')
    comments = TComment.query.filter_by(music_Id=video_Id).offset(50 * (page-1)).limit(50).all()
    comments_list = []
    for comment in comments:
        comment_info = {'comment_id': comment.id, 'likeCount': comment.like_count, 'author': comment.author,
                        'publish_time': comment.publish_time, 'comment': comment.comment}
        comments_list.append(comment_info)
    return MessageHelper.ops_renderJSON(data=comments_list)


# add music comment by video_Id
# need the front-end send the video_id and comment_content and username
@comment.route('/add_music_comment', methods=['POST'])
def add_music_comment():
    video_Id = request.json.get('video_Id')
    comment_content = request.json.get('comment_content')
    username = request.json.get('username')
    comment = TComment()
    comment.music_Id = video_Id
    comment.author = username
    comment.comment = comment_content
    comment.publish_time = datetime.datetime.now()
    db.session.add(comment)
    db.session.commit()
    return MessageHelper.ops_renderJSON()


# delete music comment by comment_id
# need the front-end send comment_id
@comment.route('/delete_music_comment', methods=['POST'])
def delete_music_comment():
    comment_id = request.json.get('comment_id')
    comment = TComment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return MessageHelper.ops_renderJSON()


# like a comment
@comment.route('/likeComment', methods=['POST'])
def likeComment():
    comment_id = request.json.get('commentId')
    comment = TComment.query.filter_by(id=comment_id).first()
    comment.like_count = comment.like_count + 1
    # db.session.update(comment)
    db.session.commit()
    return MessageHelper.ops_renderJSON()