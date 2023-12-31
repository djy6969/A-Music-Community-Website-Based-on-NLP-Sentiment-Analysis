from app import db

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
    # num = int(request.values['num'])
    music_info = TMusic.query.count()
    if num > music_info:
        return MessageHelper.ops_renderErrJSON(msg="the number of music is bigger than the total number of songs of our website.")
    # num = request.values['num']
    # get music_id from database order by publish_time
    try:
        # select all the usable music
        music_info = TMusic.query.filter_by(usable=1).order_by(TMusic.publish_time.desc()).all()
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="")

    # store music files into a list
    music_files = {}
    # get music
    for i in range(int(num)):
        music_i = music_info[i]
        music_id = music_i.music_Id
        music_file = music_id + '.mp3'

        # relative path of music in project
        music_file_path = 'https://ipa-012.ucd.ie/music/' + music_file

        print(music_i.title)
        print(music_i.publish_time)

        music_i_info = {'seq': i + 1, 'id': music_id, 'img': music_i.image_url, "url": music_file_path, 'name': music_i.title,
                      'albumId': '', 'albumName': '', 'artists': music_i.artist, 'duration': music_i.duration,
                      'durationSecond': CommonHelper.convertMusicTime(music_i.duration), 'mvId': 0}
        music_files[i] = music_i_info

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


# manage music usability, 0 is unusable, 1 is usable
# need the front-end send the music_id and send usability
@music.route("/manage_music_usability", methods=['POST'])
def manage_music_usability():
    music_id = request.json.get('music_id')
    usable = request.json.get('usability')
    music = TMusic.query.filter_by(music_Id=music_id).first()
    music.usable = usable
    db.session.commit()
    return MessageHelper.ops_renderJSON(msg="operation successfully.")

# add new music resources
# need the front-end sent a new music_Id, title, description, image, tags, artist, duration
@music.route("/add_new_music", methods=['POST'])
def add_new_music():
    # 获取参数

    image = request.files.get('image')
    music = request.files.get('music')
    music_id = request.values['music_id']
    title = request.values['title']
    description = request.values['description']
    artist = request.values['artist']
    duration = request.values['duration']

    # 传音乐文件，取得音乐文件路径
    CommonHelper.uploadServerMusic(music, music_id + '.mp3')

    # 传图片文件，取得图片文件路径
    image_path = 'https://ipa-012.ucd.ie/image/' + CommonHelper.uploadServerPic(image, 'music')
    print(image_path)

    # 添加Music到数据库
    music = TMusic()
    music.music_Id = music_id
    music.title = title
    music.description = description
    music.artist = artist
    music.duration = duration
    music.image_url = image_path
    db.session.add(music)
    db.session.commit()
    return MessageHelper.ops_renderJSON(msg="add music successfully.")


@music.route("/managerGetAllMusicResource", methods=['GET'])
def managerGetAllMusicResource():
    # get the number of music the frontend want
    # num = int(request.values['num'])
    music_count = TMusic.query.count()

    try:
        # select all the usable music
        music_info = TMusic.query.filter_by().order_by(TMusic.publish_time.desc()).all()
    except Exception as e:
        return MessageHelper.ops_renderErrJSON(msg="")

    # store music files into a list
    music_files = {}
    # get music
    for i in range(int(music_count)):
        music_i = music_info[i]
        music_id = music_i.music_Id
        music_file = music_id + '.mp3'

        # relative path of music in project
        music_file_path = 'https://ipa-012.ucd.ie/music/' + music_file

        print(music_i.title)
        print(music_i.publish_time)

        music_i_info = {'seq': i + 1, 'id': music_id, 'img': music_i.image_url, "url": music_file_path, 'name': music_i.title,
                      'albumId': '', 'albumName': '', 'artists': music_i.artist, 'duration': music_i.duration,
                      'durationSecond': CommonHelper.convertMusicTime(music_i.duration), 'mvId': 0, 'usable': music_i.usable}
        music_files[i] = music_i_info

    return MessageHelper.ops_renderJSON(data=music_files)
