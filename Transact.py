from random import *
from copy import *
def Rand(t1, t2):
    return uniform(t1, t2)
f = open('Результат_моделирования.txt', 'w')
class Transact:
    def __init__(self, id, T_g, T_e, stat):
        self.id = id
        self.T_g = T_g
        self.T_e = T_e
        self.stat = stat
        self.Q_number = 0
    def set_Q_number(self, n):
        self.Q_number = n
    def set_id(self, i):
        self.id = i
    def set_T_g(self, t):
        self.T_g = t
    def set_T_e(self, t):
        self.T_e = t
    def set_stat(self, s):
        self.stat = s
    def get_id(self):
        return self.id
    def get_T_g(self):
        return self.T_g
    def get_T_e(self):
        return self.T_e
    def get_stat(self):
        return self.stat
    def get_Q_num(self):
        return self.Q_number
    def end(self):
        #self.stat = -1
       # if(self.stat == 2):
        out = "В момент времени   |" + str("%.3lf"%self.T_e) + "\t| транзакт с ID" + str(self.id) + "\t| вышел из устройства" + str(self.Q_number) + "\n"
        f.write(out)
        #print(out)
        #print(out)


