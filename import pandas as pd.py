import pandas as pd

# Function to read the existing Excel file
def read_excel(file_path):
    return pd.read_excel(file_path)

# Function to append new data to the existing data
def append_data(existing_data, new_data):
    # Concatenate the existing and new data
    updated_data = pd.concat([existing_data, new_data], ignore_index=True)
    return updated_data

# Function to save data to an Excel file
def save_to_excel(data, file_path):
    data.to_excel(file_path, index=False, engine='openpyxl')

# Main execution
if __name__ == "__main__":
    excel_file = 'patients_data.xlsx'
    
    # New data to be added (as a list of tuples)
    new_data_list = [
        (4, 'Alice Brown', '1992-07-21', 'Female', 55.0, '3333333333'),
        (5, 'Bob White', '1983-02-11', 'Male', 85.5, '4444444444')
    ]
    
    # Define column names (these should match the existing Excel file columns)
    column_names = ['PATIENTID', 'NAME', 'DATEOFBIRTH', 'GENDER', 'WEIGHT', 'CONTACTNUMBER']
    
    # Create a DataFrame for the new data
    new_data_df = pd.DataFrame(new_data_list, columns=column_names)
    
    try:
        # Read existing data from Excel
        existing_data_df = read_excel(excel_file)
        
        # Append new data to the existing data
        updated_data_df = append_data(existing_data_df, new_data_df)
        
        # Save the updated data to the Excel file
        save_to_excel(updated_data_df, excel_file)
        
        print(f"New data successfully added to {excel_file}")
    
    except Exception as e:
        print("An error occurred:", e)
