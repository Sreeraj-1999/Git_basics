from flask import Flask,request
import os
from dotenv import load_dotenv
load_dotenv()
import pymongo

MONGO_URL=os.getenv('MONGO_URL')
print(MONGO_URL)
client=pymongo.MongoClient(MONGO_URL)

db=client.test

collection=db['flask-tutorial']

app=Flask(__name__)

@app.route('/submit1',methods=['POST'])
def submit():
    form_data=dict(request.form)
    print(request.form)
    print("//// form_data_dict ///////",form_data)
    try:
        collection.insert_one(form_data)
        return "Data Submitted successfully"

    except Exception as e:
        return f"Error: {e}"

@app.route('/view')
def view():
    data=collection.find()

    print(data)

    stuff=[]

    for item in data:
        print(item)
        item.pop('_id')
        stuff.append(item)
    
    print(stuff)
    
    # del stuff['_id']    

    return stuff

if __name__=='__main__':
    app.run(host='0.0.0.0',port='8004',debug=True)

