import pandas as pd
import os
import sys

if len(sys.argv) < 3:
    sys.exit('Two mandatory parameters necessary')

file1 = sys.argv[1]
file2 = sys.argv[2]

writing_mode = '-o' in sys.argv

def getExtension(file):
    return os.path.splitext(file)[1]

def formatcheck(file):
    # Splitting path and file extension off
    file_extension = getExtension(file)

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

def reading_file(file):
    # Splitting file extension
    file_extension = getExtension(file)


    #Read file based on fileformat
    if file_extension == '.xlsx' or file_extension == '.xls':
        # Reading excel and storing it into dataframe
        return pd.read_excel(file)
    else:
        # Reading csv and storing it into dataframe
        return pd.read_csv(file)

def headerCheck(data):
    # Get all headers
    headers = data.columns
    required_columns = ['id', 'name', 'price']
    #checking headers on correct format
    for column in required_columns:
        if column not in headers:
            sys.exit('The file does not have the right header columns. Please provide this column: ' + column)


def file_copy(origin, destination):
    # iterate over ids in the destination file
    # Set-up counter for matches
    updated_matches = 0
    # Set-up counter for where the price was already correct
    not_updated_matches = 0
    for index in range(len(destination)):
        # find all items in origin that match that item id
        filterId = origin['id'] == destination.loc[index, 'id']
        matchesId = origin.loc[filterId]
        # create counter for changed id lines

        # if there are no matched we do nothing, otherwise we copy over the price
        if len(matchesId) > 0:
            if destination.loc[index, 'price'] == matchesId.iloc[0]['price']:
                not_updated_matches += 1
            else:
                destination.loc[index, 'price'] = matchesName.iloc[0]['price']
                updated_matches += 1
        else:
            # find all items in origin that match the name column
            filterName = origin['name'].str.upper() == destination.loc[index, 'name'].upper()

            matchesName = origin.loc[filterName]
            if len(matchesName) > 0:
                if destination.loc[index, 'price'] == matchesName.iloc[0]['price']:
                    not_updated_matches += 1
                else:
                    destination.loc[index, 'price'] = matchesName.iloc[0]['price']
                    updated_matches += 1

    # Report for amount of rows in origin
    lines_origin = len(origin.axes[0])
    print('Number of items in the origin file ', lines_origin)

    # Report for amount of rows in destination
    lines_destination = len(destination.axes[0])
    print('Number of items in the destination file ', lines_destination)

    # Report for changed lines
    print('We have changed ', updated_matches, ' Items')
    # Report for items that could not be matched
    print('We were not able to match ', (lines_destination - ( updated_matches + not_updated_matches )) ,' item(s)')
    # Report for lines where the price was already correct
    print('Items that were already correct: ', not_updated_matches)


def writing_file(file, dataframe, mode):
    file_extension = getExtension(file)
    file_without_extension = os.path.splitext(file)[0]
    filename = file if mode == True else file_without_extension + '_edited' + file_extension
    if file_extension == '.xlsx' or file_extension == '.xls':
        # Reading excel and storing it into dataframe
        dataframe.to_excel(filename, index=False)
    else:
        # Reading csv and storing it into dataframe
        dataframe.to_csv(filename, index=False)

formatcheck(file1)
formatcheck(file2)

origin = reading_file(file1)
destination = reading_file(file2)

headerCheck(origin)
headerCheck(destination)

file_copy(origin, destination)

writing_file(file2, destination, writing_mode)


