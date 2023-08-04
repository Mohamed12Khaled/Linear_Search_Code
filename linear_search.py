def linear_search(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return True
    return False
l=[17,229,32,4,1,34,5,2,1]
print(linear_search(l,2))