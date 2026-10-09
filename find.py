# Part 1 - a small "find" tool (like a simplified `grep`).
#
# This is a COMMAND-LINE program: you run it from the terminal and pass it
# arguments, e.g.   python find.py apple sample.txt
#
# The argument parser is started for you. Finish the TODOs below.

import argparse
import string 
from collections import Counter 


def main():
    parser = argparse.ArgumentParser(
        description="Print the lines of a file that contain a given pattern.")
    parser.add_argument("filename", help="the file to search")
    parser.add_argument("pattern", help="the text to look for")
    parser.add_argument("-i", "--ignore-case", action="store_true") 
    args = parser.parse_args()

    with open(args.filename) as file:
        text = file.read()
    words = text.split('\n')

    i = 0
    for word in words:
        i+=1
        if ((str.lower(word)).find(str.lower(args.pattern)) != -1 and args.ignore_case == True):
            print(f'{i}: {word}')
        elif (word.find(args.pattern) != -1):
            print(f'{i}: {word}')


if __name__ == "__main__":
    main()
