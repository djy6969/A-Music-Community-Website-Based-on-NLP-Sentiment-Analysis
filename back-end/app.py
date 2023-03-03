from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager


app = Flask(__name__, instance_relative_config=True)

# 默认silent = False，即当配置文件不存在时，抛出异常
app.config.from_pyfile("../common/config/base_setting.py", silent=False)

# 启动管理
manager = Manager(app)

# db = SQLAlchemy(app)

# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=5000, debug=True)

