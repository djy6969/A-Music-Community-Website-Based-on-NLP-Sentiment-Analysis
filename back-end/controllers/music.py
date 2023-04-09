from app import app, db

from flask import Blueprint, request
from common.service import MessageHelper, CommonHelper
from common.models.Music import TMusic

music = Blueprint('music', __name__)


# get music id from the front end, and 'id.mp3' is the music name
# the role of this file is judging whether the file is existed
# 歌手，专辑随便设一下
@music.route("/getMusicResource", methods=['POST'])
def getMusicResource():
    # get the number of music the frontend want
    num = request.json.get('num')
    music_info = TMusic.query.count()
    if num > music_info:
        return MessageHelper.ops_renderErrJSON(msg="the number of music is bigger than the total number of songs of our website.")
    # num = request.values['num']
    # get music_id from database order by publish_time
    try:
        music_info = TMusic.query.order_by(TMusic.publish_time.desc()).limit(num).all()
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="")

    # store music files into a list
    music_files = {}
    # get music
    for i in range(int(num)):
        music_i = music_info[i]
        music_id = music_i.video_Id
        music_file = music_id + '.mp3'

        # relative path of music in project
        music_file_path = 'https://ipa-012.ucd.ie/music/' + music_file

        print(music_i.publish_time)

        music_i_info = {'seq': i + 1, 'id': music_id, 'img': music_i.image_url, "url": music_file_path, 'name': music_i.title,
                      'albumId': '', 'albumName': '', 'artists': music_i.artist, 'duration': music_i.duration,
                      'durationSecond': CommonHelper.convertMusicTime(music_i.duration), 'mvId': 0}
        music_files[music_id] = music_i_info
    print(music_files)
    return MessageHelper.ops_renderJSON(data=music_files)



# get musics from database and judge whether have their file in static
# @music.route("/getAllMusicResources", methods=['GET'])
# def getAllMusicResources():
#     path = os.path.dirname(os.path.abspath(__file__))
#     path = path + '/../static/music/'
#     # relative path of music in project
#     # print(path)
#     all_files = os.listdir(path)
#     music_list = []
#     for i in all_files:
#         x = re.findall(r'(.*?).mp3', i)
#         music_list.append(x)
#     # return all the music file name
#     return MessageHelper.ops_renderJSON(data=music_list)
