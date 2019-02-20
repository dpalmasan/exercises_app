from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db. This must go before the below imports (kind of circular
# dependency)
db = SQLAlchemy()
bcrypt = Bcrypt()

from .QuestionModel import QuestionModel
from .QuestionModel import  QuestionSchema
from .UserModel import UserModel
from .UserModel import UserSchema
