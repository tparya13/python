# class vehicle:
#     wheel=4
#     door=4
#     def start(self):
#         print("engine start")
        
# car=vehicle()
# car.start()     


# class vehicle:
#     wheel=4
#     door=4
#     def start(self,type):
#         print(type,"engine start")
        
# car=vehicle()
# car.start("two strok")    


# class vehicle:
#     wheel=4
#     door=4
#     def start(self,a,b):
#         print(a*b)
        
# car=vehicle()
# car.start(4,5)   


"""self"""  
# class vehicle:
#     color="red"
#     def show(self):
#         print("color is",self.color)
# car=vehicle()
# car.show()     


# class vehicle:
#   =-  def setcolor(self,color):
#         self.color=color
#     def show(self):
#         print("color is",self.color)
# car=vehicle()
# car.setcolor("yellow")
# car.show()        
 
 
"""CONSTRUCTOR"""
# class vehicle:
#     def __init__(self,color,tyre):
#         self.color=color 
#         self.tyre=tyre
#     def show(self):
#         print("color is",self.color,"tyre is",self.tyre)
# car=vehicle("red",4)
# car.show()  
    

# class animal:
#     def __init__(self,color,legs,eyes):
#         self.color=color
#         self.legs=legs
#         self.eyes=eyes
#     def show(self):
#         print("color is",self.color,"legs is",self.legs,"eyes is",self.eyes)
# pet_animal=animal("black",4,2)
# wild_animal=animal("white",4,2)
# pet_animal.show()
# wild_animal.show()



# class vehicle:
#     color="red"
#     def engine(self):
#         print("all vehicles have engine")
# class car(vehicle):
#     def fourwheel(self):
#         print("car have fourwheel",self.color)
# c=car()
# c.fourwheel()
# c.engine()  

"""multilevel inheritence"""
# class Granpa:
#     def kashandi(self):
#         print("kashandi family")
#     def farmer(self):
#         print("farmer") 
# class Father(Granpa):
#     def driver(self):
#         print("driver")    
#     def reader(self):
#         print("reader")
# class Me(Father):
#     def swimming(self):
#         print("swimming")
#     def engineer(self):
#         print("engineer")    
# class Mechild(Me):
#     def gamer(self):
#         print("gamer")   
# ob=Granpa()
# ob.kashandi()   

"""multiple inheritence"""
# class Father:
#     def driver(self):
#         print("driver")
# class Mother:
#     def cook(self):
#         print("cook") 
# class girl(Father,Mother):
#     def enginner(self):
#         print("engineer")
# g=girl()
# g.enginner()   
# g.cook()   
# g.driver()  


"""prog"""
class libraryitem:
    def title(self):
        print("voice of nature")
    def author(self):
        print("mark john")
    def id(self):
        print(201202)
class book(libraryitem):
    def no__of__pages(self):
        print("420")
    def read_book(self):
        print("reading the book")
class dvd(libraryitem):
    def duration(self):
        print("4 hours")
    def dvd_play(self):
        print("playing the dvd")
b=book()
b.author()
b.id()
b.no__of__pages()
b.read_book()
b.title()                  
        
c=dvd()
c.duration()
c.dvd_play()        



"""encapsulation"""
# class bank:
#     def __init__(self,accno,__savings):  
#         self.accno=accno
#         self.savings=__savings
#     def deposite(self,dep):
#         self.savings+=dep
#     def display(self):
#         print("savings=",self.savings)
# anu=bank(2345612346,3000)
# anu.deposite(4000)
# anu.display()        
           
"""private"""          
# class A:
#     __a=10
#     def disp(self):
#         print(self.__a)
# obj=A()
# obj.disp()   

"""protected"""
# class A:
#     _a=10
#     def disp(self):
#         print(self._a)
# obj=A()
# obj.disp() 
# print(obj._a)   

"""abstract"""
# from abc import ABC,abstractclassmethod
# class vehicle(ABC):
#     def engine(self):
#         print("engine provide")
#     @abstractclassmethod    
#     def gear(self):
#         pass
# class car(vehicle):
#     def gear(self):
#         print("automatic gear")
# class truck(vehicle):      
#     def wheel(self):
#         print("heavy")
#     def gear(self):
#         print("manuel gear")  
# c=car()
# c.gear()
# t=truck()  
# t.gear()                    
                             
                       

                                     
                                   
    
 
