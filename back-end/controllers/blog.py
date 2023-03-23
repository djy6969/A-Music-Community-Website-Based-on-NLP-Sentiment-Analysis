from flask import Blueprint,request
from common.models.Blog import TBlog
from interceptors.Auth import auth

blog = Blueprint('blog', __name__)

@blog.route('/post_blog',methods=['POST'])
@auth.login_required()
def post_blog():
    if request.method == "POST":
        text = request.form['text']
        picNum = request.form['picNumber']
        images = []
        for i in range(int(picNum)):
            images = request.form['picList'][i]


        print(text)
        return
