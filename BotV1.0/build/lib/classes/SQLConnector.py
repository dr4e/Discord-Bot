from mysql.connector import connect

connection = connect(
    host="host", 
    user="user", 
    password="password", 
    database="database"
)
