import os
import pandas as pd

# Set folder path
my_folder = r'/home/largentl/novus/Assignments/Tutorial_Assignments/Week_10/Squeakuences/squeak_log_files/'

# Create empty dataframe
df = pd.DataFrame()

# Loop through all folders and text files in folder
for root, dirs, files in os.walk(my_folder):
    for file in files:
        if file.endswith(".tsv"):
            file_path = os.path.join(root, file)
            # Read text file into dataframe
            temp_df = pd.read_csv(file_path, sep='\t', header=0)
            # Append dataframe to main dataframe
            df = df._append(temp_df, ignore_index=True)

# Export dataframe to Excel file
# writer = pd.ExcelWriter('output.xlsx', engine='xlsxwriter')
# df.to_excel(writer, index=False, sheet_name='Sheet1')
# writer._save()

#Create a CSV file
df.to_csv('output.csv')