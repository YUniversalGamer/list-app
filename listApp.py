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

    
    userInput = int(input()) #Takes user input
#Asks user for item name then adds item to list
    if userInput == 1: 
        print('What is the name of the item?')
        itemName = input()
        currItemNum = 0
        for x in itemList:
            currItemNum = currItemNum + 1
        itemNum = currItemNum + 1
        itemList[itemNum] = itemName
        printList()
        userOptions()
#Asks user for item number then removes item from list
#Also brings the rest of the list up to fill the gap
    elif userInput == 2: 
        print('What item would you like to remove?')
        userSelect = int(input())
        totalItemNum = 0
        for x in itemList:
            totalItemNum = totalItemNum + 1

        for x in range(userSelect, totalItemNum):
            itemList[x] = itemList[x + 1]
        itemList.pop(totalItemNum)
        printList()
        userOptions()

    elif userInput == 3:
        with open('list.txt', 'w') as f:
            f.write('Test')
            f.close()
                
            

    else: #Gives error message for a value not specified
            print('Unexpected Value')

    #except ValueError: #Gives an error if the user enters anything but a whole number
        #print('You did not enter a whole number.')
        #userOptions()

    #except: #Gives an error for anything else that would otherwise crash the program
        #print('Something went wrong')
        #userOptions()

printList()
userOptions()

