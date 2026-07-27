import pymysql

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="Avinash@2005",
        database="blog_db",
        port=3306
    )

    print("Connected Successfully!")

except Exception as e:
    print(e)