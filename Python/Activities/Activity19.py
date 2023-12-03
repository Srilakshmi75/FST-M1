# Import pandas
import pandas
from pandas import ExcelWriter

# Create a dictionary that will be used to create the DataFrame
data = {
    'FirstName':["Apurva", "Sri", "Priyanka"],
    'LastName':["Gade", "Lakshmi", "Kante"],
    'Email':["apurva@example.com", "srilakshmi@example.com", "priyanka.kante@example.com"],
    'PhoneNumber':["1237829158", "5432184058", "3248727830"]
}



# Create the DataFrame that will be written to the excel file
dataframe = pandas.DataFrame(data)

# Print the dataframe
print(dataframe)

# Write the dataframe to a Excel file
writer = ExcelWriter('sample.xlsx')
dataframe.to_excel(writer, 'Sheet1', index = False)

# Commit data to the Excel file
writer.close()