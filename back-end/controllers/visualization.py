import math
import pymysql
from sshtunnel import *
from tqdm import tqdm
import datetime
import time
from flask import Blueprint, request
from common.service import MessageHelper
from common.models.Comment import TComment
from common.models.Music import TMusic
from common.models.BlogComment import TBlogComment
from common.models.Blog import TBlog

visualization = Blueprint('visualization', __name__)

def song_score(input_id, now_time):
    # TODO: 得到这个id的歌
    # dict: {'id': id, 'view_count': Q_views, 'comment_count': Q_answer, 'like_count': Ascores,
    # 'pos-nega': Q_score, 'publish_time': Q_age, 'last_comment_time': Q_updatated}
    # sql = 'SELECT * FROM `music`.`t_music` WHERE `title` = {}'.format(input_id)
    # sql = 'SELECT * FROM music.t_music WHERE music_Id="{}"'.format(input_id)
    # cursor = conn.cursor()
    # cursor.execute(sql)
    # conn.commit()
    # song_tuple = cursor.fetchall()
    # cursor.close()
    music = TMusic()
    comment = TComment()
    song_title = TMusic.title
    view_count = TMusic.view_count
    like_count = TMusic.like_count
    pub_time = TMusic.publish_time
    # 通过id得到同一个song_id下的所有comments
    # comments_lst: [
    # {'score': score, 'time': time, 'comment_id': id},
    # {'score': score, 'time': time, 'comment_id': id},
    # ...
    # ]
    comments_lst = TComment.query.filter_by(music_Id=input_id).all()
    # qupdated = get_latest_time(comments_lst)
    qupdated = TComment.query.filter_by(music_Id=input_id).order_by(TComment.publish_time.desc()).first().publish_time
    qscore = get_all_score(comments_lst)
    qanswer = len(comments_lst)
    qviews = view_count
    ascore = like_count
    qage = pub_time
    qage_day = (now_time - qage).total_seconds() / (3600 * 24)
    qupdated_day = (now_time - qupdated).total_seconds() / (3600 * 24)
    qgap = (qupdated - qage).total_seconds() / (3600 * 24)

    score = float((math.log(qviews, 10) * 4 + (qanswer * qscore) /
                  5 + ascore) / math.pow((1 + qage_day / 2 + qupdated_day / 2), 1.5))
    return score

def blog_score(input_id):
    # TODO: 得到这个id的blog
    # dict: {'id': id, 'publish_time': t}
    blog = input_id
    # 通过id得到同一个id下的所有comments
    # comments_dict: {
    # 'blog_id': blog_id, 'score': score, 'comment_id': id}
    # blog_comment_lst = TBlogComment.query.filter_by(blog_id=input_id).all()

    # comments_dict = comments.get_dict()
    publish_time = TBlog.query.filter_by(id=input_id).first().publish_time
    t = (publish_time - datetime.datetime(2023, 4, 20)).total_seconds()
    vote_direction, z = count_posnega(input_id)

    score = math.log(z, 10) + (vote_direction * t / 45000)

    return score


# def get_latest_time(comments_lst):
#     latest_time = comments_lst[0]['time']
#     for i in comments_lst:
#         if i['time'] > latest_time:
#             latest_time = i['time']
#     return latest_time


def get_all_score(comments_lst):
    score_sum = 0
    for i in comments_lst:
        score_sum += i.nlp_point
    return score_sum


def count_posnega(input_id):
    pos_num = TBlogComment.query.filter_by(blog_id=input_id, nlp_point=1).count()
    neg_num = TBlogComment.query.filter_by(blog_id=input_id, nlp_point=-1).count()
    z = abs(pos_num - neg_num)
    if pos_num > neg_num:
        return 1, z
    elif pos_num < neg_num:
        return -1, z
    else:
        return 0, z


@visualization.route('/column_all_top', methods=['GET'])
def column_all_top():
    music_lst = TMusic.query.all()
    score_lst = []
    for music in music_lst:
        music_item = {'name': music.title, 'value': song_score(music.music_Id, datetime.datetime.now())}
        score_lst.append(music_item)
    # 对score_lst按照value进行排序
    score_lst.sort(key=lambda x: x['value'], reverse=True)
    return score_lst[:10]


@visualization.route('/column_all_bottom', methods=['GET'])
def column_all_bottom():
    music_lst = TMusic.query.all()
    score_lst = []
    for music in music_lst:
        music_item = {'name': music.title, 'value': song_score(music.music_Id, datetime.datetime.now())}
        score_lst.append(music_item)
    # 对score_lst按照value进行排序
    score_lst.sort(key=lambda x: x['value'], reverse=True)
    return score_lst[-10:]


@visualization.route('/pie_all_positive', methods=['GET'])
def pie_all_positive():

    comment_lst = TComment.query.filter_by(nlp_point=1).all()
    # 统计comment_lst中每个music_id出现的次数
    music_dict = {}
    for comment in comment_lst:
        if comment.music_Id in music_dict:
            music_dict[comment.music_Id] += 1
        else:
            music_dict[comment.music_Id] = 1
    # 对music_dict按照value进行排序
    music_dict = sorted(music_dict.items(), key=lambda x: x[1], reverse=True)
    # 将music_dict中的value转换为百分比
    for music in music_dict:
        music[1] = music[1] / len(comment_lst)
    item_lst = []
    for music in music_dict:
        item_dict = {'name': TMusic.query.filter_by(music_Id=music[0]).first().title, 'value': music[1]}
        item_lst.append(item_dict)
        if len(item_lst) >= 5:
            item_lst.append({'name': 'Other', 'value': 1 - sum([i['value'] for i in item_lst])})
    return item_lst


@visualization.route('/pie_all_negative', methods=['GET'])
def pie_all_negative():
    comment_lst = TComment.query.filter_by(nlp_point=-1).all()
    # 统计comment_lst中每个music_id出现的次数
    music_dict = {}
    for comment in comment_lst:
        if comment.music_Id in music_dict:
            music_dict[comment.music_Id] += 1
        else:
            music_dict[comment.music_Id] = 1
    # 对music_dict按照value进行排序
    music_dict = sorted(music_dict.items(), key=lambda x: x[1], reverse=True)
    # 将music_dict中的value转换为百分比
    for music in music_dict:
        music[1] = music[1] / len(comment_lst)
    item_lst = []
    for music in music_dict:
        item_dict = {'name': TMusic.query.filter_by(music_Id=music[0]).first().title, 'value': music[1]}
        item_lst.append(item_dict)
        if len(item_lst) >= 5:
            item_lst.append({'name': 'Other', 'value': 1 - sum([i['value'] for i in item_lst])})
    return item_lst


@visualization.route('/pie_single', methods=['POST'])
def pie_single():
    id = request.json.get('id')
    comment_lst = TComment.query.filter_by(music_Id=id).all()
    # 统计comment_lst中nlp_point为1, 0, -1的占比
    pos_num = TComment.query.filter_by(music_Id=id, nlp_point=1).count()
    zero_num = TComment.query.filter_by(music_Id=id, nlp_point=0).count()
    neg_num = TComment.query.filter_by(music_Id=id, nlp_point=-1).count()
    score_list = [
        {'name': 'Positive', 'value': pos_num / len(comment_lst)},
        {'name': 'Neutral', 'value': zero_num / len(comment_lst)},
        {'name': 'Negative', 'value': neg_num / len(comment_lst)}
    ]
    return score_list
