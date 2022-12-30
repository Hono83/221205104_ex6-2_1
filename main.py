#!/usr/bin/env python3
# coding: utf-8

import requests
import json

def main():
    square_edge = input('正方形1辺の長さを入力してください>') # 表示と入力
    square_edge = float(square_edge) # データ型の変換
    
    response = requests.get('http://127.0.0.1:5000/calc_square/{}'.format(square_edge))
    
    print(response.text)
    if response.status_code == 200:
        res_json = json.loads(response.text)
        
        number = float(res_json['number'])
        square_area = float(res_json['square_area'])
        circle_area = float(res_json['circle_area'])
    
        print('1辺の長さが{}の正方形について' .format(number))
        print('正方形の面積は:{}' .format(square_area))
        print('正方形に内接する円の面積は:{}' .format(circle_area))

if __name__ == '__main__':
    main()




