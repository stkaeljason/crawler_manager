#coding:utf-8

from flask import flash, current_app, request, redirect, url_for, Blueprint, jsonify
import flask_login
from flask_login import login_required, user_logged_in, login_user, current_user
from flask_login.utils import _get_user
from ext import db
from models.user import User
# from app import app

# user_logged_in.send(current_app._get_current_object(), user=_get_user())
b_login = Blueprint('b_login', __name__)


# login_manager.init_app()



# @flask_login.user_logged_in.connect_via(app)
# def _track_logins(sender, user, **extra):
#     user.login_count +=1
#     user.last_login_ip = request.remote_addr
#     db.session.add(user)
#     db.session.commit()
#
# @login_manager.user_loader
# def user_loader(id):
#     user = User.query.filter_by(userid=id).first()
#     return user


@b_login.route('/signin', methods=['POST'])
def signin():
    username = request.form.get('username')
    print('*******', request.values)
    print('uname', username)
    password = request.form.get('password')
    print('pwd', password)
    if username and password:
        user = User.query.filter_by(username=username).first()
        if user:
            if password == user.password:
                login_user(user)
                return jsonify({'status_code':200, 'msg':'登录成功'})
            else:
                return jsonify({'status_code': 401, 'msg': '密码错误，请重新输入'})
        else:
            return jsonify({'status_code': 402, 'msg':'用户不存在'})
    else:
        return jsonify({'status_code': 400, 'msg': '密码或用户名不能为空'})


@b_login.route('/regist', methods=['POST'])
def regist():
    pass


@b_login.route('/logout', methods=['POST'])
def logout():
    pass