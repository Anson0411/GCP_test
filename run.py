# -*- coding: UTF-8 -*-
from app import app

@app.route('/')
def index():
    return 'Flask API started'

if __name__ == '__main__':
    app.run(port=3000, debug=False)
    