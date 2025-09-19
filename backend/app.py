from flask import Flask, jsonify
import mysql.connector
import os 
app = Flask(__name__)

def get_db_connection():    
    connection = mysql.connector.connect(
        host=os.environ["DB_HOST"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        database=os.environ["DB_NAME"]
    return connection

@app.route("/")
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM users")
    result = cursor.fetchall()
    conn.close()

    users = [row[0] for row in result]
    return jsonify({"users": users})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
