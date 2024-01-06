import psycopg2

# Update these variables with your PostgreSQL database credentials
db_credentials = {
    'host': 'localhost',
    'database': 'Toptrumpsdb',
    'user': 'postgres',
    'password': 'wachtwoord',
    'port': '5432',  # Default is 5432
}

def connect_to_database():
    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(**db_credentials)
        cursor = connection.cursor()
        return connection, cursor

    except (Exception, psycopg2.Error) as error:
        print("Error connecting to PostgreSQL database:", error)
        return None, None


def call_stored_procedure(id, difficulty, higher_lower):
    connection, cursor = connect_to_database()

    if connection and cursor:
        try:
            # Execute a stored procedure
            cursor.callproc('get_computer_choice', (id, difficulty, higher_lower))  # Replace with actual parameters

            # Fetch the results if the stored procedure returns any
            results = cursor.fetchall()
            # Get the string value out of the tuple
            if results:
                actual_value = results[0]
                if isinstance(actual_value, tuple):
                    actual_value = actual_value[0]
                attribute_dict = {"Speed":1, "Weight":2, "Beauty":3, "Killer Instinct": 4}


            return attribute_dict.get(actual_value)

        except (Exception, psycopg2.Error) as error:
            print("Error calling the stored procedure:", error)

        finally:
            # Close the cursor and connection
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed.")

if __name__ == "__main__":
    # Example: Retrieve data from the 'opponent_choices' table
    # retrieve_data_from_table()

    # Example: Call a stored procedure
    # call_stored_procedure()
    print(call_stored_procedure(20,'Hard', True))
    
