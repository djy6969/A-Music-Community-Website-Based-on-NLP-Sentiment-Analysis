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
    video_Id = request.values['video_Id']
    comments_num = TComment.query.filter_by(video_Id=video_Id).count()
    print(comments_num)
    return MessageHelper.ops_renderJSON(data={'page': math.ceil(comments_num / 50)})

# get music comment by video_Id
# need the front-end send the video_id and page
@comment.route('/get_music_comments', methods=['POST'])
def get_music_comments():
    video_Id = request.values['video_Id']
    page = request.values['page']
    comments = TComment.query.filter_by(video_Id=video_Id).limit(50 * int(page)).all()
    comments_list = []
    for comment in comments:
        comment_info = {'comment_id': comment.id, 'author': comment.author, 'publish_time': comment.publish_time, 'comment': comment.comment}
        comments_list.append(comment_info)
    return MessageHelper.ops_renderJSON(data=comments_list)


# add music comment by video_Id
# need the front-end send the video_id and comment_content and username
@comment.route('/add_music_comment', methods=['POST'])
def add_music_comment():
    video_Id = request.values['video_Id']
    comment_content = request.values['comment_content']
    username = request.values['username']
    comment = TComment()
    comment.video_Id = video_Id
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
    comment_id = request.values['comment_id']
    comment = TComment.query.filter_by(id=comment_id).first()
    db.session.delete(comment)
    db.session.commit()
    return MessageHelper.ops_renderJSON()