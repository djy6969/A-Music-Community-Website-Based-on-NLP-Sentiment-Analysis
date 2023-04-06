from flask import Blueprint, request
import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__)) # 获取当前目录
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir)) # 获取上级目录

sys.path.append(parent_dir_path)

from common.nlp.predict_cloud import model_creation, predict
from common.service import MessageHelper


homepage = Blueprint("homepage", __name__)

@homepage.route('/', methods=['GET'])
# homepage会和系统默认字符重复
def home_page():
    return "hello, world!"



@homepage.route('/nlp_creation', methods=['GET'])
# homepage会和系统默认字符重复
def nlp_creation():
    model_creation('/home/student/comp3032j/nlp/best_model')
    return MessageHelper.ops_renderJSON(msg='work!')


@homepage.route('/nlp_predict', methods=['POST'])
# homepage会和系统默认字符重复
def nlp_predict():
    text = request.json.get('text')
    return MessageHelper.ops_renderJSON(data={'result': predict(text)})