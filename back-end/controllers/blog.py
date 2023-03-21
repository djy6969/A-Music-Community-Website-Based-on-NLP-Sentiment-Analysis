from flask import Blueprint,request
from common.models.Blog import TBlog

blog = Blueprint('blog', __name__)

@blog.route('/post_blog',methods=['POST'])
def post_blog():
    if request.method == "POST":
        text = request.form['text']
        images = request.form['picList']
        print(text)
        for image in images:
            image.show()
        return
