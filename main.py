from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, logout_user, current_user, \
    login_required
from flask_restful import Api
from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, \
    BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
# login_manager = LoginManager()
# login_manager.init_app(app)


'''@login_manager.user_loader
def load_user(user_id):
    sessions = db_session.create_session()
    return sessions.query(users.User).get(user_id)
'''


@app.route('/')
def main_page():
    return render_template('main_page.html')


@app.route("/first")
def first():
    return render_template('1.html')


def main():
    app.run()


if __name__ == '__main__':
    main()
