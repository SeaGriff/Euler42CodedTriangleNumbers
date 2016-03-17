""" Reads words from a text file and calculates their total letter values, with a = 1, b = 2, etc,.
Prints the number of words which have a value equal to the n-th triangular number, where n is the length of the word.
"""

""" Imports """

import re

""" Constants """

FILE_NAME = "p042_words.txt"
LETTER_OFFSET = ord('a') - 1
MAX_TRIANGLE_NUMBER = 20

""" Sums up the letter value of a string, with a = 1, b = 2, etc.
Input: string str
Restrictions: Assumes str is in upper case and contains only letters
Return: int """

def letterSum(str):
    str = str.lower()
    sum = 0
    for letter in str:
        sum += ord(letter) - LETTER_OFFSET
    return(sum)

""" Reads FILE_NAME character by character. Assumes the file is in the format "WORD1","WORD2","WORD3",...
Rather jankily does not cut out the quote at the end of the file, but it doesn't matter in this case. """
def main():
    total = 0
    triangleNumbers = {n * (n + 1) / 2 for n in range(MAX_TRIANGLE_NUMBER)}
    file = open(FILE_NAME, 'r')
    file.seek(1)
    for word in re.split('\",\"',file.read()):
        if letterSum(word) in triangleNumbers:
            total += 1
    print(total)
    file.close()

if __name__ == '__main__':
    main()