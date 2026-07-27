from urllib.parse import quote_plus

class Config:

    SECRET_KEY = "blogsphere_secret_key"

    password = quote_plus("Avinash@2005")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://root:{password}@localhost:3306/blog_db"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False