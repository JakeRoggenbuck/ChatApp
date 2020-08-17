from database import DataBase
from flask import Flask, render_template, request
from message import Message


app = Flask(__name__)

# Get db
DATABASE = DataBase()


# Load main page
@app.route('/')
def home():
    # Get messages
    messages = DATABASE.read_all()
    # Load main page
    return render_template('index.html', result=messages)


# Process send form
@app.route('/', methods=['POST'])
def new_short_post():
    # Get elements
    content = request.form['content']
    author = request.form['author']
    # Make message object
    message = Message(content, author)
    # Write object to db and push it
    message.write()
    # Get all messages
    messages = DATABASE.read_all()
    # Send back to main page with new message
    return render_template('index.html', result=messages)


if __name__ == '__main__':
    app.run()
