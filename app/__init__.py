# -*- coding: UTF-8 -*-
import numpy as np
import app.model as model

from flask import *
from flask_cors import CORS     

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html', data=None)  # data 默認為 None，首頁不顯示結果

@app.route('/predict', methods=['POST'])
def postInput():
        # 取得前端傳過來的數值
    
    x1 = request.form['sepalLengthCm']
    x2 = request.form['sepalWidthCm']
    x3 = request.form['petalLengthCm']
    x4 = request.form['petalWidthCm']
    input_data = np.array([[float(x1), float(x2), float(x3), float(x4)]])
    print(f"Received values: sepalLengthCm={x1}, sepalWidthCm={x2}, petalLengthCm={x3}, petalWidthCm={x4}")

    # 使用模型進行預測
    try:
        result = model.predict(input_data)
        prediction = f"預測結果為: {str(result)}"
    except Exception as e:
        prediction = f"發生錯誤: {e}"

    return render_template("index.html", data=prediction)
    

    
