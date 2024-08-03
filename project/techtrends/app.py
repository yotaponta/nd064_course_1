import sqlite3
import logging
#import sys

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

# Connfigure log output
#logging.basicConfig(
#    level=logging.DEBUG,
#    format='%(asctime)s - %(levelname)s - %(message)s',
#    handlers=[logging.StreamHandler(sys.stdout)]
#)


# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
      return render_template('404.html'), 404
    else:
      return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    app.logger.info('About Us page retrieved.' )
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()

            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/healthz')
def health_check():
    #Return HTTP 200 and JSON response
    return jsonify({"result": "OK - healthy"}), 200

@app.route('/metrics')
def metrics():
#    # Calculate metrics
    connection = get_db_connection()
    post_count = connection.execute('SELECT COUNT(*) FROM posts').fetchone()[0]
    connection.close()
#    # Return HTTP 200 and JSON response
    return jsonify({"db_connection_count": db_connection_count, "post_count": post_count}), 200

#def calculate_post_count():
#    return 7

db_connection_count = 0
@app.before_request
def before_request():
    global db_connection_count
    db_connection_count += 1
    app.logger.info('New database connection. Total connections: %d', db_connection_count)

if not app.debug:
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(stream_handler)


# start the application on port 3111
if __name__ == "__main__":
   app.run(host='0.0.0.0', port='3111')

