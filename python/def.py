#Python

def subnet_binary(s):
    """ Takes a slash notation subnet and calculates the 
    number of host addresses """
    if s[0] == "/":
        a = int(s.strip("/"))
    else:
        a = int(s)
        addresses = (2**(32-a))
    
    return addresses

s = input("Enter your slash notation. Use a number or a slash (/27 or 27): ")
x = (subnet_binary(s))
print(x)
