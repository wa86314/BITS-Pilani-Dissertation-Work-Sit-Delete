from flask import Flask, request
from connection import db_conn

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "INFO: This Microservice is used for deleting record from Database"

@app.route('/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    stud_id = data.get('id')

    db_cursor = db_conn.cursor()
    db_cursor.execute("DELETE FROM student WHERE id = %s", (stud_id))
    db_conn.commit()

    #If the target ID won't present in the student table
    if db_cursor.rowcount == 0:
        return f"ID {stud_id} not found"

    return f"Record deleted for {stud_id} successfully!"

if __name__ == '__main__':
     app.run(debug=True, port=5003, host='0.0.0.0')
db_conn.close()
