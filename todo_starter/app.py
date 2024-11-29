# import Flask web development framework and necessary modules
from flask import Flask, render_template, redirect, url_for, session, request, flash # type: ignore
from uuid import uuid4

app = Flask(__name__)

# setting a random secret key for the session.
app.secret_key = 'secret1'

# Generate session list
@app.before_request
def initialize_session():
    if 'lists' not in session:
        session['lists'] = []

# Create the route and render homepage
@app.route("/")
def index():
    return redirect(url_for('get_lists'))

# Render new todo list page
@app.route("/lists/new")
def add_todo():
    return render_template('new_list.html')

# Create a new todo list with a flash message everytime a new todolist is added
@app.route("/lists", methods=["POST"])
def create_list():
    title = request.form["list_title"].strip()
    session['lists'].append(
        {'id' : str(uuid4()),
         'title' : title, 
         'todos' : [],
         })
    flash("A new todo was succesfully added.", "success")
    session.modified = True
    return redirect(url_for('get_lists'))

# Render the list of todo lists
@app.route("/lists", methods = ["GET"])
def get_lists():
    return render_template('lists.html', lists=session['lists'])

if __name__ == "__main__":
    app.run(debug=True, port=5003)