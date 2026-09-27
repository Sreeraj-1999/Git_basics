from flask import Flask
import json


app=Flask(__name__)

@app.route('/api')
def read_data():
    with open("data.json",'r',encoding="utf-8") as file:
        data=json.load(file)
    print(data)

    return data

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port='8001')    