from flask import Blueprint
from app import db

from flask import Blueprint, request
from common.service import MessageHelper, CommonHelper
from common.models.Music import TMusic

search = Blueprint('search', __name__)


@search.route("/searchMusic", methods=['POST'])
#     search music
#     the front-end need send me a search content
def searchMusic():
    searchContent = request.json.get('searchContent')
    musics = {}
    musics_info = TMusic.query.filter(TMusic.title.like('%{keyword}%'.format(keyword=searchContent))).order_by(
        TMusic.publish_time.desc()).all()
    for i in range(len(musics_info)):
        music_info = musics_info[i]
        music_id = music_info.video_Id
        music_file = music_id + '.mp3'

        # relative path of music in project
        music_file_path = 'http://ipa-012.ucd.ie/music/' + music_file

        music_i_info = {'seq': i, 'id': music_id, 'img': music_info.image_url, "url": music_file_path,
                        'name': music_info.title,
                        'albumId': '', 'albumName': '', 'artists': music_info.artist, 'duration': music_info.duration,
                        'durationSecond': CommonHelper.convertMusicTime(music_info.duration), 'mvId': 1}
        musics[music_id] = music_i_info
    return MessageHelper.ops_renderJSON(data=musics)
