import re
def match(first_string,second_string):
    a = re.findall(r'[0-9]',first_string) 
    b = re.findall(r'[0-9]',second_string) 
    
    if a == b:
        return True
    else:
        return False

first_string = input("Enter first string: ")
second_string = input("Enter second string: ")

flag = match(first_string,second_string)
if flag:
    print("Strings are matched")
else:
    print("Strings are not matched")
