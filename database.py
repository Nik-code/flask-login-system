import pymysql

# Configure the MySQL database connection
DB_HOST = 'localhost'
DB_USER = 'username' # Change this to your MySQL username
DB_PASSWORD = 'password' # Change this to your MySQL password
DB_NAME = 'db-name' # Change this to your MySQL database name


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def get_connection(self):
        return pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def insert_user(self, username, password, fullname, email, phone, score):
        connection = self.get_connection()
        cursor = connection.cursor()
        insert_query = "INSERT INTO users (username, password, fullname, email, phone, score) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (username, password, fullname, email, phone, score))
        connection.commit()
        connection.close()

    def get_user(self, username, password):
        connection = self.get_connection()
        cursor = connection.cursor()
        select_query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(select_query, (username, password))
        user_data = cursor.fetchone()
        connection.close()
        return user_data

    def get_user_by_username(self, username):
        connection = self.get_connection()
        cursor = connection.cursor()
        select_query = "SELECT * FROM users WHERE username = %s"
        cursor.execute(select_query, (username,))
        user_data = cursor.fetchone()
        connection.close()
        return user_data
