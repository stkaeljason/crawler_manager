#coding:utf-8
from random import randint

from flask import Flask, render_template, jsonify
from flask_cors import CORS

from ext import db

import config
import utils

from api.stat_crawl import statis_crawl

def create_app():
    app = Flask(__name__,
                static_folder="./dist/static",
                template_folder="./dist"
                )
    if utils.is_dev():
        app.config.from_object(config.DevelopmentConfig)
    else:
        app.config.from_object(config.ProductionConfig)
    db.init_app(app)

    app.register_blueprint(statis_crawl, url_prefix='/statis')

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        # 只需要vue写路由，flask捕捉到路由后交给vue处理
        return render_template("index.html")

    return app

app = create_app()

cors = CORS(app, resources={"/api/*": {"origins": "*"}})


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
