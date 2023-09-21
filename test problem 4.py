#test case for validating sort_list funtion
from problem4 import sort_list

def test_sort_list_1():
    assert(sort_list([1,3,2])==[1,2,3])

def test_sort_list_2():
    assert(sort_list([1,3,2,4,5,6,3,7,8,9])==[1,2,3,3,4,5,6,7,8,9])

def test_sort_list_3():
    assert(sort_list([1,2,3,4,5,6,7,8,9])==[1,2,3,4,5,6,7,8,9])

#test case with 50000 elements
def test_sort_list_4():
    list_number=[]
    for i in range(50000):
        list_number.append(i)
    assert(sort_list(list_number)==list_number)

def test_sort_list_5():
    assert(sort_list([1,2,3,4,5,6,7,8,9])==[1,2,3,4,5,6,7,8,9])

    
test_sort_list_1()
test_sort_list_2()
test_sort_list_3()
test_sort_list_4()
test_sort_list_5()
