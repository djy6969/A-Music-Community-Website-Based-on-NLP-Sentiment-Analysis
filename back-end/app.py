from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_cors import CORS
import paramiko
# from flask_socketio import SocketIO


app = Flask(__name__, instance_relative_config=True)

CORS(app, supports_credentials=True)

# 默认silent = False，即当配置文件不存在时，抛出异常
#
# /home/student/comp3032j/back-end/common/config/base_setting.py
# ../common/config/base_setting.py
app.config.from_pyfile("../common/config/base_setting.py", silent=False)

db = SQLAlchemy(app)

transport = paramiko.Transport('137.43.49.28', 22)

transport.connect(username='student', password='Ahkoh4queidiegho')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh._transport = transport

# socketio = SocketIO()
# socketio.init_app(app, cors_allow_origin='*')

# 启动管理
manager = Manager(app)



