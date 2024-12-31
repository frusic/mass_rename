import os
import re

# Start of program
def startup():
    print('===============================')
    print('Welcome to the Mass Rename Tool')
    print('===============================')
    print('Choices:')
    print('    a) Remove specific string')
    print('    b) Remove matching regex')
    print('    q) Exit program')
    choice = input('-> ').lower()
    print()
    handleChoice(choice)

# Handle input from startup
def handleChoice(choice):
    if choice == 'a':
        removeMatchingStringsInDirectory()
    if choice == 'b':
        removeRegexInDirectory()
    elif choice == 'q':
        quit()
    else:
        print('Invalid option')
        print()
        startup()

# General logic to apply an operation if filename matches a condition
def applyOperationToFiles(inputRequest, condition, operation):
    print(inputRequest)
    string = input('-> ')
    print()
    # Be able to quit instead of input string
    if string.lower() == 'q':
        quit()
    cwd = os.getcwd()
    count = 0
    for filename in os.listdir(cwd):
        # Don't do anthing if directory
        if not os.path.isfile(filename):
            continue
        # Rename by removing string
        if condition(string, filename):
            operation(string, filename)
            count += 1
    print('Replaced', count, 'file(s).')
    print('-------------------------------')
    print()
    startup()

# Option A: Remove a particular string
def removeMatchingStringsInDirectory():
    def condition(string, filename):
        return string in filename
    def operation(string, filename):
        os.rename(filename, filename.replace(string, ''))
    inputRequest = 'Please enter the exact string, or quit'
    applyOperationToFiles(inputRequest, condition, operation)

# Option B: Replace all characters matching given regex
def removeRegexInDirectory():
    def condition(string, filename):
        return re.search(string, filename) is not None
    def operation(string, filename):
        os.rename(filename, re.sub(string, '', filename))
    inputRequest = 'Please enter the regex string, or quit'
    applyOperationToFiles(inputRequest, condition, operation)

# Run startup when running this file
if __name__ == '__main__':
    startup()