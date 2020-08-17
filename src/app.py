from database import DataBase
from flask import Flask, render_template, request
from message import Message


app = Flask(__name__)

DATABASE = DataBase()


@app.route('/')
def home():
    messages = DATABASE.read_all()
    return render_template('index.html', result=messages)


@app.route('/', methods=['POST'])
def new_short_post():
    content = request.form['content']
    author = request.form['author']
    message = Message(content, author)
    message.write()
    messages = DATABASE.read_all()
    return render_template('index.html', result=messages)


if __name__ == '__main__':
    app.run()
