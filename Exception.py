#import pickle

try:
    objFile=open("/Users/semineni/Documents/_PythonClass/Assignment07/Exception.txt","r") #making sure I can read or write at the same time
    #objFile.write("Testing read and write at the same time") #writing to file
    strData = objFile.read()# reading the file contents
    print(strData) #printing the data
    objFile.close()
except:
    print("Cant find the file or read")
else:
    print("File successfully processed")
