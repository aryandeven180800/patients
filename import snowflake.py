import snowflake.connector
import pandas as pd

# Define connection parameters
connection_parameters = {
    'account': 'keiuzfs-zp01978',
    'user': 'ARYAN18',
    'password': 'Aryan@2000',
    'warehouse': 'my_warehouse',
    'database': 'pratcie',
    'schema': 'hospital',
    'role': 'ACCOUNTADMIN'
}

# Function to establish a connection
def get_connection(params):
    return snowflake.connector.connect(
        user=params['user'],
        password=params['password'],
        account=params['account'],
        warehouse=params['warehouse'],
        database=params['database'],
        schema=params['schema'],
        role=params['role']
    )

# Function to retrieve data from Snowflake
def fetch_data(conn, query):
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        df = pd.DataFrame(data, columns=columns)
        return df
    finally:
        cursor.close()

# Main execution
if __name__ == "__main__":
    # Establish connection
    try:
        conn = get_connection(connection_parameters)
        
        # Define your SQL query
        query = "SELECT * FROM Patients"
        
        # Fetch data from Snowflake
        df = fetch_data(conn, query)
        
        # Save DataFrame to Excel file
        excel_file = 'patients_data.xlsx'
        df.to_excel(excel_file, index=False, engine='openpyxl')
        
        print(f"Data successfully saved to {excel_file}")
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Close the connection
        if conn is not None:
            conn.close()
