#Imports
import Customer, FileManager



if __name__!="__main__":
    raise Exception("This is meant to be run by itself")

ObjC1 = Customer.Customers(Id=101, FirstName="Sri", LastName="Emineni")
ObjC2 = Customer.Customers(Id=102, FirstName="Satya", LastName="Veeranki")

lstCustomers = [ObjC1, ObjC2]

ObjF = FileManager.File(FileName="CustomerData.txt")
for i in lstCustomers:
    print(i.ToString())
    ObjF.TextData = i.ToString() + "\n"
    ObjF.SaveData()
