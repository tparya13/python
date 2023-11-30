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
# import re
# terms="hel{2}o"
# x=re.search(terms,"hello synnefo")
# if x:
#     print("matched") 
# else:
#     print("not matched")    
 
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


# import re
# terms="['a-zA-Z0-9']..."
# x=re.match(terms,"arya") 
# if x:
#     print("matched") 
# else:
#     print("not matched")

    
# import re
# terms="hel{2}o"
# x=re.search(terms,"hello synnefo")
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
   
     

# import re
# terms='^arya?$'
# x=re.search(terms,"aryaa") 
# if x:
#     print("matched") 
# else:
#     print("not matched") 
   
     
     
# import re
# terms="hel{2}o"
# x=re.search(terms,"hello synnefo")
# if x:
#     print("matched") 
# else:
#     print("not matched")  

  
     
# import re
# terms="hel{2}o"
# x=re.search(terms,"helo synnefo")
# if x:
#     print("matched") 
# else:
#     print("not matched")

    
 
# import re
# terms="\d"
# x=re.search(terms,"2rya")
# if x:
#     print("matched") 
# else:
#     print("not matched")        


# import re
# terms="^[^h]ello"
# x=re.search(terms,"hello synnefo")                                                                                                      ello synnefo")
# if x:
#     print("matched") 
# else:
#     print("not matched") 



# import re
# terms="^[5-9]\d{9}$"
# x=re.search(terms,"5578156789")
# if x:
#     print("validate") 
# else:
#     print("not validate")   



# import re
# a=str(input("enter the user name: "))
# terms="^[a-zA-Z]\w{3,25}$"
# x=re.search(terms,a)
# if x:
#     print("validate") 
# else:
#     print("not validate")
 


"""date"""
# import re
# a=str(input("enter the date: "))
# terms="(^[012]\d|3[01])-([0]\d|1[012])-\d{4}$"
# x=re.search(terms,a)
# if x:
#     print("validate") 
# else:
#     print("not validate")  
  



# import re
# a=str(input("enter the date: "))
# terms="^([^00]|[0][1,9]|[12][1,9]|3[1]|[123][0])(-|.|/)([^00]|[0][1,9]|1[012])|(-|.|/)([^0000]\d{4}|$"
# x=re.search(terms,a)
# if x:
#     print("validate") 
# else:
#     print("not validate")    
    
    
    
import re
a=str(input("enter the email: "))
terms="^([a-zA-Z]{12}\d{3})[@]([a-z]{10}[.])([in]|[com])$"
x=re.search(terms,a)
if x:
    print("validate") 
else:
    print("not validate")  
  
    
     
       
     
              
     
       
     