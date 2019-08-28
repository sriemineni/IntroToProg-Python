import pickle
try:
    objFileData = [None]
    intId = int(input("Enter an Id: "))
    strName = str(input("Enter a Name: "))
    lstCustomer = [intId, strName]
    #print(lstCustomer)

    #Now we store the data with the pickle.dump method
    objFile=open("/Users/semineni/Documents/_PythonClass/Assignment07/Exception2.dat","ab") #making sure I can read or write at the same time
    pickle.dump(lstCustomer, objFile)
    objFile.close()

    objFile = open("/Users/semineni/Documents/_PythonClass/Assignment07/Exception2.dat","rb")
    objFileData.clear()
    while(True):
        objFileData += pickle.load(objFile)  # Note that load() only load one row of data
except EOFError as e:
    print(objFileData)

except:
    print("cant find the file")

else:
    print("Successfully written to file")
    print(objFileData)
objFile.close()