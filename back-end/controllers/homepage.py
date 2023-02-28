from flask import Blueprint

homepage = Blueprint("homepage", __name__)

@homepage.route('/', methods=['GET'])
# homepage会和系统默认字符重复
def home_page():
    return "hello, world!"
