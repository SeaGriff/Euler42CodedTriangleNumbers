""" Reads words from a text file and calculates their total letter values, with a = 1, b = 2, etc,.
Prints the number of words which have a value equal to the n-th triangular number, where n is the length of the word.
"""

""" Constants """

FILE_NAME = "p042_words.txt"

""" Sums up the letter value of a string, with a = 1, b = 2, etc.
Input: string str
Restrictions: Assumes str is in upper case and contains only letters
Return: int """

def letterSum(str):
    str = str.lower()
    sum = 0
    for i in range(0,len(str)):
        sum += str[i].ord() - 64
    return(sum)

def main():
    file = open(FILE_NAME, r)


if __name__ == '__main__':
    main()