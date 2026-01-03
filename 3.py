# tuples operation
# concatenation

tuple1 = (1,2,3);
tuple2 = (4,5,6);
combine_tuple = tuple1 + tuple2;
print(combine_tuple);

# repetition
repeated_tuple = (1,2) * 3;
print(repeated_tuple);

# membership
print(1 in tuple1);

# functions
my_tuple = (1,2,3,1,1,1);
print(my_tuple.count(1));
print(my_tuple.count(2));
print(len(my_tuple));

print(my_tuple.index(2));
print(my_tuple.index(3));
print(my_tuple.index(1));
print(my_tuple.index(1,1));

# Advantages
# Immutable : this ensures that data cannot be modified after creation
# Faster than Lists : due to its immutability
# can be used as keys in dictionary

# Sets in Python
# set is a collection of unique items that is unordered and unindexed.
# set do not allow duplicate values
# syntax : my_Set = {element1, element2,element3,...}

fruits_set = {"apple","Kiwi","banana","cherry"}
numbers_set = {1,2,3,4,5}
print(fruits_set);
print(numbers_set);
numbers_set = {6,2,7,4,3}
print(numbers_set);

empty_set = set(); # to assign empty set
print(empty_set);

set1 = {1,2,3}
set2 = {3,4,5}


# union
union_set = set1 | set2;
print(union_set);

# intersection
intersection = set1 & set2;
print(intersection);

# difference
diff_set = set1 - set2;
print(diff_set);

diff_set = set2 - set1;
print(diff_set);

# symmetric difference
sym_diff_set = set1 ^ set2;
print(sym_diff_set);

# functions
# add
fruits_set.add("orange");
print(fruits_set);

# remove
fruits_set.remove("orange");
print(fruits_set);

fruits_set.discard("Kiwi");
print(fruits_set);

# remove random element
fruits_set.pop();
print(fruits_set);

# clear
fruits_set.clear();
print(fruits_set);

# Dictionaries
# syntax my_dict = {
#       "key1" : "value1",
#       "key2" : "value2",
#       "key3" : "value3"
#       }

karnataka_food = {
    "Bengaluru" : "Masala Dosa",
    "Mysuru" :"Mysore",
    "Mysuru" :"Mysore Pak",
    "Mangaluru" : "Neer Dosa"
}
print(karnataka_food);

# accessing
print(karnataka_food["Mysuru"]);
print(karnataka_food.get("Mysuru"));

print(karnataka_food.get("Mandya","Not Found"));
print(karnataka_food.get("Mandya"));

# Adding
karnataka_food["Mandya"] = "Mudde";
print(karnataka_food);

# # remove
# mysuru_food = karnataka_food.pop("Mysuru");
# print(mysuru_food);
# print(karnataka_food);

# del karnataka_food["Mandya"]
# print(karnataka_food);

# functions
print(karnataka_food.keys());
print(karnataka_food.values());
print(karnataka_food.items());

new_dish = {"Davangere" : "Benne Dosa"}
karnataka_food.update(new_dish);
print(karnataka_food);

# Conditional Statement
# if, elif and else
time = 20;
if time == 20:
    print("time is 20");
elif time >= 21:
    print("time is 25");
else:
    print("time is not 20");

# While loop
# While condition:

# i = 1;
# while i<=5:
#     print(i);
#     if i==3:
#         break;
#     i += 1;

i = 0;
while i <= 5:
    if i == 3:
        i += 1;
        continue;
    print(i);
    i += 1;

pin = "";
correct_pin = "1234";
while pin != correct_pin:
    pin = input("Enter your pin: ")
    if pin != correct_pin:
        print("Incorrect PIN, Try again")
print("PIN Accepted");

# bus has & seats, each time a seat it booked availability decreases. when there are no seat stop loop and display no seat msg
# print all off number for given user input