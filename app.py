from flask import Flask, render_template
from config import Config
from extensions import db, bcrypt, login_manager

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
bcrypt.init_app(app)
login_manager.init_app(app)

# Import models
from models.user import User
from models.post import Post

# Import Blueprints
from routes.auth import auth_bp
from routes.blog import blog_bp

app.register_blueprint(auth_bp)
app.register_blueprint(blog_bp)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/")
def home():
    return render_template("home.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)