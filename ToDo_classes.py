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

class fileprocessor():

    def display_data():
        print("Current items in the todo list are :\n")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")

    def add_item():
        dicRow = {"Task": strTask, "Priority": strPriority}
        lstTable.append(dicRow)

    def remove_item(strkeytoremove):
        toberemoved= False  # Creating a boolean Flag
        intRowNumber = 0
        while (intRowNumber < len(lstTable)):
            if (strkeytoremove == str(
                    list(dict(lstTable[intRowNumber]).values())[0])):  # the values function creates a list!
                del lstTable[intRowNumber]
                toberemoved = True
            intRowNumber += 1
        return toberemoved

    def save_to_file():
        objFile = open(objFileName, "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()






while(True):
    print ("""\nMenu of Options\n1) Show current data\n2) Add a new item.\n3) Remove an existing item.\n4) Save Data to File\n5) Exit Program\n""")
    strChoice = str(input("Please choose an option [1 to 4] - \n"))


    if (strChoice.strip() == '1'):
        fileprocessor.display_data()


    # Step 4
    # Add a new item to the list/Table
    elif(strChoice.strip() == '2'):
        strTask = str(input("What is the task? - ")).strip()
        strPriority = str(input("What is the priority? [high|low] - ")).strip()
        fileprocessor.add_item()
        #print("Current Data in table:")
        #for dicRow in lstTable:
            #print(dicRow)
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
            print("*******************************************")
        continue  # to show the menu

    # Step 5
    # Remove a new item to the list/Table
    elif(strChoice == '3'):
        #5a-Allow user to indicate which row to delete
        strkeytoremove = input("Which TASK would you like removed? - ")
        blnItemRemoved = fileprocessor.remove_item(strkeytoremove)
        if(blnItemRemoved == True):
            print("The task was removed.")
        else:
            print("I'm sorry, but I could not find that task.")

        #5c Show the current items in the table
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        continue


    elif(strChoice == '4'):
        print("******* The current items ToDo are: *******")
        for row in lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")
        print("*******************************************")
        #5b Ask if they want save that data
        if("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            fileprocessor.save_to_file()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved, but previous data still exists! Press the [Enter] key to return to menu.")
        continue #to show the menu

        
    elif (strChoice == '5'):
        break #and Exit the program

