from flask import Flask, render_template, request, session, redirect, url_for
from flask_socketio import SocketIO, join_room, leave_room
import sshtunnel
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config.from_pyfile("base_setting.py", silent=False)
# CORS(app, supports_credentials=True, cors_allowed_origins="*")
socketio = SocketIO(app, cors_allowed_origins='*', async_mode='threading')
socketio.init_app(app)

db = SQLAlchemy(app)


class TUser(db.Model):
    __tablename__ = 't_user'

    id = db.Column(db.SmallInteger, primary_key=True)
    username = db.Column(db.String(32, 'utf8_bin'), nullable=False, unique=True)
    password = db.Column(db.String(32, 'utf8_bin'), nullable=False)
    password_salt = db.Column(db.String(32, 'utf8_bin'))
    email = db.Column(db.String(32, 'utf8_bin'))
    tel = db.Column(db.String(11, 'utf8_bin'))
    nickname = db.Column(db.String(32, 'utf8_bin'), nullable=False)
    created_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    updated_time = db.Column(db.DateTime, server_default=db.FetchedValue())


class TChatroom(db.Model):
    __tablename__ = 't_friend'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # foreignKey需要放到nullable之前
    user_id = db.Column(db.SmallInteger,
                        db.ForeignKey(TUser.id, ondelete="CASCADE"), nullable=False)
    friend_id = db.Column(db.SmallInteger,
                          db.ForeignKey(TUser.id, ondelete="CASCADE"), nullable=False)
    room = db.Column(db.String(128, 'utf8_bin'), nullable=False, default='')
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())


online_user = []
room_user = {}


# @app.route('/chat/message/')
# def message():
#     username = request.values['username']
#     room = request.values['room']
#     if username != '' and room != '':
#         return render_template('chat.html', username=username, room=room)
#     else:
#         return redirect(url_for('index'))


@socketio.on('connect')
def handle_connect():
    username = 1
    # online_user.append(username)
    # print('connect info:  ' + f'{username}  connect')
    # print(username)
    # print(online_user)
    # socketio.emit('connect info', f'{username}  connect')
    # socketio.emit('connect', {'sd'})



# 断开连接
@socketio.on('disconnect')
def handle_disconnect(data):
    username = data['username']
    print('connect info:  ' + f'{username}  disconnect')
    # socketio.emit('connect info', f'{username}  disconnect')


@socketio.on('send_msg')
def handle_message(data):
    print('sendMsg' + str(data))
    room = data['room']
    data['message'] = data['message'].replace('<', '&lt;').replace('>', '&gt;').replace(' ', '&nbsp;')
    socketio.emit('send_msg', data, to=room)

@socketio.on('update_music')
def update_music(data):
    print(data)
    room = data['room']
    socketio.emit('update_music', data, to=room)

@socketio.on('play_music')
def playMusic(data):
    print(data)
    room = data['room']
    socketio.emit('play_music', data, to=room)


@socketio.on('pause_music')
def pauseMusic(data):
    print(data)
    room = data['room']
    socketio.emit('pause_music', data, to=room)


@socketio.on('resume_music')
def resumeMusic(data):
    print(data)
    room = data['room']
    socketio.emit('resume_music', data, to=room)


@socketio.on('invite')
def invite(data):
    print(data)
    room = data['room']
    socketio.emit('invite', data, to=room)


@socketio.on('join')
def on_join(data):
    # username = request.values['username']
    # room = request.values['room']
    username = data['username']
    room = data['room']
    try:
        room_user[room].append(username)
    except:
        room_user[room] = []
        room_user[room].append(username)

    join_room(room)
    print('join room:  ' + str(data))
    print(room_user)
    socketio.emit('connect info', username + 'Enter the Room', to=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    room_user[room].remove(username)
    # delete room in database if there are no user in this chatroom
    if (room_user[room].length() == 0):
        room_delete = TChatroom.query.get(room=room).first()
        db.session.delete(room_delete)
        db.session.commit()
    leave_room(room)
    print('leave room   ' + str(data))
    print(room_user)
    socketio.emit('connect info', username + 'Leave the Room', to=room)


if __name__ == '__main__':
    socketio.run(app, host='127.0.0.1', port=5004, debug=True)
