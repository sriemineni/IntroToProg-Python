
if __name__ == "__main__":
    raise Exception("This file is not meant to run by itself")


# --- Make the class ---
class Person(object):
    """ Base Class for Personal data """


    # --Fields--
    #__FirstName
    #__LastName


    # --Constructor--
    def __init__(self, FirstName="", LastName=""):
        # Attributes
        self.__FirstName = None  # Private Attribute
        self.__LastName = None  # Private Attribute

        self.FirstName = FirstName
        self.LastName = LastName

    # --Properties--
    # FirstName
    @property  # getter(accessor)
    def FirstName(self):
        return self.__FirstName

    @FirstName.setter  # (mutator)
    def FirstName(self, Value):
        self.__FirstName = Value

    # LastName
    @property  # getter(accessor)
    def LastName(self):
        return self.__LastName

    @LastName.setter  # (mutator)
    def LastName(self, Value):
        self.__LastName = Value

    # --Methods--
    def ToString(self):
        """Explictly returns field data"""
        return self.FirstName + " " + self.LastName

    def __str__(self):
        """Implictly returns field data"""
        return self.ToString()



    # --End of class Person--
