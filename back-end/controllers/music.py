from app import app, db

from flask import Blueprint, request
from common.service import MessageHelper
from common.models import Music
import os
import re

music = Blueprint('music', __name__)


# get music id from the front end, and 'id.mp3' is the music name
# the role of this file is judging whether the file is existed
# 歌手，专辑，时长随便设一下
@music.route("/getMusicResource", methods=['POST'])
def getMusicResource():
    # get music_id from the request
    global music_filepath
    music_id = request.json.get('music_id')
    # music_id = '_uRC-ZabKhY'
    music_file = music_id + '.mp3'
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + '/../static/music/'
    # relative path of music in project
    file_name = 'back-end/static/music' + music_id + '.mp3'
    all_files = os.listdir(path)
    for i in all_files:
        if i == music_file:
            music_filepath = {"music_filepath": file_name}
        else:
            return MessageHelper.ops_renderErrJSON(msg="music doesn't exists.")


    try:
        music_info = Music.query.filter_by(video_Id=music_id).first()
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="")

    music_info = {'id': music_id, 'img': music_info.image_url, "url": music_filepath, 'name': music_info.title,
                  'albumId': '', 'albumName': '', 'artists': 'yang', 'duration': music_info.duration, 'durationSecond': '270', 'mvId': 1}
    return MessageHelper.ops_renderJSON(data=music_info)



# get musics from database and judge whether have their file in static
@music.route("/getAllMusicResources", methods=['GET'])
def getAllMusicResources():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + '/../static/music/'
    # relative path of music in project
    # print(path)
    all_files = os.listdir(path)
    music_list = []
    for i in all_files:
        x = re.findall(r'(.*?).mp3', i)
        music_list.append(x)
    # return all the music file name
    return MessageHelper.ops_renderJSON(data=music_list)
