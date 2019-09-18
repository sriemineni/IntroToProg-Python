
class Product:
    
    def __init__(self, PID, Pname, ProPrice):
        self.PID = PID
        self.Pname = Pname
        self.ProPrice = ProPrice

    def PID(self): return self.__PID
    def PID(self,value): self.__PID = Value
    def Pname(self): return self.__Pname
    def Pname(self,value): self.__Pname = Value
    def ProPrice(self): return self.__ProPrice
    def ProPrice(self,value): 
        if value<0 :
            raise Exception("price must be greater than zero")
        else:
            self.__ProPrice = value


    def __str__(self):
        return self.PID + ',' + self. Pname + ','+ self.ProPrice



class datalayer:
    #Data
    objFile = None #File Handle
    strUserInput = None #A string which holds user input

    #Processing
    def WriteProductUserInput(File):
        try:
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while(True):
                strUserInput = input("Enter the Id, Name, and Price (ex.1,ProductA,9.99): ")
                if(strUserInput.lower() == "exit"): break
                else: File.write(strUserInput + "\n")
        except Exception as e:
            print("Error: " + str(e))

    def ReadAllFileData(File, Message="Contents of File"):
        try:
            print(Message)
            File.seek(0)
            print(File.read())
            File.seek(0)
            for row in File:
                list = row.strip().split(',')
                p = Product(list[0], list[1], list[2])
                print(p)
        except Exception as e:
            print("Error: " + str(e))



#I/O
try:
    datalayer.objFile = open("/Users/satya/Documents/Personal stuff/AdvancedPyTraining/Assignment_Sridevi/Product.txt", "r+")
    datalayer.ReadAllFileData(datalayer.objFile, "Here is the current data:")
    datalayer.WriteProductUserInput(datalayer.objFile)
    datalayer.ReadAllFileData(datalayer.objFile, "Here is this data was saved:")
except FileNotFoundError as e:
    print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
   print("Error: " + str(e))
finally:
    if(datalayer.objFile != None):datalayer.objFile.close()