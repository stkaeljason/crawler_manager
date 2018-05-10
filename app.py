from flask import Flask, render_template, jsonify
from flask_cors import CORS
from random import randint

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist"
            )
cors = CORS(app, resources={"/api/*": {"origins": "*"}})

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # 只需要vue写路由，flask捕捉到路由后交给vue处理
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
