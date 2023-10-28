# for i in range(1,6): 
#     for j in range(i):
#         print("*",end="")
#     print("\n")  
# for i in range(4,0,-1): 
#     for j in range(i):
#         print("*",end="")
#     print("\n")
    
"""area of a circle"""
   
# r=int(input("enter the radius: "))
# def area(r):
#     return 3.14*r**2
# area=area(r)
# print("area=",area)


"""sum"""

# a=int(input("enter the number: "))
# b=int(input("enter the number: "))
# def sum(a,b):
#     return a+b
# sum=sum(a,b)
# print("sum=",sum)

"""area of rectangle"""

# l=int(input("enter the length: "))
# w=int(input("enter the width: "))
# def area(l,w):
#     return l*w
# area=area(l,w)
# print("area=",area)

"""even or odd"""
# n=int(input("enter a number: "))
# def even(n):
#     return n%2
# t=even(n)
# if t==0:
#     print("true")
# else:
#     print("false")    

"""largest number"""

# ls=[2,4,5,8,10,20,7,1]
# def find_max(ls):
#     return max(ls)
# max=find_max(a,b,c)
# if max==a:
#     print("largest number is: ",a)
# elif max==b:
#     print("largest number is: ",b)
# else:
#     print("largest number is: ",c)    
        
"""power"""
# base=3
# exponent=3
# result=1
# while exponent !=0:
#     result*=base
#     exponent-=1
# print("answer ="+str(result))   

"""reverse string"""
# def reverse(s):
#     str=""
#     for i in s:
#         str=i+str
#     return str
# s="aryaanu" 
# print("the original string is: ")
# print(s)
# print("the reversed string is: ")
# print(reverse(s))            

"""vowels"""
# s=str(input("enter the string: "))
# print("string is: ",s)
# vowels="aeiouAEIOU"
# count=sum(s.count(vowel)for vowel in vowels)
# print("number of vowels=: ",count)            
