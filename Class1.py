class Computer(): # Defining a class

    def __init__(self,cpu,ram): # init is a constructor
        print("To execute this func call not required number objects are created:")
        self.cpu=cpu
        self.ram=ram

    def config(self): # A func in class is called method
        print("16gb,i5,1TB")
        print("config:",self.cpu,self.ram)# cpu & ram are global variable that's y we call it using self

com1=Computer('i5',16) # Creating objects using class name

com2=Computer('Ryzen 3',8)# argument passing while abject creation

#Computer.config(com1)# Calling func using class refference
Computer.config(com2)

com1.config()#calling func using object itself......commonly used syntax
#com2.config()
print(type(com1))

print(id(com1))# Addressof com1
""" Size of an object depends the no.of var and size of the variables & constructor allocates the size of an object"""
# Computer() is a constructor and it will call init method implicitly

