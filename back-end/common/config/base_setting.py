# 基础通用配置文件

import sshtunnel

SECRET_KEY = 'fianna_11'

AUTH_COOKIE_NAME = 'Fianna_music_communicity'

ssh_host = "137.43.49.28"  # 堡垒机ip地址或主机名
ssh_port = 22  # 堡垒机连接mysql服务器的端口号，一般都是22，必须是数字
ssh_user = "student"  # 这是你在堡垒机上的用户名
ssh_password = "fianna-LDLYR?"  # 这是你在堡垒机上的用户密码
mysql_host = '127.0.0.1'  # 这是你mysql服务器的主机名或ip地址
mysql_port = 3306  # 这是你mysql服务器上的端口，3306，mysql就是3306，必须是数字
mysql_user = "root"  # 这是你mysql数据库上的用户名
mysql_password = "123456"  # 这是你mysql数据库的密码
mysql_db = "music"  # mysql服务器上的数据库名

server = sshtunnel.SSHTunnelForwarder(
        (ssh_host, ssh_port),
        ssh_username=ssh_user,
        ssh_password=ssh_password,
        remote_bind_address=(mysql_host, mysql_port)
)
server.start()
local_port = str(server.local_bind_port)

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'\
    .format(mysql_user, mysql_password, '127.0.0.1', local_port, mysql_db)
