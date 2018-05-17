#coding:utf-8

from flask import Blueprint
from flask import request
from flask import jsonify
from flask.views import MethodView


from models.img_user_model import ImgUser
from ext import db

statis_crawl = Blueprint('statis_crawl', __name__)


@statis_crawl.route('/statis_users',methods=['GET'])
def statis_crawled_users():
    is_crawled = request.args.get('is_crawled')
    im_counts_filter = request.args.get('im_counts')
    from_datetime = request.args.get('date')
    user_account = db.session.query(ImgUser).filter_by(im_counts_filter).count(ImgUser.id)
    print('useraccount:',user_account)
    result_dict = {'statis_result':user_account}
    return jsonify(result_dict)


class StatisUsersApi(MethodView):

    def get(self):
        is_crawled = request.args.get('is_crawled')
        im_counts_filter = request.args.get('im_counts_filter')
        from_datetime = request.args.get('from_datetime')
        user_account = db.session.query(ImgUser).filter_by(im_counts_filter).count(ImgUser.id)
        print('useraccount:', user_account)
        result_dict = {'statis_result': user_account}
        return jsonify(result_dict)



# statis_crawl.add_url_rule('/users_count', view_func=StatisUsersApi.as_view('users_count'))