from flask import Blueprint, request
from common.nlp.nlp import sentient_analysis
from common.service import MessageHelper

comment = Blueprint("comment", __name__)

@comment.route('/single_comment_analysis', methods=['POST'])
def single_comment_analysis():
    comment = request.json.get('comment')
    score = sentient_analysis(comment)
    return MessageHelper.ops_renderJSON(data={'score': score})

