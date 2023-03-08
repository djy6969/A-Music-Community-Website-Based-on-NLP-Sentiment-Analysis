'''
操作数据Helper
'''
import os, re

# 将json数据导入Mysql
def load_data_from_json():
    path = os.path.dirname(os.path.abspath(__file__))
    path = path + '/../..'
    all_files = os.listdir(path)
    print(all_files)
    json_list = []
    for i in all_files:
        x = re.findall(r'(.*?).json', i)
        json_list.append(x)
    print(json_list)


if __name__ == "__main__":
    load_data_from_json()

