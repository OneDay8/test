class Person:
    def __init__(self,x):
        self.x = x
        self.name = 'William'
        self.age = 45
        self.wight = 90
    def greet(self):
        print('hi,my name is ' + self.name)

    
    
    
class Animal(Person):
    def __init__(self,x):
        super(Animal, self).__init__(x)
        self.name = 'cat'
    def greet(self,Person):
        print(self.name + ' is belong to ' + Person.name )



#creat a object
p1 = Person(1)
a1 = Animal(123)
#call the method
a1.greet(p1)



class Fib():
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
'''
fib = Fib()
for i in fib:
    if i > 10:
        break
    print(i)
'''
    



class People(object):
    def __init__(self,name,age,gender, money):
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    def __play(self):           ##双下划线表示类内部使用
        print("王者荣耀正在进行时")
        self.newname = '111'
        return self.newname
    def play(self):
        self.newname1 = self.__play()
        return self.newname1
        
'''    
p1 = People('user1', 10, 'male', 1000000)
p1.play()
'''



lalalalal

























