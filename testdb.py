import MySQLdb

# Database configuration
MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'AtestDB@24'
MYSQL_DB = 'python_sms1'


try:
    # Establish a connection to the database
    db = MySQLdb.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWORD,
        db=MYSQL_DB
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute a SQL query to get all tables
    cursor.execute("SHOW TABLES")

    # Fetch all the results
    tables = cursor.fetchall()

    # Print the tables
    print("Tables in the database:")
    for table in tables:
        print(table[0])

except MySQLdb.Error as e:
    print(f"Error connecting to MySQL Platform: {e}")

finally:
    print('pass')
