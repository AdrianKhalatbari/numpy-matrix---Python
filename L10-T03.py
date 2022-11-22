import numpy
import numpy as np

print('This program demonstrates use of numpy-matrix.')
rows = int(input('Enter amount of rows:\n'))
columns = int(input('Enter number of columns:\n'))
# ///////////Show Zero matrix
zeors_array = np.zeros((rows, columns), dtype='i')
print('Zero-matrix of the given rows & columns is:\n' , zeors_array)
# /////////////Change the rows and columns
print('Matrix printed with np-formatting:')
newArray = np.zeros((rows, columns), dtype='i')
for i in range(rows):
    for j in range(columns):
        newArray[i][j] = (i + 1) * (j + 1)
print(newArray)
# /////////////////Sort the matrix
print('\nMatrix sorted into one array:')
newArray = (numpy.sort(newArray))
np.round(newArray.transpose()).astype(int)
sortedList = []
for x in newArray:
    for y in x:
        sortedList.append(y)
print(numpy.sort(sortedList))
# ////////////////////Show with semicolons
print('Matrix printed with elements separated by semicolons:')
for x in newArray:
    output = str(x).replace("[ ", "")
    output = str(output).replace("[", "")
    output = str(output).replace("]", "")
    output = str(output).replace("  ", " ")
    output = str(output).replace(" ", ";")
    output = output + ";"
    print(output)
print("")
# //////////////////////Create a new Shape
while (True):
    try:
        print('Shaping the matrix. Please, enter the new dimensions.')
        newRows = int(input("Enter amount of new rows:\n"))
        newColumns = int(input("Enter amount of new columns:\n"))
        newArray.shape = (newRows, newColumns)
        print('Newly shaped matrix is:\n' , newArray)
        # print(newArray)
        break
    except ValueError:
        print('Faulty shape. Please, try again.')
# /////////////////Print max
print('Largest number in the matrix is: ' + str(np.max(newArray)))
print('Smallest number in the matrix is: ' + str(np.min(newArray)))
print('Sum of all values in the matrix is: ' + str(np.sum(newArray)))
# ////////////////////Get list from user and sort it and remove the duplicated
list_values = [int(item) for item in input("Enter the list items: \n").split()]
print('Unique values are: ' + str(np.unique(list_values)))
