from Transact import *
from copy import *
class Device:
    def __init__(self, id, t1, t2):
        self.Tr = Transact(0, 0, 0, 0)
        self.Id = id
        self.t1 = t1
        self.t2 = t2
        self.T_g = 0.0
        self.stat = 0
    def add_transact_to_D(self, transact):

        self.Tr = copy(transact)
        self.stat = 1
        self.Tr.set_stat(2)
        out = "В момент времени   |" + str("%.3lf"%self.T_g) + "\t| транзакт с ID" + str(self.Tr.get_id()) +  "\t| вошел в устройство " + str(self.Id)
        f.write(out)
        #print(out)
        #print(out)
    def set_T_g(self, t):
        self.T_g = t
    def go_out_of_D(self):
        #self.stat = 0
        self.Tr.set_T_e(self.T_g + Rand(self.t1, self.t2))
        out = " выйдет в  " + str("%.3lf"%self.Tr.get_T_e()) + "\n"
        f.write(out)
        #print(out)
        #print(out)

        #self.Tr.set_stat()
        return self.Tr
    def get_stat(self):
        return self.stat
    def set_stat(self, s):
        self.stat = s

