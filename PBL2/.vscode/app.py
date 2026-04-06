from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Your MySQL username
app.config['MYSQL_PASSWORD'] = 'yourpassword'  # Your MySQL password
app.config['MYSQL_DB'] = 'user_db'

mysql = MySQL(app)

@app.route('/')
def home():
    return "Flask + MySQL Connected Successfully!"

@app.route('/users', methods=['GET'])
def get_users():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
