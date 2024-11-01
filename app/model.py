import pickle
import gzip

with gzip.open('app/model/xgboost-iris.pgz', 'r') as f:
    xgboostModel = pickle.load(f)
    
# 將模型預測寫成一個 function 
def predict(input):
    pred=xgboostModel.predict(input)[0]
    return pred