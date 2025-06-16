
import pymysql

def test_user_exists_in_db():
    connection = pymysql.connect(host="localhost", user="root", password="", database="testdb")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username='testuser'")
    result = cursor.fetchone()
    assert result is not None
    connection.close()
