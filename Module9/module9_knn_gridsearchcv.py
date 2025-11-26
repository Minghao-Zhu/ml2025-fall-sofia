import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score


def get_input(character ):
    while True:
        N = input("Please enter a positive integer "+ character + ":")
        if N.isdigit() and float(N) // 1 == float(N) and float(N) >= 1:
            x_array = np.empty(int(N), dtype=float)
            y_array = np.empty(int(N), dtype=int)
            N = int(N)
            get_all_input = True
            for i in range(1, N + 1):
                tmp = input("please enter the " + str(i) + "th x number:")
                if not tmp.isdigit():
                    print("your input " + str(tmp) + " is not digit, please try again")
                    get_all_input = False
                    break
                else:
                    x_array[i - 1] = int(tmp)
                tmp = input("please enter the " + str(i) + "th y number:")
                if not tmp.isdigit() or (int(tmp) < 0) or (float(tmp) // 1 != float(tmp)):
                    print("your input " + str(tmp) + " is not non negative integer, please try again")
                    get_all_input = False
                    break
                else:
                    y_array[i - 1] = int(tmp)
            if not get_all_input:
                continue
        else:
            print("your input " + str(N) + " is not a positive integer, please try again")
            continue
        return x_array, y_array

x_train, y_train = get_input("N")
x_test, y_test = get_input("M")

x_train = x_train.reshape(-1, 1)
x_test = x_test.reshape(-1, 1)

min_len = min(len(x_train), len(x_test))
param_grid = {'n_neighbors': range(1, 10)}
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=3, scoring='accuracy')
grid_search.fit(x_train, y_train)
best_k = grid_search.best_params_['n_neighbors']
print("Best k value is: "+ str(best_k))
y_pred = grid_search.best_estimator_.predict(x_test)
test_accuracy = accuracy_score(y_test, y_pred)
print("Test accuracy is: " + str(test_accuracy))
print("Predictions are: " + str(y_pred))


