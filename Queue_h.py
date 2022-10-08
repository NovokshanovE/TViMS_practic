from Transact import *
from Device import *
from copy import *
class Queue_to_device:
    def __init__(self, i, D):
        self.Q = []
        self.Id = i
        self.D = D
    def add_transact_to_Q(self, new_Tr):
        self.Q.append(new_Tr)
    def go_to_device(self):
        self.D.add_transact_to_D(self.Q[0])
        self.Q.pop(0)
    def get_lenght(self):
        return len(self.Q)
    def get_ID(self):
        return self.Id
