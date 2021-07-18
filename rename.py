import os

# Start of program
def startup():
    print('===============================')
    print('Welcome to the Mass Rename Tool')
    print('===============================')
    print('Choices:')
    print('    a) Remove a particular string from all files in current directory')
    print('    b) This functionality does not exist yet')
    print('    q) Exit program')
    choice = input('-> ')
    print()
    handleChoice(choice)

# Handle input from startup
def handleChoice(choice):
    if choice == 'a' or choice == 'A':
        print('You have chosen wisely')
        removeMatchingStringsInDirectory()
    elif choice == 'q' or choice == 'Q':
        quit()
    else:
        print('Invalid option')
        print()
        startup()

# Option A: Remove a particular string from all files in current directory
def removeMatchingStringsInDirectory():
    print('Please enter the exact string you would like removed, or quit')
    string = input('-> ')
    print()
    # Be able to quit instead of input string
    if string == 'q' or string == 'Q':
        quit()
    cwd = os.getcwd()
    count = 0
    for filename in os.listdir(cwd):
        # Don't do anthing if directory
        if not os.path.isfile(filename):
            continue
        # Rename by removing string
        if string in filename:
            os.rename(filename, filename.replace(string, ''))
            count += 1
    print('Replaced', count, 'file(s).')
    print('-------------------------------')
    print()
    startup()
 
# Run startup when running this file
if __name__ == "__main__":
    startup()