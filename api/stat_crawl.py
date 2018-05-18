#coding:utf-8

from flask import Blueprint
from flask import request
from flask import jsonify
from flask.views import MethodView


from models.img_user_model import ImgUser
from ext import db
from utils import time_to_timestamp
from sqlalchemy import text


statis_crawl = Blueprint('statis_crawl', __name__)


@statis_crawl.route('/statis_users',methods=['GET'])
def statis_crawled_users():
    filter_list = []
    is_crawled = request.args.get('is_crawled')
    if is_crawled:
        filter_is_crawled = 'is_crawled=%s'%is_crawled
        filter_list.append(filter_is_crawled)

    left_im_counts= request.args.get('left_im_counts')
    if left_im_counts:
        filter_left_im_counts = 'image_counts>%s'%left_im_counts
        filter_list.append(filter_left_im_counts)

    right_im_counts = request.args.get('right_im_counts')
    if right_im_counts:
        filter_right_im_counts= 'image_counts<%s'%right_im_counts
        filter_list.append(filter_right_im_counts)

    date = request.args.get('date').strip()
    time = request.args.get('time').strip()
    start_time = time_to_timestamp(date+' '+time)
    if start_time:
        filter_start_time = 'crawled_time>%s'%start_time
        filter_list.append(filter_start_time)

    filter_and = ' and '.join(filter_list)
    # print('filter_and:',filter_and)

    user_account = db.session.query(ImgUser).filter(text(filter_and)).count()
    # print('useraccount:',user_account,type(user_account))
    result_dict = {'statis_result':user_account}
    return jsonify(result_dict)


# class StatisUsersApi(MethodView):
#
#     def get(self):
#         is_crawled = request.args.get('is_crawled')
#         im_counts_filter = request.args.get('im_counts_filter')
#         from_datetime = request.args.get('from_datetime')
#         user_account = db.session.query(ImgUser).filter_by(im_counts_filter).count(ImgUser.id)
#         print('useraccount:', user_account)
#         result_dict = {'statis_result': user_account}
#         return jsonify(result_dict)

# statis_crawl.add_url_rule('/users_count', view_func=StatisUsersApi.as_view('users_count'))