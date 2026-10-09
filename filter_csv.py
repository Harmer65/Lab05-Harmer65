# Part 2 (STRETCH) - filter the rows of a CSV file.
#
# This is a COMMAND-LINE program. You run it like:
#     python filter_csv.py people.csv city Oshawa
#
# The argument parser is finished for you. Complete the TODO.

import argparse
import csv

def main():
    parser = argparse.ArgumentParser(
        description="Print the rows of a CSV where a column has a given value.")
    parser.add_argument("filename", help="the CSV file to read")
    parser.add_argument("column", help="the name of the column to match on")
    parser.add_argument("value", help="the value to match")

    args = parser.parse_args()

    with open(args.filename) as file:
        text = file.read()
    words = text.split('\n')
    # print(f'{words = }')

    column2 = -1

    if args.column == 'name':
        column2 = 0
    elif args.column == 'city':
        column2 = 1
    elif args.column == 'age':
        column2 = 2
    else:
        print('Invalid column input!')

    word2 = []
    for i in range(len(words)):
        if (words[i].find(',') != -1):
            word2.append(words[i].split(','))
            if(word2[i][column2].find(args.value) != -1):
                print(f'{words[i]}')

    # print(f'{word2}')
    # print(f'{word2[args.column][args.value] = }')

    # TODO: open args.filename and read it with csv.reader. The first row is the
    #   header. Find the position of args .column within the header, then print every
    #   data row (its values joined by commas) whose value in that column equals
    #   args.value.


if __name__ == "__main__":
    main()
