from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from market.config import DEV_DB, PROD_DB
import os

app = Flask(__name__)

if os.environ.get('DEBUG') == '1':
    app.config['SQLALCHEMY_DATABASE_URI'] = DEV_DB
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = PROD_DB

app.config['SECRET_KEY'] = "bX7xeda&4xfd*xd0Mx(8xf9u9Gx8fP"



db = SQLAlchemy(app)
crypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from market import routes


# from market import db
# from market.models import Item, User
# db.create_all()
# user1 = User(username = 'User1',
#             email_address = 'User1@gmail.com
#             password = '1234')
# db.session.add(user1)

# user2 = User(username = 'User2',
#             email_address = 'User2@gmail.com',
#             password = '1234')
# db.session.add(user2)


# item1 = Item(name = 'laptop',
#         price = 500,
#         barcode = 123123123123,
#         description = 'bloody best laptop ever')
# db.session.add(item1)

# item2 = Item(name = 'iphone',
#         price = 300,
#         barcode = 321321321321,
#         description = 'bloody worst phone ever')
# db.session.add(item2)

# db.session.commit()