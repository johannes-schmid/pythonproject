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
    allowed_extension = ['.xlsx', '.csv']

    # checking if the path exists
    if not os.path.exists(file):
        print('The file path for the following file does not exist:', file)

    # checking if the format is valid
    if file_extension not in allowed_extension:
        print('The following file has none supported file format:', file)
    return file_extension, filepath

formatcheck(file1)
formatcheck(file2)


def reading_file(file):
    filepath = os.path.dirname(file)
    # Changing working directory to filepath
    os.chdir(filepath)

    print(file)
    # Reading file and storing it into dataframe
    df = pd.read_excel(file)
    print(df)


reading_file(file1)