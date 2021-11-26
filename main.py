import csv
from enum import Enum
from io import TextIOWrapper


class datatype(Enum):
    """
    Data type enum
    """
    TEXT = 'TEXT'
    BOOLEAN = 'BOOLEAN'
    INTEGER = 'INTEGER'


def getFormat(formatFile: TextIOWrapper):
    """
    Get format from format file.

    Args:
        formatFile (TextIOWrapper): Format file

    Raises:
        err: Other errors

    Returns:
        list: A list of dictionary
    """
    try:
        formats = []
        reader = csv.DictReader(formatFile, delimiter=',')
        for format in reader:
            for key, value in format.items():
                key = key.strip()
                value = value.strip()
            format['width'] = int(format['width'])
            format['datatype'] = datatype(format['datatype'])
            formats.append(format)
        return formats
    except BaseException as err:
        raise err


def getData(formatData: list, dataFormatFile: TextIOWrapper):
    """
    Get data from data file and return the desired output format

    Args:
        formatData (list): Format data returned by the function getFormat()
        dataFormatFile (TextIOWrapper): Data format file

    Raises:
        ValueError: A line in the file does not have the same length specified by the format file
        ValueError: A value in a line which is meant to be a boolean value is neither 0 nor 1
        err: Other errors

    Returns:
        list: A list of dictionary
    """
    try:
        total_line_length = 0
        output = []
        for format in formatData:
            total_line_length += format['width']

        for line_no, line in enumerate(dataFormatFile):
            line = line.strip()

            # Check if the length of line is the same as how the format file described.
            if total_line_length != len(line):
                raise ValueError(f'Line {line_no} length mismatch')

            obj = {}
            line_idx = 0  # Current reading index point to the line
            for format in formatData:
                col_name = format['column name']
                width = format['width']
                data_type = format['datatype']
                substring = line[line_idx: line_idx + width]
                line_idx += width
                substring = substring.strip()
                # Change [substring] to the desired data type
                if data_type == datatype.TEXT:
                    substring_val = substring
                elif data_type == datatype.INTEGER:
                    substring_val = int(substring)
                else:
                    if substring == '1':
                        substring_val = True
                    elif substring == '0':
                        substring_val = False
                    else:
                        raise ValueError(
                            f'{substring} is not a type of BOOLEAN at line {line_no}')
                # Put [substring_val] into [obj]
                obj[col_name] = substring_val
            # Add [obj] into [output]
            output.append(obj)
        # Return output
        return output
    except BaseException as err:
        raise err


def parse_flatfile(datafilename: str, formatfilename: str):
    try:
        dataFormatFile = open(datafilename, "r", newline='')
        formatFile = open(formatfilename, "r", newline='')

        formatData = getFormat(formatFile)
        output = getData(formatData, dataFormatFile)

        dataFormatFile.close()
        formatFile.close()
        return output
    except BaseException as err:
        raise err


def main():
    input = [["data/testformat1_2015-06-28.txt", "specs/testformat1.csv"]]
    for files in input:
        try:
            output = parse_flatfile(files[0], files[1])
            print(output)
        except BaseException as err:
            print(err)


if __name__ == '__main__':
    main()
