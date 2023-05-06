import sys
itemList = { #Dictionary containing list
    1: 'Groceries',
    2: 'Pringles',
    3: 'IDFK This is a test'
    }
def printList(): #This function takes all items in itemList and prints them
    for x in itemList:
        print(str(x) + '.' + str(itemList[x]))
    return 'Done'

def userOptions(): #Lists the users options, takes input, then acts accordingly
    print(' ')
    print('This is your list. What would you like to do now?')
    print('1. Add Item')
    print('2. Remove Item')
    print('3. Save and exit')

    try:
        userInput = input() #Takes user input
        userInput = int(userInput)

        if userInput == 1: #Asks user for item name then adds item to list
            print('What is the name of the item?')
            itemName = input()
            currItemNum = 0
            for x in itemList:
                currItemNum = currItemNum + 1
            itemNum = currItemNum + 1
            itemList[itemNum] = itemName
            printList()
            userOptions()

        else: #Gives error message for a value not specified
            print('Unexpected Value')

    except ValueError: #Gives an error if the user enters anything but a whole number
        print('You did not enter a whole number.')
        userOptions()

    except: #Gives an error for anything else that would otherwise crash the program
        print('Something went wrong')
        userOptions()

printList()
userOptions()

