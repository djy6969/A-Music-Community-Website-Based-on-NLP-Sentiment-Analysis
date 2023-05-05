import math
import pymysql
from sshtunnel import *
from app import db
from tqdm import tqdm
import datetime
import time
from flask import Blueprint, request
from common.service import MessageHelper, CommonHelper
from common.models.Comment import TComment
from common.models.Music import TMusic
from common.models.BlogComment import TBlogComment
from common.models.Blog import TBlog

visualization = Blueprint('visualization', __name__)


# song_list = ['-er1ZoYEFLQ', '-tPcc1ftj8E', '-wNSFmqhQsU', '04cHqPMD4So', '09R8_2nJtjg', '0F-XzhAMFAM', '0JXQdrjS-Ac',
#              '0QolgSt-JKo', '1GNOoi0seNg', '1jh9TTAhka0', '1KOj9Ttj9p8', '3P_FYbXdYZQ', '45vYLubtMXo', '4fSJq1OX_pY',
#              '5ovhzJ0VdOs', '6iseNlvH2_s', '6J_TnDnb8SM', '8gjNhJ7l7Mk', '8kQZHYbZkLs', '989-7xsRLR4', '9a9FV2stBP0',
#              '9cw-mcJwZ_A', '9hrQ4yYtjUY', '9IN_QXasarA', '9jK-NcRmVcw', '9llrYBIqg_k', 'A7q40ca0LgU', 'AIksM4DTl-I',
#              'aMCNWhCx4eI', 'CA5CwZ4Nmnk', 'Ct6BUPvE2sM', 'DOJE9wE64No', 'dOjQ9PxkYFM', 'dQw4w9WgXcQ', 'eNiw3EtVq-w',
#              'fl6jdVdm6go', 'fOlYPHy9J5o', 'fW7X3FBNmrQ', 'fy8yftMkb8M', 'gAotCGoKhD0', 'gcEbrwHnmWY', 'gEPmA3USJdI',
#              'gsFSYIkCLC8', 'h-e6nlLsj5A', 'h-nkfAj5woE', 'H4OWyG6k2sY', 'hlnsIlEFGYI', 'hTWKbfoikeg', 'hxVT-GYnjjw',
#              'h_D3VFfhvs4', 'IJNR2EpS0jw', 'iM2S4cw-4VQ', 'iQlVf6LVr88', 'j5ZOwyhrevg', 'jALi8gYi7Gw', 'jHtC_LyIOKA',
#              'jIZadPWm7VM', 'k38GYko6imI', 'k521ij9DfXA', 'k85mRPqvMbE', 'LDAGVftLS1w', 'lXY49Vds4Rc', 'lyHL2o5ztsE',
#              'm6Ruks5rRio', 'mC9cLPyzwKo', 'MlWDQYR7yH0', 'MPmYh1iSohI', 'MQftzFOYUJc', 'MxMNwnlO9bI', 'OGACI56J34A',
#              'Ou57jsJVWy8', 'OZ3UuZdUHZc', 'p47fEXGabaY', 'PAC6aZlf994', 'pGW3zyk4GD4', 'PivwSBkhA3s', 'PrGsAMbgUh4',
#              'q2lvbv2f4Lg', 'Q7LVVfk070A', 'qa-VN_oEa24', 'QFshBEOBXyY', 'Quqh-1z4H7w', 'quXwZ_zmjNM', 'RWHVh3PlO7I',
#              'S32A68Zm6KY', 'S5tfNBxl5wE', 'seO_MZ16aUw', 'sFMMp0JSnA0', 'SlPFfbS25Bo', 'SM-FehTxG9o', 'Sm_DVsixxsk',
#              't0a7b_QHA24', 'T60zhmAaZi8', 'tcc37xJou3U', 'tEYuWFdKIn0', 'uacbJIL1C1c', 'ufnJwBV76iw', 'VdbxP5ACvFY',
#              'vPNyLUJkZNI', 'VSOnIahWAs4', 'wWBQkUfsdhs', 'xcc2bwx2AWA', 'xp0AQgesIu8', 'xQd4wQhnwbk', 'xqVnN-SPl90',
#              'xVMOu5DlPGA', 'xwI8pYCRTcU', 'yAqjR3wS44I', 'ygf2uiEUg64', 'z2vCOR51v34', 'z4f5FBSBybU', 'z715VTEkY6E',
#              'ZjD2VqBDSF4', '_uRC-ZabKhY']


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
    # music = TMusic()
    # comment = TComment()
    # song_title = TMusic.query.filter_by(music_Id=input_id).first().title
    music = TMusic.query.filter_by(music_Id=input_id).first()
    view_count = music.view_count
    like_count = music.like_count
    pub_time = music.publish_time
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
    score = round(score, 3)
    music.score = score
    db.session.commit()
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
    score = round(score, 3)

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


def datetime_split(publish_time, now_time):
    # 获取时间差
    time_delta = now_time - publish_time
    # 获取时间差的秒数
    time_delta_seconds = time_delta.total_seconds()
    # 获取时间差的小时数
    time_delta_hours = time_delta_seconds // 3600
    datetime_list = []
    for i in range(0, 11):
        # 获取从publish_time开始经过i*(time_delta_hours/10)小时后的时间表示为datetime格式
        datetime_list.append(publish_time + datetime.timedelta(hours=i * (time_delta_hours / 10)))
    return datetime_list


def get_score_by_time(comment_list, time_list):
    score_list = []
    score = 0
    for i in range(0, 10):
        for comment in comment_list:
            if time_list[i] <= comment.publish_time < time_list[i + 1]:
                score += comment.nlp_point
        score_list.append(score)
    score_list.append(get_all_score(comment_list))
    return score_list


@visualization.route('/blog_rank', methods=['GET'])
def blog_rank():
    blog_lst = TBlog.query.all()
    score_lst = []
    for blog in tqdm(blog_lst):
        blog_item = {'id': blog.id, 'content': blog.blog_content, 'publish_time': blog.publish_time, 'score': blog_score(blog.id)}
        score_lst.append(blog_item)

    # 对score_lst按照score进行排序
    score_lst.sort(key=lambda x: x['score'], reverse=True)
    return_list = []
    for i in range(0, 10):
        return_list.append(score_lst[i])
    return MessageHelper.ops_renderJSON(data=return_list)


@visualization.route('/rank_list', methods=['GET'])
def rank_list():
    music_lst = TMusic.query.all()
    score_lst = []
    i = 0
    for music in tqdm(music_lst):
        music_file_path = 'https://ipa-012.ucd.ie/music/' + music.music_Id + '.mp3'
        music_item = {'id': music.music_Id, 'img': music.image_url, "url": music_file_path,
                      'name': music.title,
                      'albumId': '', 'albumName': '', 'artists': music.artist, 'duration': music.duration,
                      'durationSecond': CommonHelper.convertMusicTime(music.duration), 'mvId': 0, 'value': music.score}
        score_lst.append(music_item)

    # 对score_lst按照value进行排序
    score_lst.sort(key=lambda x: x['value'], reverse=True)
    return_list = score_lst[:10]
    i = 1
    for item in return_list:
        item['seq'] = i
        i += 1
    return MessageHelper.ops_renderJSON(data=return_list)


@visualization.route('/update_score', methods=['GET'])
def update_score():
    music_lst = TMusic.query.all()
    for song in tqdm(music_lst):
        song_score(song.music_Id, datetime.datetime.now())
    return MessageHelper.ops_renderJSON(msg='Update Success')


@visualization.route('/column_all_top', methods=['GET'])
def column_all_top():
    music_lst = TMusic.query.all()
    score_lst = []
    for music in tqdm(music_lst):
        music_item = {'name': music.title, 'value': music.score}
        score_lst.append(music_item)
    # 对score_lst按照value进行排序
    score_lst.sort(key=lambda x: x['value'], reverse=True)
    return MessageHelper.ops_renderJSON(data=score_lst[:10])


@visualization.route('/column_all_bottom', methods=['GET'])
def column_all_bottom():
    music_lst = TMusic.query.all()
    score_lst = []
    for music in tqdm(music_lst):
        music_item = {'name': music.title, 'value': music.score}
        score_lst.append(music_item)
    # 对score_lst按照value进行排序
    score_lst.sort(key=lambda x: x['value'], reverse=True)
    return MessageHelper.ops_renderJSON(data=score_lst[-10:])


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
    top_list = []
    for music in music_dict:
        if len(top_list) < 5:
            music_item = {'name': TMusic.query.filter_by(music_Id=music[0]).first().title,
                          'value': music[1] / len(comment_lst)}
            top_list.append(music_item)
        if len(top_list) >= 5:
            top_list.append({'name': 'Other', 'value': 1 - sum([i['value'] for i in top_list])})
            break
    # item_lst = []
    # for music in music_dict:
    #     item_dict = {'name': TMusic.query.filter_by(music_Id=music[0]).first().title, 'value': music[1]}
    #     item_lst.append(item_dict)

    return MessageHelper.ops_renderJSON(data=top_list)


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
    top_list = []
    for music in music_dict:
        if len(top_list) < 5:
            music_item = {'name': TMusic.query.filter_by(music_Id=music[0]).first().title,
                          'value': music[1] / len(comment_lst)}
            top_list.append(music_item)
        if len(top_list) >= 5:
            top_list.append({'name': 'Other', 'value': 1 - sum([i['value'] for i in top_list])})
            break
    return MessageHelper.ops_renderJSON(data=top_list)


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
    return MessageHelper.ops_renderJSON(data=score_list)


@visualization.route('/line_score', methods=['POST'])
def line_score():
    id = request.json.get('id')
    music = TMusic.query.filter_by(music_Id=id).first()
    comment = TComment.query.filter_by(music_Id=id).all()
    pub_time = music.publish_time
    time_list = datetime_split(pub_time, datetime.datetime.now())
    qscore_list = get_score_by_time(comment, time_list)
    view_count = music.view_count
    like_count = music.like_count
    score_list = [0]
    for i in range(1, 11):
        view_temp = view_count * (i / 10)
        like_temp = like_count * (i / 10)
        qupdated = TComment.query.filter(TComment.music_Id == id, TComment.publish_time <= time_list[i]).order_by(
            TComment.publish_time.desc()).first()
        if qupdated is not None:
            qupdated = qupdated.publish_time
        else:
            qupdated = pub_time
        qscore = qscore_list[i]
        qanswer = len(comment)
        qviews = view_temp
        ascore = like_temp
        qage = pub_time
        qage_day = (time_list[i] - qage).total_seconds() / (3600 * 24)
        qupdated_day = (time_list[i] - qupdated).total_seconds() / (3600 * 24)
        score = float((math.log(qviews, 10) * 4 + (qanswer * qscore) /
                       5 + ascore) / math.pow((1 + qage_day / 2 + qupdated_day / 2), 1.5))
        #对score保留三位小数
        score = round(score, 3)
        score_list.append(score)
    label_list = []
    for t in time_list:
        t = t.strftime("%Y-%m-%d %H:%M:%S")
        t = t[:10]
        label_list.append(t)
    fianl_json = [
        {'name': 'label', 'data': label_list},
        {'name': 'score', 'data': score_list}
    ]
    return MessageHelper.ops_renderJSON(data=fianl_json)


@visualization.route('/line_sentiment', methods=['POST'])
def line_sentiment():
    id = request.json.get('id')
    pub_time = TComment.query.filter_by(music_Id=id).order_by(TComment.publish_time).first().publish_time
    time_list = datetime_split(pub_time, datetime.datetime.now())
    pos_list, neu_list, neg_list = [], [], []
    for i in range(0, 11):
        pos_num = TComment.query.filter(TComment.music_Id == id, TComment.nlp_point == 1, TComment.publish_time <= time_list[i]).count()
        neu_num = TComment.query.filter(TComment.music_Id == id, TComment.nlp_point == 0, TComment.publish_time <= time_list[i]).count()
        neg_num = TComment.query.filter(TComment.music_Id == id, TComment.nlp_point == -1, TComment.publish_time <= time_list[i]).count()
        pos_list.append(pos_num)
        neu_list.append(neu_num)
        neg_list.append(neg_num)
    label_list = []
    for t in time_list:
        t = t.strftime("%Y-%m-%d %H:%M:%S")
        t = t[:10]
        label_list.append(t)
    final_json = [
        {'name': 'label', 'data': label_list},
        {'name': 'positive', 'data': pos_list},
        {'name': 'neutral', 'data': neu_list},
        {'name': 'negative', 'data': neg_list}
    ]
    return MessageHelper.ops_renderJSON(data=final_json)


@visualization.route('/get_music_info', methods=['GET'])
def get_music_info():
    music_list = TMusic.query.all()
    info_list = []
    for music in music_list:
        music_item = {'value': music.music_Id, 'label': music.title}
        info_list.append(music_item)
    # music_file_path = 'https://ipa-012.ucd.ie/music/' + music.music_Id + '.mp3'
    # music_item = {'id': music.music_Id, 'img': music.image_url, "url": music_file_path,
    #               'name': music.title,
    #               'albumId': '', 'albumName': '', 'artists': music.artist, 'duration': music.duration,
    #               'durationSecond': CommonHelper.convertMusicTime(music.duration), 'mvId': 0}
    return MessageHelper.ops_renderJSON(data=info_list)
