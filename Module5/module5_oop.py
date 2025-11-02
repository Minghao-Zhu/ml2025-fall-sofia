
while True:
    N = input("Please enter a positive integer:")
    if N.isdigit() and float(N)//1 == float(N) and float(N)>=1:
        N_list = []
        N = int(N)
        get_all_input = True
        for i in range(1,N+1):
            tmp = input("please enter the " + str(i) + "th number:")
            if not tmp.isdigit() or float(tmp)//1 != float(tmp):
                print("your input " + str(tmp) + " is not an integer, please try again")
                get_all_input = False
                break
            else:
                N_list.append(int(tmp))
        if not get_all_input:
            continue
        X = input("please enter the number you want to find:")
        if not X.isdigit() or float(X)//1 != float(X):
            print("your input " + str(X) + " is not an integer, please try again")
            continue
        else:
            X = int(X)
            if X in N_list:
                print(N_list.index(X)+1)
            else:
                print(-1)
            break
    else:
        print("your input " + str(N) + " is not a positive integer, please try again")
        continue

