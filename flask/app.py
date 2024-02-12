from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def get_character_sets():
    connection = mysql.connector.connect(host='mysql', user='root', password='password', database='information_schema')
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM CHARACTER_SETS")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

