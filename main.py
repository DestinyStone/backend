from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from controller.controller import controller
from models.model import db

app = Flask(__name__)


app.config['SECRET_KEY'] = '123456'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 * 1024
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_ECHO'] = True
app.register_blueprint(controller)
if __name__ == '__main__':
    db.init_app(app)
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, port=3000)