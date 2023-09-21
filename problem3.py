# program to validate an IP address. Given a string, write a function to check if it is a valid IP address or not. If valid, return true, otherwise return false.

def validate_ip(ip):
    l=ip.split('.')
    if len(l)!=4:
        return False
    for i in l:
        if i.isnumeric():
            if int(i)<0 or int(i)>255:
                return False
        else:
            return False
    return True