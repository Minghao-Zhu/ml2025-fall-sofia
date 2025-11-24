import numpy as np
import sklearn

while True:
    N = input("Please enter a positive integer to start:")
    if N.isdigit() and float(N)//1 == float(N) and float(N)>=1:
        x_array = np.empty(int(N), dtype=int)
        y_array = np.empty(int(N), dtype=int)
        N = int(N)
        get_all_input = True
        for i in range(1,N+1):
            tmp = input("please enter the " + str(i) + "th x number:")
            if not tmp.isdigit() or (int(tmp)!=1 and int(tmp)!=0):
                print("your input " + str(tmp) + " is not 0 or 1, please try again")
                get_all_input = False
                break
            else:
                x_array[i-1] = int(tmp)
            tmp = input("please enter the " + str(i) + "th y number:")
            if not tmp.isdigit() or (int(tmp) != 1 and int(tmp) != 0):
                print("your input " + str(tmp) + " is not 0 or 1, please try again")
                get_all_input = False
                break
            else:
                y_array[i - 1] = int(tmp)
        if not get_all_input:
            continue

        precision = sklearn.metrics.precision_score(y_array, x_array)
        recall = sklearn.metrics.recall_score(y_array, x_array)
        #precision, recall, f1score, support = sklearn.metrics.precision_recall_fscore_support(y_array, x_array)
        print("precision: " + str(precision))
        print("recall: " + str(recall))
    else:
        print("your input " + str(N) + " is not a positive integer, please try again")
        continue

