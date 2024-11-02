#Multi-level Inheritance
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#The child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")  
#The child class Dogchild inherits another child class Dog  
class BabyDog(Animal):  
    def eat(self):  
        print("dog eating") 
d = BabyDog()  
#d.bark()
d.eat()  
d.speak()  

