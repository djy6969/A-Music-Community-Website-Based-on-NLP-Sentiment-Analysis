from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import paramiko

app = Flask(__name__, instance_relative_config=True)

# 默认silent = False，即当配置文件不存在时，抛出异常
app.config.from_pyfile("../common/config/base_setting.py", silent=False)

db = SQLAlchemy(app)

transport = paramiko.Transport('137.43.49.28', 22)

transport.connect(username='student', password='fianna-LDLYR?')

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh._transport = transport

# 启动管理
manager = Manager(app)


