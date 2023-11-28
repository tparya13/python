"""method overloading"""
# class maths:
#     def add(self,a,b):
#         print(a+b)
#     def add(self,a,b,c=0):
#         print(a+b+c)
# ob=maths()
# ob.add(5,3)
# ob.add(5,4,2)   



"""method overriding"""
# class kozhikode:
#     def place(self):
#         print("kappad")
# class koyilandy(kozhikode):
#     def place(self):
#         print("kollam") 
# class vadakara(kozhikode):
#     def place(self):
#         print("kunjipalli")
# a=kozhikode()
# b=koyilandy()
# c=vadakara()
import re
# terms="['a-zA-Z0-9']..."
# x=re.match(terms,"arya") 
# if x:
#     print("matched") 
# else:
#     print("not matched")    
     

#     print("not matched")    
     
"""DOT"""
# import re
# terms="['a-zA-Z0-9']..."
# x=re.match(terms,"arya") 
# if x:
#     print("matched") 
# else:
#     print("not matched")    
     

import re
terms='^arya?$'
x=re.search(terms,"aryaa") 
if x:
    print("matched") 
else:
    print("not matched")    
     