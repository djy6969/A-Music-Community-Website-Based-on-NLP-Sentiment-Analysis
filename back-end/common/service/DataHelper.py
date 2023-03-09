'''
操作数据Helper
'''
import os, re, json
from common.models.Music import TMusic
from common.models.Comment import TComment
from app import db

# find json file function
def find_json_files(data_type):
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + '/../../static/data/' + data_type
    all_files = os.listdir(path)
    json_list = []
    for i in all_files:
        x = re.findall(r'(.*?).json', i)
        if len(x) != 0:
            json_list.append(path + '/' + i)
    return json_list

# load json data to a data list, the json file can only contain one json data
def load_single_data_from_jsons(data_type):
    json_list = find_json_files(data_type)
    data_list = []
    for filepath in json_list:
        with open(filepath) as f:
            data = json.load(f)
            data_list.append(data)
    return data_list

# load json data to a data list, the json file can contain numerous json data
def load_datas_from_json(data_type):
    json_list = find_json_files(data_type)
    data_list = []
    for filepath in json_list:
        with open(filepath) as f:
            data = json.load(f)
            # print(data)
            data_list.append(data)
    return data_list


# load json file data to Tmusic table
def load_json_data_to_Tmusic(data_list):
    for data in data_list:
        music = TMusic()
        print(data)
        data_info = re.split('T|Z', data[0].get("publishedAt"))
        datatime = data_info[0] + ' ' + data_info[1]
        music.video_Id = data[0].get("videoId")
        music.publish_time =datatime
        music.title = data[0].get("title")
        music.description = data[0].get("description")
        music.like_count = data[0].get("likeCount")
        music.view_count = data[0].get("viewCount")
        music.image_url = data[0].get("thumbnailsURL")
        music.tags = data[0].get("tags")
        db.session.add(music)
    db.session.commit()


# load json file data to Tcomment table
def load_json_data_to_Tcomment(data_list):
    for i in range(len(data_list)):
        data = data_list[i]
        print(i)
        print('start!')
        # print(len(data))
        for j in range(len(data)):
            print(j)
            t_comment = TComment()
            data_single = data[j]
            # print(data)
            data_info = re.split('T|Z', data_single.get("publishtime"))
            datatime = data_info[0] + ' ' + data_info[1]
            t_comment.video_Id = data_single.get("videoId")
            t_comment.author = data_single.get("author")
            t_comment.publish_time = datatime
            t_comment.like_count = data_single.get("likeCount")
            t_comment.comment = data_single.get("comment")
            db.session.add(t_comment)
            if j % 500 == 0 or j == len(data):
                db.session.commit()

if __name__ == "__main__":
    load_json_data_to_Tcomment(load_datas_from_json('comment'))

