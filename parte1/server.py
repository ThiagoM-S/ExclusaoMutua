from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

score = {
    'valor': 0
}

@app.route('/verScore',methods=['GET'])
def getScore():
    return jsonify(score)

@app.route('/aumentar/<valor>',methods=['GET'])
def getEmp(valor):
    newScore = score.update({'valor': valor})
    return jsonify(score)

if __name__ == '__main__':
    app.run()