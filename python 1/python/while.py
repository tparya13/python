# 1i=1
# while i<=10:
#     print(i)
#     i+=1  
    
# i=1   
# while i<=9:
#     print(i)
#     i+=2           


# i=2
# while i<=10:
#     print(i)
#     i+=2


# i=10
# while i>=1:
#     print(i)
#     i-=1


# i=9
# while i>=1:
#     print(i)
#     i-=2


# i=10
# while i>=2:                  
#     print(i)
#     i-=2



"""FOR LOOP"""


# for i in range(10):
#     print(i)


# for i in range(2,11,2):
#     print(i,end="")    


# for i in range(1,11,2):
#     print(i,end="")



# a=int(input("enter starting range:"))
# b=int(input("enter ending range:"))
# for a in range(2,b,a+1):
#     print(a)
# s=sum(range(2,b,a+1))
# print("sum =",s)
    
    
    
# for i in range(1,6):
#     for j in range(1,6):
#         print(j,end="")
#     print("/n")  
    
    
# for i in range(1,6):
#     for j in range(1,i+1):  
#         print(j,end="")
#     print("/n") 



# for i in range(1,6):
#     for j in range(1,i+1):  
#         print(i,end="")
#     print("/n")  
       
        
        
        
# ls=[]
# for i in range(2,101,2):
#     ls.append(i)
# print(ls)    
        
           
           
# ls=[]
# for i in range(1,101,2):
#     ls.append(i)
# print(ls)           



# ls=[]
# for i in range(1,101):  
#     if i%3==0:
#         i=("fizz" and "buzz")
#     ls.append(i)
# print(ls)    



# ls=[]
# for i in range(1,101):  
#     if i%5==0:
#         i=("fizz" and "buzz")
#     ls.append(i)
# print(ls)    



# ls=[]
# for i in range(1,101):  
#     if i%3==0:
#         i="fizz"
#     elif i%5==0:
#         i="buzz"     
#     ls.append(i)
# print(ls)    




# for i in range(1,6): 
#     for j in range(i):
#         print("*",end="")
#     print("\n")        



# ls=[]
# for i in range(1,101):  
#     if i%3==0 and i%5==0:
#         ls.append("fizzbuzz")
#     elif i%5==0:
#         ls.append("buzz")
#     elif i%3==0:
#         ls.append("fizz")
#     else:       
#         ls.append(i)
    
# print(ls)    



# for i in range(1,6): 
#     for j in range(i):
#         print("*",end="")
#     print("\n")  
# for i in range(4,0,-1): 
#     for j in range(i):
#         print("*",end="")
#     print("\n")        


# ls=[1,2,3,4,5,6,7,8,9,10]
# even_cound,odd_count=0,0
# for i in ls:
#     if i%2==0:
#         even_cound+=1
#     else:
#         odd_count+=1
# print("even number in the list: ",even_cound) 
# print("odd number in the list: ",odd_count)           



# even=0
# odd=0
# for i in range(1,11):
#     if i%2==0:
#         even=even+1
        
#     else:
#         odd=odd+1
        
# print("odd",odd)
# print("even",even)    



# for i in range(0,7):
#     if(i==3 or i==6):
#         continue
#     print(i,end="")  
# print("\n")     


  
# number=int(input("enter the number: "))
# sum=0
# for value in range(1,number+1):
#     sum=sum+value
# print(sum)  



# n=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(n,end="")
#         n=n+1
#     print()    



# n=int(input("enter the number: "))
# if n<0:
#     print("enter a positive number")
# else:
#     sum=0
#     while(n>0):
#         sum+=n
#         n-=1
#     print("the  sum is: ",sum)    



# i=0
# j=1
# while j<50:
#     print(j,end = "")
#     i,j=j,i+j    



# ls=[10,20,30,20,10,1,3]
# print(ls[4])
# print(ls[:-1])
# print(ls[-1:])
# print(ls[2:6:3])



"""list comprehension"""



# ls1=[10,20,30,20,10,1,3]
# ls2=[i**2 for i in ls1]
# print(ls2)



"""string functions"""

# s="synnefo solutions"
# print(len(s))
# print(s.upper())
# print(s.lower())
# print(s.strip())
# s="      synnefo solutions       "
# print(s.replace("synnefo","novavi"))
  
"""split"""

# s="apple,orange,graps,mango"
# print(s.split(","))
# s="apple_orange_graps_mango"
# print(s.split("_"))
# print(s.startswith("app"))
# print(s.endswith("mangos"))

# s="apple orange graps mango"
# print(s.find("s"))



"""function with return"""
 
# def add():
#     a,b=10,20
#     print(a+b)
# print(add())
# print(type(add()))     


# def add():
#     a,b=10,20
#     return a+b
# print(type(add()))
    
    
    
"""function with arguments and return"""

# def add(a,b):
#     return a+b
# x=add(3,5)
# print(x)    


# l=int(input("enter the length: "))
# w=int(input("enter the width: "))
# def area(l,w):
#     return l*w
# area=area(l,w)
# print("area=",area)    

"""area"""
# s=int(input("enter a number: "))
# r=int(input("enter a number: "))
# def add(s,r):
#     return s+r
# add=add(s,r)
# print("add=",add)

"""even or odd"""
# r=int(input("enter the radius: "))
# def area(r):
#     return 3.14*r**2
# area=area(r)
# print("area=",area)

"""largest"""
# n=int(input("enter a number: "))
# def even(n):
#     return n%2
# t=even(n)
# if t==0:
#     print("true")
# else:
#     print("false")


"""discount"""
# a=int(input("enter the amound:" ))
# d=int(input("enter the discount"))
# def discount(b,c):
#     return (b/c*100)


"""local and global"""

# a=10
# def asd():
#     print("inside asd()",a)
# asd()
# print("outside asd()",a)    



"""local"""
# def abc():
#     a=20
#     print(a)
# abc()  

"""global"""
# a=30
# def abc():  
#     print(a)
# abc()  

"""enclosed"""  
# def abc():
#     a=10
#     def adc():    
#         print(a)
#     adc()
# abc()    

"""recursion"""
# def asd():
#     print("a")
#     asd()
# asd()    



# a=1
# def asd(b):
#     b=b+1
#     print(b)
#     asd(b)
# asd(a)    


# a=1
# def asd(b):
#     if b<=10:
       
#         print(b)
#         b=b+1
#         asd(b)
# asd(a)        
          
          
          
""" recursion function"""

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# res=fact(0) 
# 0print(res) 


# a=100
# def asd(b):
#     if b>=1:
#         print(b)
#         b=b-1







# asd(b)
# asd(a)                     
                                                                                                                                                     
"""exception"""

# print("start")
# try:
#     a=10 
#     b=0
#     print(a/b)
# except:
#     print("cant divid by zero")
# finally:
#     print("this is final")
# print("end")  


# print("start")
# try:
#     a=20
#     b=10
#     print(a*b)   
# except:
#     print("cant divid by zero")
# finally:0
#     print("this is final")
# print("end")   

"""filehandling"""

# file=open("demo.txt","r")   
# s=file.readline()
# print(s)
# file.close() 


# file=open("demo.txt","w") 
# file.write("hello") 
# file.close()  

# file=open("demo.txt","a")    
# file.write("hai")
# file.close()   

"""context"""

# with open("demo.txt","w") as file:
#     file.write("hai anu")


# with open("demo.txt","r") as file:
#     s=file.readline()
#     print(s)

"""lambda"""

# s=lambda a,b:a*b
# print(s(4,5))
 
 
# def fun(a):
#     return lambda b:a+b
# x=fun(4)
# print(x(5))


"""functional programming"""

# def add(a,b):
#     return a+b
# def sqr(x):
#     return x**2
# z=sqr(add(5,3))
# print(z)


"""module"""


 
    
       

    
 

          

