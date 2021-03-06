# class definition 
class Animal(object): 
    species = 'Animal' 

    def __init__(self, name): 
        self.name = name 
        self.attributes = ['beathe'] 
 
    def add_attributes(self, attributes): 
        if type(attributes) == list: 
            self.attributes.extend(attributes)
        else: 
            self.attributes.append(attributes)
 
    def __str__(self): 
        return self.name+" is of type "+self.species+" and has attributes:"+str(self.attributes) 
 
# instantiating the class 
a1 = Animal('Rover') 
# invoking instance method 
a1.add_attributes(['runs', 'eats', 'dog']) 
# user defined string representation of the Animal class 
print (str(a1) )
 
# deriving class Dog from base class Animal 
class Dog(Animal):     
    species = 'Dog' 
 
    def __init__(self, *args): 
        super(Dog, self).__init__(*args)  
 
# deriving class Fox from base class Animal 
class Fox(Animal):     
    species = 'Fox' 
 
    def __init__(self, *args): 
        super(Fox, self).__init__(*args) 
 
# creating instance of class Dog 
d1 = Dog('Rover') 
d1.add_attributes(['lazy', 'beige', 'sleeps', 'eats']) 
print (str(d1) )
 
# creating instance of class Fox 
f1 = Fox('Silver') 
f1.add_attributes(['quick', 'brown', 'jumps', 'runs']) 
print (str(f1) )
