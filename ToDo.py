objFileName = "/Users/semineni/Documents/_PythonClass/Assignment05/Todo.txt"
strData = ""
dicRow = {}
lstTable = []

objFile = open(objFileName, "r")
for line in objFile:
    strData = line.split(",") # readline() reads a line of the data into 2 elements
    dicRow = {"Task":strData[0].strip(), "Priority":strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

while(True):
    print ("""\nMenu of Options\n1) Show current data\n2) Add a new item.\n3) Remove an existing item.\n4) Save Data to File\n5) Exit Program\n""")
    strChoice = str(input("Please choose an option [1 to 4] - \n"))


    if (strChoice.strip() == '1'):
        print("Current items in the todo list are :\n")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    # Step 4
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        dicRow = {"Task":strTask,"Priority":strPriority}
        lstTable.append(dicRow)
        print("Current Data in table:")
        for dicRow in lstTable:
            print(dicRow)

        #4a Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue #to show the menu

    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        #5a-Allow user to indicate which row to delete
        strKeyToRemove = input("Which TASK would you like removed? - ")
        blnItemRemoved = False #Creating a boolean Flag
        intRowNumber = 0
        while(intRowNumber < len(lstTable)):
            if(strKeyToRemove == str(list(dict(lstTable[intRowNumber]).values())[0])): #the values function creates a list!
                del lstTable[intRowNumber]
                blnItemRemoved = True
            #end if
            intRowNumber += 1
        #end for loop
        #5b-Update user on the status
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        #5c Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue #to show the menu

    # Step 6
    # Save tasks to the ToDo.txt file
    elif(strChoice == '4'):
        #5a Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(objFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue #to show the menu
    elif (strChoice == '5'):
        break #and Exit the program

