import argparse

parser = argparse.ArgumentParser(prog='dictionary',usage='%(prog)s [keyword] [-nonr]')
parser.add_argument('-nonr', default='', help='Non-relevant search')
parser.add_argument('--foo', help='test')
args = parser.parse_args()


openFile = open("dict.txt", "r")

cuttingFile = openFile.readlines()

def feedInput():
    userInput = input('Search: ')
    return userInput

def searching():
    count = 0
    userInput = feedInput()

    formatInput = str(userInput.title())

    for i in cuttingFile:
        if formatInput in i:
            #print(i)
            relevantSearch(formatInput, i)
            count = count + 1
    return count

def relevantSearch(userInput, word):
    if userInput == word[:len(userInput)]:
        print(word)

while True:
    try:
        if searching() == 0:
            print('No result')
        else:
            pass

    except:
        break
