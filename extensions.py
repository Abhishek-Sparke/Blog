from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Database
db = SQLAlchemy()

# Password hashing
bcrypt = Bcrypt()

# Login manager
login_manager = LoginManager()
login_manager.login_view = "auth.login"