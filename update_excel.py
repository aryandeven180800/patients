import pandas as pd

# Existing Excel file path
excel_file = 'patients_data.xlsx'

# Additional dummy data (5 rows)
additional_data = [
    (4, 'Emma Johnson', '1980-09-25', 'Female', 60.0, '5551234567'),
    (5, 'James Brown', '1995-03-12', 'Male', 85.5, '9876543210'),
    (6, 'Sophia Miller', '1988-07-30', 'Female', 55.5, '1239876543'),
    (7, 'William Davis', '1976-12-15', 'Male', 75.0, '4567890123'),
    (8, 'Olivia Wilson', '1992-05-05', 'Female', 70.2, '3210987654')
]

# Read existing Excel file
existing_data = pd.read_excel(excel_file)

# Convert additional data to DataFrame
additional_df = pd.DataFrame(additional_data, columns=existing_data.columns)

# Append additional data to existing data
updated_data = existing_data.append(additional_df, ignore_index=True)

# Write updated data to Excel file
updated_data.to_excel(excel_file, index=False)

print("Additional data added successfully.")
