import textwrap
from datetime import date

class CreditCard:
    def __init__(self, expiryMonth, expiryYear, firstName, lastName, ccNumber):
        self.__expiryMonth = expiryMonth
        self.__expiryYear = expiryYear
        self.__firstName = firstName
        self.__lastName = lastName
        self.__ccNumber = ccNumber

    def formatExpiryDate(self):
        self.date = str(self.__expiryMonth) + "/" + str(self.__expiryYear)[-2:]
        print(self.date)

    def formatFullName(self):
        self.name = self.__firstName + " " +self.__lastName
        print(self.name)

    def formatCCNumber(self): 
        self.number = " ".join(textwrap.wrap(self.__ccNumber,4))
        print(self.number)

    def isValid(self):
        today = date.today()
        if (today.year, today.month) > (self.__expiryYear, self.__expiryMonth):
            print("The card has expired.")
            return False
        else:
            print("The card is still valid.")
            return True

cc1 = CreditCard(10, 2014, "Bob", "Jones", "1234567890123456")
cc1.formatExpiryDate()
cc1.formatFullName()
cc1.formatCCNumber()
cc1.isValid()