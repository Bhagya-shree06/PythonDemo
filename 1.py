# What is Python
# * Hign level, interpreted programming language
# * Web Development(e. g django, Flask)
# * Data Science and Machine Learning (e.g pandas, Teensorflow)
# * Automation(e.g scripting tasks)
# * Software devlopment and many more

# Why it is so popular
#     * Easy to learn
#     * community support
#     * Cross-platform
#     * Versatile

# Python - Setup
#     https://www.python.org/
#     go to download and download latest version
#     slect add to path and install now

# Python IDE (Integrated Development Environment)
#     * Pycharm(community edition - https://www.jetbrains.com/pycharm/editions/)
#     * VS Code
#     * jupyter Notebook

# verify the installation
#     "python --version" in cmd

# Key Features of Python
#     * Simple Syntax
#     * Interpreted -executed line by line
#     * Dynamical Typed - No Need to declare the variable types explicitly
#     * Object-Oriented - Supports OOP (Object oriented programming) like classes and objects
#     * Rich Standard Library - it has built in modules
# list code
# open IDE ->Create a python file 1.py -> print("Hello World") -->in terminal run "python 1.py"

print("Hello, World!!");

# variables & data types in python
x = 5;
print(type(x));
X = 6;
print(type(X));
y = "Hello";
print(type(y));
print(x);
print(X);
print(y);
is_true = True;
print(type(is_true));
print(is_true);

# type conversion
a = "10.25";
print(a)
print(type(a));
b = float(a);
print(b);
print(type(b));

c = int(b);
print(c);
print(type(c));

# Arithmetic Operation
# + add
# - sub
# * mul
# / div
# // floor div
# % modulus
# ** Exponentiation

a = 10;
b = 3;
print(a + b);
print(a - b);
print(a * b);
print(a / b);
print(a // b);
print(a % b);
print(a ** b);

# assigning values to multiple variables
x,y,z = 11,12,13;
print(x);
print(y);
print(z);

# variable reassignment
g = 5;
print(g);
g = 10;
print(g);
