#test cases for testing validate_ip function:

# 255.255.0.0	true
# 555.555.555.555	false
# 256.255.0.0	false
from problem3 import validate_ip

def test_validate_ip_1():
    assert(validate_ip('255.255.0.0')==True)

def test_validate_ip_2():
    assert(validate_ip('555.555.555.555')==False)

def test_validate_ip_3():
    assert(validate_ip('256.255.0.0')==False)

def test_validate_ip_4():
    assert(validate_ip('-1.22,23.23.23')==False)

def test_validate_ip_5():
    assert(validate_ip('')==False)


test_validate_ip_1()
test_validate_ip_2()
test_validate_ip_3()
test_validate_ip_4()
test_validate_ip_5()