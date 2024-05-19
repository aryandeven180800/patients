import os
import pandas as pd
import snowflake.connector



def get_connection():
    return snowflake.connector.connect(
        USER=os.getenv('USER'),
        PASSWORD=os.getenv('PASSWORD'),
        ACCOUNT=os.getenv('ACCOUNT'),
        WAREHOUSE=os.getenv('WAREHOUSE'),
        DATABASE=os.getenv('DATABASE'),
        SCHEMA=os.getenv('SCHEMA'),
        ROLE=os.getenv('ROLE')
    )

def read_excel(file_path):
    return pd.read_excel(file_path)

def insert_data(conn, table_name, data):
    cursor = conn.cursor()
    try:
        placeholders = ','.join(['%s'] * len(data.columns))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        data_tuples = [tuple(x) for x in data.to_numpy()]
        cursor.executemany(query, data_tuples)
        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

if __name__ == "__main__":
    excel_file = 'patients_data.xlsx'
    
    try:
        new_data_df = read_excel(excel_file)
        
        conn = get_connection()
        
        insert_data(conn, 'Patients', new_data_df)
    
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        if conn is not None:
            conn.close()
