from flask import Flask,request,render_template,jsonify
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/insert',methods=['POST'])
def index():
    connection = sqlite3.connect('database/ray.db')
    cursor = connection.cursor()

    username = request.form['dipta']
    password = request.form['dipta2']

    query = "Insert into users(username,password) values(?,?)"

    cursor.execute(query,(username,password))

    connection.commit()
    return "Data inserted successfully"




@app.route('/show_data',methods=['GET'])
def show_data():
    return render_template('showData.html')





@app.route('/get_db_data',methods=['GET'])
def show_db_data():
    connection = sqlite3.connect('database/ray.db')
    cursor = connection.cursor()

    query = "Select * from users"
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    return str(data)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5500)

   