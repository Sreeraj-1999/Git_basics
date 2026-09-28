from flask import Flask,request,render_template
from datetime import datetime
import requests
app=Flask(__name__)

BACKEND_URL='http://0.0.0.0:8004'

@app.route('/')
def home():
    day_of_week = datetime.now().strftime('%A')
    return render_template('index.html', day_of_week=day_of_week)

@app.route('/submit', methods=['POST'])
def submit():
    form_data=dict(request.form)
    print(request.form)
    print("form_data_dict///////",form_data)
    if form_data['password'] != form_data['confirm_password']:
        return render_template(
            'index.html',
            day_of_week=datetime.now().strftime('%A'),
            error="Passwords do not match"
        )

    # requests.post(BACKEND_URL + '/submit1',data=form_data)
    requests.post(BACKEND_URL + '/submit1',data=request.form)
    return 'Data submitted successfully'
@app.route('/view')
def view():
    response=requests.get(BACKEND_URL + '/view')
    data=response.json()
    print(data)
    return data


if __name__=='__main__':
    app.run(debug=True)