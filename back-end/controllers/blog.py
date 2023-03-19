from flask import Blueprint,request

blog = Blueprint('blog', __name__)

@blog.route('/post_blog',methods=['POST'])
def post_blog():
    if request.method == "POST":
        text = request.form.get('text')
        images = request.files.get('picList')
        print(text)
        print(images)
        for image in images:
            image.show()
        return
