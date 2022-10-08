from Transact import *
from Queue_h import *
from Device import *
from copy import *
from datetime import datetime
def funcSort(x):
    #M = [x.get_t_e]
    return int(1000*max(x.get_T_e(), x.get_T_g()))
def ask(F):
    res = 0
    for i in F:
        if(i.get_stat() == 0):
            res += 1
    return res

def main():
    print("Ввещдите время моделирования:")
    k1 = 0
    k2 = 0
    osCommandString = "notepad.exe file.txt"
    current_datetime = datetime.now()
    f.write("Время запуска модели:" + str(current_datetime) + "\n")
    f.write("\t\t\tВремя" + "\t\tID" + "\t\t   Действие\n")
    global_time = 0.0
    t_end = int(input())

    time = 0.0
    index = 1

    FEC = []
    # while(t < t_end):
    #     FEC.append(Transact(i, t, -1.0, 0))
    #     i+=1
    #     t += Rand(0, 10)


    j = 0
    D1 = Device(1, 10, 28)
    D2 = Device(2, 9, 28)
    Q1 = Queue_to_device(1, D1)
    Q2 = Queue_to_device(2, D2)
    #FEC.append(Transact(index, time, -1.0, 0))
    global_time = time
    Mq1 = 0
    Mq2 = 0
    while(global_time < t_end):

        #print("______________________________________________________________")
        j = 0;
        #print(ask(FEC))
        #if(len(FEC)>0):

        #    print(max(FEC[0].get_T_e(),FEC[0].get_T_g()), "and", time)
        #if(len(FEC)>0 and FEC[0].get_stat() == 2):
            #flag = 0
        #else:
            #flag = 1
        #if(flag):
        if (len(FEC) <=2 and ask(FEC) == 0):
            #print("добавление нового элемента")
            if(index == 1):
                time = 0.0
            else:
                time += Rand(0, 28)
            tr_gen = copy(Transact(index, time, -1.0, 0))

            FEC.append(tr_gen)
            FEC = sorted(FEC, key=lambda trans: funcSort(trans))
            index += 1


        if(FEC[0].get_stat() == 0):
            Mq1 +=Q1.get_lenght()
            k1+=1
            k2+=1
            Mq2 += Q2.get_lenght()

            CEC = copy(FEC[0])
            FEC.pop(0)
            global_time = CEC.get_T_g()
            time = global_time
            if (global_time > t_end):
                f.write("Мат ожидание очереди: "+str("%.3lf"%((Mq2+Mq1)/index))+"\nДля очереди 1: "+str("%.3lf"%(Mq1/k1))+"\nДля очереди 2: "+str("%.3lf"%(Mq2/k2)))
                print("Model terminated")
                # for i in range(j,len(FEC)):
                #     print("\t\tTRANSACT ID", FEC[i].get_id(), "\t\tcancelled")
                return 0
            if(Q1.get_lenght()+D1.get_stat() <= Q2.get_lenght() + D2.get_stat()):
                CEC.set_stat(1)
                CEC.set_Q_number(1)
                out = "В момент времени   |" + str("%.3lf" % global_time) + "\t| транзакт с ID" + str(CEC.get_id()) + "\t| вошел в очередь номер" + "1" + "\n"
                f.write(out)
                #print(out)
                #print(Q1.get_lenght(), "___", D1.get_stat())
                Q1.add_transact_to_Q(CEC)
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
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
                    #FEC.pop(j)
                    #print(1)
                    #FEC.insert(k-1, Tr_in_D)
            else:
                CEC.set_stat(1)
                CEC.set_Q_number(2)
                out = "В момент времени   |" + str("%.3lf" % global_time) + "\t| транзакт с ID" + str(CEC.get_id()) + "\t| вошел в очередь номер" + '2' + "\n"
                f.write(out)
                #print(out)
                #print(Q1.get_lenght(), "___", D1.get_stat())
                Q2.add_transact_to_Q(CEC)
                #print(Q2.get_lenght())
                if (D2.get_stat() == 0 and Q2.get_lenght() == 1):
                    D2.set_T_g(global_time)
                    Q2.go_to_device()
                    #D2.add_transact_to_D(FEC[j])
                    Tr_in_D = copy(D2.go_out_of_D())
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))

                    #j -= 1
            #j += 1


        elif(FEC[0].get_stat() == 2):

            global_time = FEC[0].get_T_e()
            CEC = copy(FEC[0])

            #time = global_time
            #t += Rand(0, 20)
            #FEC.append(Transact(i, t, -1.0, 0))
            if (global_time > t_end):
                f.write("Мат ожидание очереди: " + str("%.3lf" % ((Mq2 + Mq1) / index)) + "\nДля очереди 1: " + str(
                    "%.3lf" % (Mq1 / k1)) + "\nДля очереди 2: " + str("%.3lf" % (Mq2 / k2)))

                print("Model terminated")
                # for i in range(0,len(FEC)):
                #     if FEC[i].get_stat()<=1:
                #         print("\t\tTRANSACT ID", FEC[i].get_id(), "\t\tcancelled")
                return 0
            FEC[0].end()
            FEC.pop(0)
            if(CEC.get_Q_num() == 1):
                D1.set_stat(0)
                D1.set_T_g(global_time)

                if(Q1.get_lenght()>0):
                    D1.set_T_g(global_time)
                    Q1.go_to_device()
                    # D2.add_transact_to_D(FEC[j])
                    Tr_in_D = copy(D1.go_out_of_D())
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
                    #FEC.pop(j)
            elif(CEC.get_Q_num() == 2):
                D2.set_stat(0)
                D2.set_T_g(global_time)

                if (Q2.get_lenght() > 0):
                    D2.set_T_g(global_time)
                    Q2.go_to_device()
                    # D2.add_transact_to_D(FEC[j])
                    Tr_in_D = copy(D2.go_out_of_D())
                    FEC.append(Tr_in_D)
                    FEC = sorted(FEC, key=lambda trans: funcSort(trans))
                    #FEC.pop(j)

            #j-=1
        #j += 1
    # for j in range(0,len(FEC)):
    #      print(j+1, FEC[j].get_T_g())
    f.write("Мат ожидание очереди: " + str("%.3lf" % ((Mq2 + Mq1) / index)) + "\nДля очереди 1: " + str(
        "%.3lf" % (Mq1 / k1)) + "\nДля очереди 2: " + str("%.3lf" % (Mq2 / k2)))

    return 0
if __name__ == '__main__':
    main()
