#create 5 test case for the sort_s function
from problem1 import sort_s
def test_sort_s_1():
    assert sort_s('hello world')=='llloohe wrd'

def test_sort_s_2():
    assert sort_s('tree')=='eetr'

def test_sort_s_3():
    assert sort_s('')==''

def test_sort_s_4():
    assert sort_s('a')=='a'

def test_sort_s_5():
    assert sort_s('aa')=='aa'


test_sort_s_1()
test_sort_s_2()
test_sort_s_3()
test_sort_s_4()
test_sort_s_5()
