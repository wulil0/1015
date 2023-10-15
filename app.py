# app.py

from flask import Flask, render_template, jsonify
import utils
import json

app = Flask(__name__)

# 模拟数据，实际中从数据库或其他数据源获取
data = {"message": "Hello Flask!"}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/get_data", methods=["GET"])
def get_data():
    # 将数据以JSON格式发送给前端
    return jsonify(data)

@app.route("/get_top10_1", methods=["GET"])
def get_top10_1():
    # 将数据以JSON格式发送给前端
    gnmk,gnx,mknum,xnum = utils.get_top10_1()
    data = json.dumps(dict(zip(gnmk,mknum)))
    data2 = json.dumps(dict(zip(gnx,xnum)))
    # print(data)
    return jsonify(data,data2)
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=2333)
