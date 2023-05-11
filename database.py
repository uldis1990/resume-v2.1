#Python 3.10.8
import mysql.connector

# create a connection to the database with SSL/TLS encryption
cnx = mysql.connector.connect(user='xxxx',
                              password='xxxxxx',
                              host='xxxxxx',
                              database='xxxx',
                              ssl_ca='xxxxx')

# create a cursor object for executing queries
cursor = cnx.cursor()
#s='users'
# execute a query
#query = f'SELECT * FROM {s}'
# define a variable to hold the table name
#table_name = 'mytable'

# build a dynamic query with string concatenation
#query = 'SELECT * FROM ' + table_name

query = f'SELECT * FROM users'
cursor.execute(query)

# fetch the results and print them
results = cursor.fetchall()
#for row in results:
print(results)
#returns list of tuples 
# close the cursor and connection
cursor.close()
cnx.close()