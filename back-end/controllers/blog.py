
from flask import Blueprint,request
from pyarrow import BufferReader

from common.models.Blog import TBlog
from common.models.User import TUser
from common.models.BlogComment import TBlogComment
from app import db
from common.service import MessageHelper, CommonHelper
from interceptors.Auth import auth

blog = Blueprint('blog', __name__)

@blog.route('/post_blog',methods=['POST'])
# @auth.login_required()
# need get user_id, text, pictureNum and pictureList from the front-end
def post_blog():
    user_id = request.values['user_id']
    text = request.values['text']
    picNum = request.values['picNumber']
    print(picNum)
    images = []
    for i in range(int(picNum)):
        name = 'picList['+str(i)+"]"
        image = request.files.get(name)
        pic_name = CommonHelper.uploadServerPic(image, user_id)
        print(pic_name)
        images.append("https://137.43.49.28/image/" + pic_name)
    blog = TBlog()
    blog.user_id = user_id
    blog.blog_content = text
    blog.piclist = images
    blog.likes = 0
    db.session.add(blog)
    db.session.commit()

    return MessageHelper.ops_renderJSON(msg='Post blog successfully.')

@blog.route('/get_all_blogs', methods=['GET'])
# @auth.login_required()
# get all blogs
# the front-end need post a user_id
# read all information from database
#       id, user_id, blog_content, piclist, publish_time
def get_all_blogs():
    # status = 1 表示公开， status = 0 表示删除， status = 2 表示私密
    blogs_data_info = TBlog.query.filter_by(state=1).order_by(TBlog.publish_time.desc()).all()
    blogs_info = []
    for blog_data_info in blogs_data_info:
        user = TUser.query.filter_by(id=blog_data_info.user_id).first()
        blog_info = {
            'id': blog_data_info.id,
            'user_id': blog_data_info.user_id,
            'username': user.username,
            'blog_content': blog_data_info.blog_content,
            'publish_time': blog_data_info.publish_time,
            'head': user.head,
            'picList': blog_data_info.piclist}
        blogs_info.append(blog_info)

    print(blogs_info)
    return MessageHelper.ops_renderJSON(data=blogs_info)

@blog.route('get_user_blog', methods=['POST'])
# get user all blogs
# need the front-end post an userid
def get_usr_blog():
    userid = request.json.get('userid')
    blogs_data_info = TBlog.query.filter_by(user_id=userid).order_by(TBlog.publish_time.desc()).all()
    blogs_info = []
    for blog_data_info in blogs_data_info:
        user = TUser.query.filter_by(id=blog_data_info.userid).first()
        blog_info = {'id': blog_data_info.id, 'user_id': blog_data_info.userid, 'username': user.username,
                     'blog_content': blog_data_info.blog_content,
                     'publish_time': blog_data_info.publish_time, 'picList': blog_data_info.piclist, 'status': blog_data_info.state}
        blogs_info.append(blog_info)

    print(blogs_info)
    return MessageHelper.ops_renderJSON(data=blogs_info)


# update user blog state
# need the front-end send a blog_id and new blog state
# 1 is public, 2 is private, 3 is deleted
@blog.route('/update_blog_state', methods=['POST'])
def update_blog_state():
    blog_id = request.json.get('blog_id')
    state = request.json.get('state')
    blog = TBlog.query.filter_by(blog_id=blog_id).first()
    blog.state = state
    db.session.update(blog)
    db.session.commit()
    return MessageHelper.ops_renderJSON()

@blog.route('get_blog_comments', methods=['POST'])
# get comments for one blog
# need the front-end send blog_id
def get_blog_comments():
    blogid = request.json.get('blogid')
    blog_comments = TBlogComment.query.filter_by(blog_id=blogid).order_by(TBlogComment.publish_time.desc()).all()
    comments = []
    for blog_comment in blog_comments:
        user = TUser.query.filter_by(id=blog_comment.user_id).first()
        comment = {'id': blog_comment.id, 'user_id': blog_comment.user_id, 'username': user.username,
                   'content': blog_comment.content}
        comments.append(comment)

    return MessageHelper.ops_renderJSON(data=comments)

@blog.route('post_blog_comment', methods=['POST'])
# post a comment for one blog
# need the front-end send user_id, blog_id, and comment_content
def post_blog_comment():
    user_id = request.json.get('user_id')
    blog_id = request.json.get('blog_id')
    comment_content = request.json.get('comment_content')

    blog_comment = TBlogComment()
    blog_comment.user_id = user_id
    blog_comment.blog_id = blog_id
    blog_comment.content = comment_content
    db.session.add(blog_comment)
    db.session.commit()

    return MessageHelper.ops_renderJSON(msg='Post blog comment successfully.')


# delete blog comment by blog comment_id
# need the front-end send the comment_id
@blog.route('delete_blog_comment', methods=['POST'])
def delete_blog_comment():
    comment_id = request.json.get('commentid')
    blog_comment = TBlogComment.query.filter_by(id=comment_id).first()
    db.session.delete(blog_comment)
    db.session.commit()
    return MessageHelper.ops_renderJSON()