import pandas as pd
import os

file1 = '/Users/johannesschmid/Desktop/CodeBaking/Python Project/sheet1.xlsx'
file2 = '/Users/johannesschmid/Desktop/CodeBaking/Python Project/sheet2.xlsx'

def getExtension(file):
    return os.path.splitext(file)[1]


def formatcheck(file):
    # Splitting path and file extension off
    filepath = os.path.dirname(file)
    file_extension = getExtension(file)

    # Changing working directory to filepath
    os.chdir(filepath)

    # Defining allowed file extensions
    allowed_extension = ['.xlsx', '.csv', '.xls']

    # checking if the path exists
    if not os.path.exists(file):
        print('The file path for the following file does not exist:', file)

    # checking if the format is valid
    if file_extension not in allowed_extension:
        print('The following file has none supported file format:', file)

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
    #reading for 3 columns of file
    # TODO: only check on the 3 column not the first three
    headers = (data.columns)
    columns = ['id', 'name', 'price']
    #checking headers on correct format
    for column in columns:
        if column not in headers:
            exit()
    if ['id', 'name', 'price'] in headers:
        print('The file does not have the right header columns. Please provide format: id, name, price')

headerCheck(data1)

def file_copy(data_file1,data_file2):
    # Check if id is present in file2
    print(data_file1[0])


file_copy(data1,data2)