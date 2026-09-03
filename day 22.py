'''
                                   ABSTRACTION
                                   -----------
                                   -----------

- abstraction means hiding the implemented data and showing only needed data to the user

ABC -> Abstract Base Class
- the abstract method is mainly used to hide that particular information of a base class
-----------------------------------------------------------
from abc import ABC, abstractmethod
class gov_bank(ABC):
    @abstractmethod
    def interest(self):
        print("Government interest is 3.5")

class SBI_bank(gov_bank):
    def interest(self):
        print("SBI bank interest is 7.8")

class ICICI_bank(gov_bank):
    def interest(self):
        print("ICICI bank interest is 8.8")

obj = SBI_bank()
obj.interest()

obj1 = ICICI_bank()
obj1.interest()
'''
from abc import ABC, abstractmethod
class cls_fee():
    @abstractmethod
    def free_str(self):
        print("college fee 45000")

class manag(cls_fee):
    