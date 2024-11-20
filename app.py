from flask import Flask, request, jsonify
from task_reminder.utils import categorize_task, extract_due_time
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                     (id INTEGER PRIMARY KEY, task TEXT, category TEXT, due_time TEXT)''')
    conn.commit()
    conn.close()

@app.route('/add_task', methods=['POST'])
def add_task():
    task_input = request.json.get('task')
    category = categorize_task(task_input)
    due_time = extract_due_time(task_input)

    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task, category, due_time) VALUES (?, ?, ?)",
                   (task_input, category, due_time))
    conn.commit()
    conn.close()

    return jsonify({"message": "Task added successfully!"})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
