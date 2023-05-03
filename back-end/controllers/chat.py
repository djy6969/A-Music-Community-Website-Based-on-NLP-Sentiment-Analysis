from app import db
from flask import Blueprint, request
# import openai
from common.service import MessageHelper
from common.models.Chatroom import TChatroom

#
chat = Blueprint('chat', __name__)


# openai.api_key = "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"
# @chat.route('/get_chat_response', methods=['POST'])
# def get_chat_response():
#     user_input = request.json.get('user_input')
#     song_name = request.json.get('song_name')
#     artist_name = request.json.get('artist_name')
#     # Connect to your database and get song information based on user input
#     # conn = psycopg2.connect(database="your_database", user="your_username", password="your_password", host="your_host", port="your_port")
#     # cursor = conn.cursor()
#     # cursor.execute("SELECT * FROM songs WHERE title ILIKE %s", ("%" + user_input + "%",))
#     # song_info = cursor.fetchone()
#
#     # Create a prompt using the song information
#
#     # prompt = f"What can you tell me about {song_info[1]} by {song_info[2]}?"
#
#     prompt = f"Answer below question based on the {song_name} by {artist_name}, if the question in not related to this song then return: 'It seems like the question is not related to this song, please try another one.'. The question is: {user_input}"
#
#     # Generate a response from ChatGPT
#     model_engine = "text-davinci-003"
#     response = openai.Completion.create(
#         engine=model_engine,
#         prompt=prompt,
#         max_tokens=1024,
#         n=1,
#         stop=None,
#         temperature=0.5,
#     )
#     message = response.choices[0].text.strip()
#
#     # Close the database connection and return the response
#     # cursor.close()
#     # conn.close()
#     return MessageHelper.ops_renderJSON(data=message)

# add a new chat room, need the front-end send the user_id and friend_id
# the room_id combines the user_id and friend_id
@chat.route('/add_chatroom', methods=['POST'])
def add_chatroom():
    user_id = request.json.get('user_id')
    friend_id = request.json.get('friend_id')
    room_id = user_id + friend_id
    chatroom = TChatroom()
    chatroom.user_id = user_id
    chatroom.friend_id = friend_id
    chatroom.room = room_id
    db.session.add(chatroom)
    db.session.commit()
    return MessageHelper.ops_renderJSON(
        msg="create a new chatroom",
        data={
            "id": chatroom.id,
            "chatroom_id": chatroom.room
        }
    )


@chat.route('/check_all_chatroom', methods=['POST'])
def check_all_chatroom():
    user_id = request.json.get('user_id')
    chatroom = TChatroom.query.filter_by(friend_id=user_id).first()
    if (chatroom is not None):
        room = {
            "id":chatroom.id,
            "chatroom_id": chatroom.room,
            "friend_id": chatroom.friend_id
        }
        return MessageHelper.ops_renderJSON(data=room)
    else:
        return MessageHelper.ops_renderJSON(msg="no chat!")
