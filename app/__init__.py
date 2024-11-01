# -*- coding: UTF-8 -*-
import numpy as np
import app.model as model

from flask import Flask, request, jsonify
from flask_cors import CORS     

app = Flask(__name__)
CORS(app)

@app.route('/predict', method=['POST'])
def postInput():
        # 取得前端傳過來的數值
    insertValues = request.get_json()
    x1=insertValues['sepalLengthCm']
    x2=insertValues['sepalWidthCm']
    x3=insertValues['petalLengthCm']
    x4=insertValues['petalWidthCm']
    input = np.array([[x1, x2, x3, x4]])
    
    result = model.predict(input)
    
    return jsonify({'result':str(result)})
    

if __name__ == '__main__':
    app.run(port=3000, debug=True)
