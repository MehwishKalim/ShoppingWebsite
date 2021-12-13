def mainMenu():
    while True:
        print("***Shopping List***")
        print("Select the number from the giving options")
        print("1.View Shopping list")
        print("2.add items to the shopping list")
        print("3.Remove items from the shopping list")
        print("4.Check item is in the shopping list")
        print("5.View the shopping Cart")
        print("6.Clear shopping list")


        selection = input("Choose an option:")
        if selection == "1":
            displayList()


        elif selection == "2":
             addItem()

        elif selection == "3":
             removeItem()

        elif selection == "4":
            checkItem()

        elif selection == "5":
            viewCart()

        elif selection == "6":
            clearList()

        else:
            print("not valid")

#shopping_list = ["apples", "oranges", "carrots"]
shopping_list = {}
def displayList():
    print()
    print("SHOPPING LIST")
    for i in shopping_list:
        print("*" + i)

def addItem():
    #item = input("Enter item from the shopping list:")
    #shopping_list.append(item)
    #print(item + " has been added in the cart")
    #print(shopping_lis

    item = input("Enter an item:")

    if item in shopping_list:
        print("Item already the shopping  ")
        qnty = int(input("Enter the quantity"))
        shopping_list[item] = shopping_list[item] + qnty
    else:
        qnty = int(input("enter the quantity"))
        shopping_list[item] = qnty
        print(item + " added")
        print(shopping_list)

def removeItem():
    item = input("Which im you like to remove from the cart:")
    if item in shopping_list:
        qnty = int(input("how many quantity"))
        shopping_list[item] = shopping_list[item] - qnty
    else:
        del(shopping_list[item])
    #shopping_list.remove(item)
    #print(item + " has removed from the cart")


    print(shopping_list)

def checkItem():
    item = input("what item would you like to add in the list:")
    if item in shopping_list:
        print("yes" + item + " is in the shoppinglist")
    else:
        print("no, not available")
def viewCart():
    #print("there are" ,len(shopping_list), "items on the shoppinglist.")
    for item in shopping_list:
        print(item, ":" , shopping_list[item])

def clearList():
    shopping_list.clear()
    print("The shopping list is empty")


mainMenu()