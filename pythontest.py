import pandas as pd
import os
import sys

file1 = '/Users/johannesschmid/Desktop/CodeBaking/Python Project/sheet1.xlsx'
file2 = '/Users/johannesschmid/Desktop/CodeBaking/Python Project/sheet2.xlsx'

def getExtension(file):
    return os.path.splitext(file)[1]


def formatcheck(file):
    # Splitting path and file extension off
    file_extension = getExtension(file)
    filepath = os.path.dirname(file)
    # Changing working directory to filepath
    os.chdir(filepath)

    # Defining allowed file extensions
    allowed_extensions = ['.xlsx', '.csv', '.xls']

    # checking if the path exists
    if not os.path.exists(file):
        # Throw file path error
        sys.exit('The file path for the following file does not exist ' + file)

    # checking if the format is valid
    if file_extension not in allowed_extensions:
        # Throw file format error
        sys.exit('The following file has none supported file format: ' + file)

formatcheck(file1)
formatcheck(file2)

def reading_file(file):
    filepath = os.path.dirname(file)
    # Changing working directory to filepath
    os.chdir(filepath)
    # Splitting file extension
    file_extension = getExtension(file)


    #Read file based on fileformat
    if file_extension == '.xlsx' or file_extension == '.xls':
        # Reading excel and storing it into dataframe
        return pd.read_excel(file)
    else:
        # Reading csv and storing it into dataframe
        return pd.read_csv(file)


origin = reading_file(file1)
destination = reading_file(file2)

def headerCheck(data):
    #reading first 3 columns of file
    headers = data.columns
    required_columns = ['id', 'name', 'price']
    #checking headers on correct format
    for column in required_columns:
        if not column in headers:
            sys.exit('The file does not have the right header columns. Please provide those columns in each file: id, name, price')

headerCheck(origin)
headerCheck(destination)

def file_copy(origin,destination):
    # Creating first match criteria via ID
    # Read all IDs of origin file and converting into regular array
    origin_ids = origin['id'].to_numpy()
    # Read all IDs of destination file and converting into regular array
    destination_ids = destination['id'].to_numpy()
    # Looping through all origin ids and check if it exists in destination
    for id_value in origin_ids:
        # If we find the id in the destination file we copy over the value
        if id_value in destination_ids:
            # Get the value of the origin id for the price
            price = origin['price'][origin.id == id_value]
            # Set value of destination file price to this price
            destination['price'][destination.id == id_value] = price

file_copy(origin, destination)