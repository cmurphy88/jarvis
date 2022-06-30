import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="postgres",
                                  password="password",
                                  host="localhost",
                                  port="5432",
                                  database="jarvisdb")

    # selecting information from the database
    cursor = connection.cursor()
    users_query = ''' SELECT * FROM users;'''
    cursor.execute(users_query)
    connection.commit()
    record = cursor.fetchall()
    print("result ", record)

    # # inserting into the database
    # insert_query = """INSERT INTO users (first_name, last_name, email, password) VALUES ('Rory', 'Murphy', 'r@gmail.com', 'qwerty');"""
    # cursor.execute(insert_query)
    # connection.commit()
    # print("1 user inserted successfully")
    # cursor.execute("SELECT * FROM users;")
    # record = cursor.fetchall()
    # print("Result ", record)

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection == True):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

