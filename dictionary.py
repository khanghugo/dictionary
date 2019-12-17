import argparse

# argument -nonr will trigger non-relevant search when you add it into the command-line option
parser = argparse.ArgumentParser(prog='dictionary',usage='%(prog)s [-nonr]')
parser.add_argument('-nonr', default='', help='Non-relevant search', action="store_true")
args = parser.parse_args()

# casual openning file. On linux, the encoding part is not needed. But on Windows, it does not work if you try to open it.
openFile = open("dict.txt", "r", encoding="utf8")

# this command somehow makes lines into a list so really neat
cuttingFile = openFile.readlines()

# This function is necessary but it looks neat
def feedInput():
    userInput = input('Search: ')
    return userInput

# The part where it searches, it takes in input and flag for the non-relevant search
def searching(userInput, flag):
    # This variable returns whether there is no result or not down in the loop
    count = 0

    # This uses argument parser to turn on non-relevant search
    if args.nonr:
        flag == 1

    # This just makes the first word of the input Capitalized or just in normal so the non-relevant search can filter all the words in the dictionary 
    capInput = str(userInput.title())
    lowInput = capInput.lower()

    # cuttingFile is arranged into a list so now we split it into strings
    for i in cuttingFile:

        # because of case-sensitivity, I have to make it insesitive, this takes less cpu consumption than formatting all of the definitions
        if userInput in i or capInput in i or lowInput in i:

            # this is the default search. When you search something, it will look at the words from the start, take a look at dict.txt for an easier picture
            if flag != 1:
                relevantSearch(capInput, i)

            # since the condition up there is non-discriminant, it will take every keyword in the dictionary whether Capitalized or not.
            else:
                print(i)

            # if the condition returns true, it means there is a search result and this variable will raise to one. In the loop, it says: "Do not say 'there is no result'"
            count = 1

    # since the print is in the condition, we don't need to print it in with another command. This return count will be caught by the loop to return whether there is a search result or not.
    return count

# a function that checks the first words of the dictionary with the input. If it returns true, it will print the string. Because of how the dictionary is written, not a lot of work is needed because it is all beautifully organized. Thanks, Oxford Dictionary.
def relevantSearch(userInput, word):
    if userInput == word[:len(userInput)]:
        print(word)

# this is where the program starts. 
while True:
    try:
        # a condition will call the function. This makes everything looks nicer. If the function returns zero, it means the condition in the fuction is not met and no search result appears
        if searching(feedInput(), args.nonr) == 0:
            print('No result')
        else:
            pass
    except:
        break
