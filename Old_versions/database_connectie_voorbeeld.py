import psycopg2
import decimal


# Connection parameters
db_credentials = {
    'host': 'localhost',
    'database': 'Toptrumpsdb',
    'user': 'postgres',
    'password': 'wachtwoord',
    'port':'5432'
}


# Establish a connection to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_credentials)
    cursor = connection.cursor()

    # Execute a simple SELECT query
    query = "SELECT * FROM animals;"
    cursor.execute(query)

    # Fetch all the results
    records = cursor.fetchall()

    # Display the results
    for record in records:
        record = tuple(float(value) if isinstance(value, decimal.Decimal) else value for value in record)
        print(record)
    


except (Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL database:", error)

finally:
    # Close the cursor and connection
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed.")
