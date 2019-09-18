import Persons

if __name__ == "__main__":
        raise Exception("This file is not meant to run by itself")
class Customers(Persons.Person):

    # --Constructor--
    def __init__(self, Id="", FirstName="", LastName=""):
        # Attributes
        self.__Id = Id

        #set the property
        self.Id - Id
        self.FirstName = FirstName
        self.LastName = LastName


    # --Properties--
    # Id
    @property  # getter(accessor)
    def Id(self):
        return self.__Id

    @Id.setter  # (mutator)
    def Id(self, Value):
        self.__Id = Value

    # --Methods--

    def ToString(self):
        """Explictly returns field data"""
        return str(self.Id) + ' - ' + super().ToString()

    def __str__(self):
        """Implictly returns field data"""
        return self.ToString()
        # --End of Class Customer --


