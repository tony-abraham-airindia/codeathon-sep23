from problem2 import maximum_profit

#test case for testing maximum_profit function
def test_maximum_profit_1():
    assert maximum_profit([9,11,8,5,7,10])==5


def test_maximum_profit_2():
    assert maximum_profit([100,180,260,310,40,535,695])==655

def test_maximum_profit_3():
    assert maximum_profit([100,90,80,70,60,50])== -1

def test_maximum_profit_4():
    assert maximum_profit([100,90,80,70,60,50,100])==50


test_maximum_profit_1()
test_maximum_profit_2()
test_maximum_profit_3()
test_maximum_profit_4()
