import pandas as pd
import os

file1 = '/Users/johannesschmid/Desktop/CodeBaking/Python Project/sheet1.xlsx'
file2 = '/Users/johannesschmid/Desktop/CodeBaking/Python Project/sheet2.xlsx'


def formatcheck(file):
    # Splitting path and file extension off
    filepath = os.path.dirname(file)
    file_extension = os.path.splitext(file)[1]

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
    return file_extension

formatcheck(file1)
formatcheck(file2)


def reading_file(file):
    filepath = os.path.dirname(file)
    # Changing working directory to filepath
    os.chdir(filepath)
    # Splitting file extension
    file_extension = os.path.splitext(file)[1]

    #Read file based on fileformat
    if file_extension == '.xlsx' or 'xls':
        # Reading excel and storing it into dataframe
        return pd.read_excel(file)
    else:
        # Reading csv and storing it into dataframe
        return pd.read_csv(file)

data1 = reading_file(file1)
data2 = reading_file(file2)

def header_check(data):
    #reading for 3 columns of file
    headers = (data.columns)[:3]
    #checking headers on correct format
    if not (headers==(['id', 'name', 'price'])).all():
        print('The file does not have the right header columns. Please provide format: id, name, price')

header_check(data1)

def file_copy(data_file1,data_file2):
    # Check if id is present in file2
    print(data_file1[0])


file_copy(data1,data2)