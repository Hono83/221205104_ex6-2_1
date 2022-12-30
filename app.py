#!/usr/bin/env python3
# coding: utf-8


from flask import Flask, jsonify, request, render_template
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_root():
    return render_template('index.html')

@app.route('/calc_square/<number>', methods=['GET'])
def c_square(number):
    number = float(number)
    square_area = number ** 2 # 面積を計算
    
    circle_radius = number / 2 # 半径を計算
    circle_area = circle_radius ** 2 * 3.14 # 面積を計算
    
    output_dic = {"number":number, "square_area":square_area, "circle_area":circle_area}
    return jsonify(output_dic)

@app.route('/calc_square_app', methods=['GET'])
def calc_square_app():
    side = float(request.args["number"])
    square_area = side ** 2 # 面積を計算
    
    circle_radius = side / 2 # 半径を計算
    circle_area = circle_radius ** 2 * 3.14 # 面積を計算

    title = '1辺の長さが%sの正方形について' % (side)
    message = '正方形の面積: %s, 正方形に内接する円の面積: %s' % (square_area, circle_area)
    return render_template('kekka.html', 
        title = title, 
        message = message)

if __name__ == "__main__":
    app.run()




