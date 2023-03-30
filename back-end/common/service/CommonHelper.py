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
    return str(second) + ".00"

def getFolderFileCount(folder):
    sftp = paramiko.SFTPClient.from_transport(transport)
    # data = sftp.listdir('/home/group3/public_html/project/flask-back/static/img/{}'.format(folder))

    is_existence = True if folder in sftp.listdir('/home/student/comp3032j/data/image/') else False

    if not is_existence:
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
    sftp.putfo(file, '/home/student/comp3032j/data/image/{}/{}'.format(folder, name))
    return_name = '{}/{}'.format(folder, name)
    return return_name

if __name__ == "__main__":
    # sftp = paramiko.SFTPClient.from_transport(transport)
    # data = sftp.listdir('/home/student/comp3032j/data/image/1')
    uploadServerPic('D:\\2.jpg', '2')