import re, os
import paramiko
from app import transport
'''
the format of music time in database is minute:second
the front-end need pure second time, format second.00
'''
def convertMusicTime(time):
    time = re.split(":", time)
    second = int(time[0]) * 60 + int(time[1])
    return "%.3f" % float(str(second))

def getFolderFileCount(folder):
    sftp = paramiko.SFTPClient.from_transport(transport)
    # data = sftp.listdir('/home/group3/public_html/project/flask-back/static/img/{}'.format(folder))

    is_existence = True if folder in sftp.listdir('/home/student/comp3032j/data/image/') else False



    if not is_existence:
        # /home/student/comp3032j/data/image
        sftp.mkdir('/home/student/comp3032j/data/image/{}'.format(folder))
        return 0
    else:
        data = sftp.listdir('/home/student/comp3032j/data/image/{}'.format(folder))
        return len(data)

def uploadServerPic(file, folder):
    count = str(getFolderFileCount(folder) + 1)
    name = '{}-{}.jpg'.format(folder, count)
    print(name)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # sftp.put(path, '/home/group3/public_html/project/flask-back/static/img/{}/{}'.format(folder, name))
    # a = request.files.get('file')
    print(type(file))
    # 本地用路径传文件使用put方法，接收前端传递的文件用putfo
    sftp.putfo(file, '/home/student/comp3032j/data/image/{}/{}'.format(folder, name))
    return_name = '{}/{}'.format(folder, name)
    return return_name

# 向服务器传递音乐/home/student/comp3032j/data/music/
# filename是music_id
def uploadServerMusic(file, filename):
    sftp = paramiko.SFTPClient.from_transport(transport)
    sftp.putfo(file, '/home/student/home/student/comp3032j/data/music/{}'.format(filename))
