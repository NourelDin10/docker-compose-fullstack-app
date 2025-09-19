from flask import Flask, jsonify
import mysql.connector
import os 
app = Flask(__name__)

def get_db_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "rootpass"),
        database=os.getenv("DB_NAME", "myapp")
    )
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
