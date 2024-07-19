#i just copy the chatgpt's code and it's working!
from flask import Flask, request, render_template, redirect, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def get_config():
    return {
        'user': 'applicationUser',
        'password': 'my_user_password',
        'host': 'mysql-container',
        'port': '3306',
        'database': 'applicationdb'
    }

def execute_query(query, params=None, fetchone=False, fetchall=False):
    config = get_config()
    connection = None
    result = None
    cursor = None
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params)
        if fetchall:
            result = cursor.fetchall()
        elif fetchone:
            result = cursor.fetchone()
        else:
            connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
    return result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    todos = execute_query("SELECT * FROM todos", fetchall=True)
    return render_template('home.html', todos=todos)

@app.route('/create', methods=['GET', 'POST'])
def create_todo():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        due_date = request.form['due_date']
        
        query = "INSERT INTO todos (name, description, due_date) VALUES (%s, %s, %s)"
        params = (name, description, due_date)
        execute_query(query, params)
        return redirect(url_for('home'))
    
    return render_template('create.html')

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    query = "DELETE FROM todos WHERE id = %s"
    params = (todo_id,)
    execute_query(query, params)
    return redirect(url_for('home'))

@app.route('/last')
def last_todo():
    # Retrieve the last added todo
    last_todo = execute_query("SELECT * FROM todos ORDER BY id DESC LIMIT 1", fetchone=True)
    if last_todo:
        description = last_todo['description']
        query = f"SELECT * FROM todos WHERE description = '{description}'"
        result = execute_query(query, fetchall=True)
        return render_template('last.html', todos=result)
    return "No todos found."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
