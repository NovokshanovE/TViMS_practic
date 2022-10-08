from Transact import *
#from prt import *

from Queue_h import *
from Device import *
from copy import *
from datetime import datetime
def funcSort(x):
    #M = [x.get_t_e]
    return int(1000*max(x.get_T_e(), x.get_T_g()))
def main():
    print("Ввещдите время моделирования:")

    osCommandString = "notepad.exe file.txt"
    current_datetime = datetime.now()
    f.write("Время запуска модели:" + str(current_datetime) + "\n")
    f.write("\t\t\tВремя" + "\t\tID" + "\t\t   Действие\n")
    #log = mylogger("res.txt", True)
    #print = log.printml()
    global_time = 0.0
    t_end = int(input())
    t = 0.0
    i = 1
    FEC = []
    while(t < t_end):

        FEC.append(Transact(i, t, -1.0, 0))
        i+=1
        t += Rand(0, 28)

    for j in range(0,len(FEC)):
        (FEC[j].get_T_g())

    j = 0
    D1 = Device(1, 10, 28)
    D2 = Device(2, 9, 28)
    Q1 = Queue_to_device(1, D1)
    Q2 = Queue_to_device(2, D2)
    while(j < len(FEC)):
        if(FEC[j].get_stat() == 0):

            global_time = FEC[j].get_T_g()
            if (global_time > t_end):
                f.write("End model")
                return 0
            if(Q1.get_lenght()+D1.get_stat() <= Q2.get_lenght() + D2.get_stat()):
                FEC[j].set_stat(1)
                FEC[j].set_Q_number(1)
                out = "В момент времени   |" + str("%.3lf"%global_time) + "\t| транзакт с ID" + str(FEC[j].get_id()) + "\t| вошел в очередь номер" + "1" + "\n"
                f.write(out)
                Q1.add_transact_to_Q(FEC[j])
                #print(Q1.get_lenght())
                if(D1.get_stat() == 0 and Q1.get_lenght() == 1):
                    D1.set_T_g(global_time)
                    Q1.go_to_device()

                    #D1.add_transact_to_D(FEC[j])
                    Tr_in_D = copy(D1.go_out_of_D())
                    #k = 0
                   # while(Tr_in_D.get_T_e() > FEC[j].get_T_g() or (Tr_in_D.get_T_e() > FEC[j].get_T_e() and FEC[j].get_stat()==2)):
                       # k+=1
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key = lambda trans: funcSort(trans))
                    #print(1)
                    #FEC.insert(k-1, Tr_in_D)

            else:
                FEC[j].set_stat(1)
                FEC[j].set_Q_number(2)
                out = "В момент времени   |" + str("%.3lf"%global_time) + "\t| транзакт с ID" + str(FEC[j].get_id()) + "\t| вошел в очередь номер" + '2' + "\n"
                f.write(out)
                Q2.add_transact_to_Q(FEC[j])
                #print(Q2.get_lenght())
                if (D2.get_stat() == 0 and Q2.get_lenght() == 1):
                    D2.set_T_g(global_time)
                    Q2.go_to_device()

                    #D2.add_transact_to_D(FEC[j])
                    Tr_in_D = copy(D2.go_out_of_D())
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
        elif(FEC[j].get_stat() == 1):
            global_time = FEC[j].get_T_g()
            if (global_time > t_end):
                f.write("End model")
                return 0
            if(FEC[j].set_Q_number()==1):
                if (D1.get_stat() == 0 and Q1.get_lenght() == 1):
                    D1.set_T_g(global_time)
                    Q1.go_to_device()

                    #D1.add_transact_to_D(FEC[j])
                    Tr_in_D = copy(D1.go_out_of_D())
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
            else:
                if (D2.get_stat() == 0 and Q2.get_lenght() == 1):
                    D2.set_T_g(global_time)
                    Q2.go_to_device()

                    #D2.add_transact_to_D(FEC[j])
                    Tr_in_D = copy(D2.go_out_of_D())
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
        elif(FEC[j].get_stat() == 2):
            global_time = FEC[j].get_T_e()
            if (global_time > t_end):
                f.write("End model")
                return 0
            if(FEC[j].get_Q_num() == 1):
                D1.set_stat(0)
                D1.set_T_g(global_time)
                if(Q1.get_lenght()>0):
                    D1.set_T_g(global_time)
                    Q1.go_to_device()

                    # D2.add_transact_to_D(FEC[j])
                    Tr_in_D = D1.go_out_of_D()
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
            elif(FEC[j].get_Q_num() == 2):
                D2.set_stat(0)
                D2.set_T_g(global_time)
                if (Q2.get_lenght() > 0):
                    D2.set_T_g(global_time)
                    Q2.go_to_device()

                    # D2.add_transact_to_D(FEC[j])
                    Tr_in_D = D2.go_out_of_D()
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
            FEC[j].end()
        j += 1
    f.close()
    print(len(FEC))
    #os.startfile("Результат_моделирования.txt")
    #os.system(osCommandString)
    #subprocess.call(['notepad.exe', "Результат_моделирования.txt"])
    return 0
if __name__ == '__main__':
    main()
