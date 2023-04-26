from app import app, db

from common.models.Collection import TCollection
from flask import Blueprint, request, make_response

from common.models.Music import TMusic
from common.service import MessageHelper, UserHelper, CommonHelper

collection = Blueprint('collection', __name__)

# create new Collection, add music to a collection
@collection.route("/addMusicToCollection", methods=['POST'])
def addCollection():
    # get collectionName and musicId of music want to add into the collection and userId
    # every user only have one collection
    # collectionName = request.json.get('collectionName')
    musicId = request.json.get('musicId')
    userId = request.json.get('userId')

    # create a new TCollection object and insert information into it
    newCollection = TCollection()
    newCollection.video_Id = musicId
    # newCollection.collection_name = collectionName
    newCollection.userid = userId

    # add collection to database
    db.session.add(newCollection)
    db.session.commit()

    return MessageHelper.ops_renderJSON(msg="add new music to collection.")

@collection.route("/deleteMusicFromCollection", methods=['POST'])
def deleteMusicFromCollection():
    # every user only have one collection
    # collectionName = request.json.get('collectionName')
    musicId = request.json.get('musicId')
    userId = request.json.get('userId')

    # get collection
    getCollection = TCollection.query.fliter_by(user_id=userId, video_Id=musicId).first()

    # delete music from collection
    db.session.remove(getCollection)
    db.session.commit()

    return MessageHelper.ops_renderJSON()


@collection.route("/getMusicsFromCollection", methods=['POST'])
def getMusicsFromCollection():
    userId = request.json.get('userId')

    # get collection
    getCollections = TCollection.query.fliter_by(user_id=userId).all()

    collections = {}

    i = 0

    # get music info by video_Id and add music info to collections
    for getCollection in getCollections:
        music = TMusic.query.filter_by(video_Id= getCollection.video_Id).first()
        music_info = {'seq': i, 'id': music.video_Id, 'img': music.image_url,
                        "url": 'https://ipa-012.ucd.ie/music/' + music.video_Id + ".mp3",
                        'name': music.title, 'albumId': '', 'albumName': '',
                        'artists': music.artist, 'duration': music.duration,
                        'durationSecond': CommonHelper.convertMusicTime(music.duration), 'mvId': 0}
        collections[i] = music_info
        i += 1


    return MessageHelper.ops_renderJSON(data=collections)