# function
# syntax
def my_function():
    print("Hello World!!");

my_function();

def my_function(fname, lname):
    print("Hello! " + fname + " " + lname);

my_function("World", "Param");

# to pass arbitrary arguments --> *args
def arb_arg(*kids):
    print("Tallest kid of class is " + kids[2]);
    print(kids);

arb_arg("abc","efg","xyz","pqr");

# kwargs, keyword arguments --> **kwargs

def print_kid_name(**kids):
    print("first name is " + kids["fname"] + " & last name is " + kids["lname"]);

print_kid_name(fname = "Hello", lname = "World");

# default Param
def print_country(country = "India"):
    print("The Country is " + country);
print_country();

# passing list as param
def print_fruits(fruits):
    for x in fruits:
        print(x);

fruits = ["apple","orange", "cherry"]
print_fruits("Apple");
print_fruits(fruits);

# Return from function
def multiply_by_2(num):
    return 2 * num;

print(multiply_by_2(5));
print(multiply_by_2(15));
print(multiply_by_2(25));

# for empty function
def myfunction():
    pass;

myfunction();

# OOP - Object Oriented Programming
# class

class MyClass:
    x = 5;

O1 = MyClass();
print(O1.x)

O2 = MyClass();
print(O2.x);

class Car:
    Door = 5;
    Wheel = 4;
    Seat = 5;

toyota = Car();
print(toyota.Door);
print(toyota.Wheel);
print(toyota.Seat);

suzuki = Car();
print(suzuki.Door);
print(suzuki.Wheel);
print(suzuki.Seat);

class Car:
    def __init__(self, door, wheel, seat):
        self.door = door;
        self.wheel = wheel;
        self.seat = seat;

    def print_car_design(self):
        print("Wheels: "+self.wheel);
        print("Seats: "+self.seat);
        print("Door: "+self.door);

toyota = Car("3","4","2");
toyota.print_car_design();

suzuki = Car("5","4","4");
suzuki.print_car_design();

# OOP --> Inheritance , Abstraction , Encapsulation , Polymorphism
class Person:
    def __init__(self, name, age, gender):
        self.name = name;
        self.age = age;
        self.gender = gender;
        print("init called");

    def print_person_name(self):
        print(f"Hello my name is mr/ms: {self.name} and age is : {self.age}");

j1 = Person("John", 30, "male");
j1.age = 40;
j1.name = "Johnny";
j1.print_person_name();

r1 = Person("Raj", 20, "male");
r1.print_person_name();

print(j1.name);
print(j1.age);   


class Person:
    def __init__(self, name, age, gender):
        self.name = name; #public
        self.__age = age; #private
        self._gender = gender; #protected
        print("init called");

    def get_person_name(self):
        print(f"name is : {self.name}");

    def get_person_age(self):
        print(f"Age is: {self.__age}");

    def get_person_gender(self):
        print(f"Gender is: {self._gender}");

    def set_person_age(self, age):
        if age>0:
            self.__age = age;
        else:
            print("Invalid Age");

p1 = Person("Raj",25,"male");

print(p1.name);

p1.get_person_name();

print(p1._gender);

# print(p1.__age);

# p1.set_person_age(40);
# print(p1.get_person_age());

p1.set_person_age(0);
print(p1.get_person_age());

str1 = "Hello World";
print(len(str1));

myTuple = ("apple", "orange", "Cherry");
print(len(myTuple));



class Student(Person):
    pass

class Teacher(Person):
    pass

s1 = Student("Satish", 20, "Male");
s1.get_person_name();
s1.get_person_age();

t1 = Student("Raju", 40, "Male");
t1.get_person_name();
t1.get_person_gender();