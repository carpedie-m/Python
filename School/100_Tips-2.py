#
## 100 Helpful Python Tips
#
contents = [
            "filter() returns a new object",
            "map() returns a new object",
            "range() includes a step parameter that may not be known that much",
            "range() starts by default at 0",
            "You don’t need to compare the length with 0",
            "You can define the same method multiple times inside the same scope",
            "You can access private properties even outside their intended scope",
            "Check the memory usage of an object",
            "You can define a method that can be called with as many parameters as you want",
            "You can call the parent class’s initializer using super() or parent class’s name",
            "You can redefine the '+' operator inside your own classes",
            "You can also redefine the '<' and '=' operators inside your own classes",
            "You can define a custom printable version for an object of a class",
            "Swap cases of characters in a string",
            "Check if all characters are white spaces in a string",
            "Check if all characters in a string are either alphabets or numbers",
            "Check if all characters in a string are alphabets",
            "Remove characters from the right based on the argument",
            "Check if a string represents a number",
            "Check if a string represents a Chinese number",
            "Check if a string has all its words starting with an uppercase character",
            "We can use negative indexes in tuples too",
            "Nest a list and a tuple inside a tuple",
            "Quickly count the number of times an element appears in a list that satisfies a condition",
            "You can easily get the last n elements using slice()",
            "Count the number of times an element appears in a tuple",
            "Get the index of an element in a tuple",
            "Get sub-tuples by making jumps",
            "Get sub-tuples starting from an index",
            "Remove all elements from a list, set, or dictionary",
            "Join 2 sets",
            "Condition inside the print function",
            "Multiple conditions at a single if-statement",
            "At least one condition is met out of many in a single if-statement",
            "Any non-empty string is evaluated to True",
            "Any non-empty list, tuple, or dictionary is evaluated to True",
            "Other values that evaluate to False are None, 'False' and the number 0",
            "You cannot change the value of a global variable just by mentioning it inside a function",
            "Count the number of elements in a string or list using Counter from 'collections'",
            "Check if 2 strings are anagrams using Counter",
            "Count the number of elements using 'count' from 'itertools'",
            "Sort elements of a string or list based on their frequency",
            "Find the most frequent element in a list in just one line",
            "Difference between copy() and deepcopy()",
            "You can avoid throwing errors when trying to access a non-existent key in a dictionary",
            "You can build your own iterator",
            "You can remove duplicates from a list in a single line",
            "Print the place where a module is located",
            "You can check whether a value is not part of a list using 'not in'",
            "Difference between sort() and sorted()",
            "Generate unique IDs using the uuid module"]

#for idx, content in enumerate(contents, 1):
#    print(f'#{idx:03d}.{content}')

def content_list():  # generator
    for idx, content in enumerate(contents, 1):
        yield f'\n#{idx + 49:03d}. {content}'
cl = content_list()


print(next(cl)) #50
my_list = [1, 2, 3, 4]
odd = filter(lambda x: x % 2 == 1, my_list)
print(f'\t{my_list = }')
print(f'\t{list(odd) = }')
odd2 = [x for x in my_list if x % 2 == 1]
print(f'\t{odd2 = }')


print(next(cl)) #51
squared = map(lambda x: x**2, my_list)
print(f'\t{list(squared) = }')
squared2 = [x**2 for x in my_list]
print(f'\t{squared2 = }')


print(next(cl)) #52
print("\t", end= "")
for number in range(1, 10, 3):
    print(number, end=" ")
print()


print(next(cl)) #53
def range_with_zero(number):
    for i in range(0, number):
        print(i, end= ' ')

def range_with_no_zero(number):
    for i in range(number):
        print(i, end= ' ')
print("\t", end= "")
range_with_zero(3)
print("\n\t", end= "")
range_with_no_zero(3)


print(next(cl)) #54
# if the length is greater than 0, then it is by default True, so you don't really need to compare it with 0
def get_element_with_comparison(my_list):
    if len(my_list) > 0:
        return my_list[0]

def get_first_element(my_list):
    if len(my_list):
        return my_list[0]

elements = [1, 2, 3, 4]
first_result = get_element_with_comparison(elements)
second_result = get_first_element(elements)
print(f'\t{first_result == second_result = }')


print(next(cl)) #55
def get_address():
    return "First Address"

def get_address():
    return "Second Address"

def get_address():
    return "Third Address"

print(f'\t{get_address() = }')


print(next(cl)) #56
class Engineer:
    def __init__(self, name):
        self.name = name
        self.__starting_salary = 62_000
    
lee = Engineer('Lee')
print(f'\t{lee._Engineer__starting_salary = }')


print(next(cl)) #57
import sys
print(f'\t{sys.getsizeof("bitcoin") = }')


print(next(cl)) #58
def get_sum(*args):
    result = 0
    for i in args:
        result += i
    return result

print(f'\t{get_sum(1, 2, 3) = }')
print(f'\t{get_sum(1, 2, 3, 5, 6) = }')
print(f'\t{get_sum(1, 2, 3, 5, 6, 7) = }')


print(next(cl)) #59
class Parent:
    def __init__(self, city, address):
        self.city = city
        self.address = address

class Child(Parent):
    def __init__(self, city, address, university):
        #super().__init__(city, address)
        Parent.__init__(self, city, address)
        self.university = university

child = Child('Lee', 'Daejoen', 'HiT')
print(f'\t{child.university = }')


print(next(cl)) #60
print(f'\t{10 + 1 = } # adding two integers')
print(f'\t{"first" + "second" = } # merging two strings')

class Expenses:
    def __init__(self, rent, groceries):
        self.rent = rent
        self.groceries = groceries
    def __add__(self, other):
        return Expenses(self.rent + other.rent, self.groceries + other.groceries)

april_expenses = Expenses(1000, 200)
may_expenses = Expenses(1000, 300)
total_expenses = april_expenses + may_expenses
print(f'\t{total_expenses.rent =  }')
print(f'\t{total_expenses.groceries =  }')


print(next(cl)) #61
class Game:
    def __init__(self, score):
        self.score = score
    
    def __lt__(self, other):
        return self.score < other.score

first = Game(1)
second = Game(2)
print(f'\t{first < second = }')

class Journey:
    def __init__(self, location, destination, duration):
        self.location = location
        self.destination = destination
        self.duration = duration
    def __eq__(self, other):
        return ( (self.location == other.location) and 
                 (self.destination == other.destination) and 
                 (self.duration == other.duration))
first = Journey('Location A', 'Destination A', '30 min')
second = Journey('Location B', 'Destination B', '30 min')
print(f'\t{first == second = }')
"""
    __sub__() for -
    __mul__() for *
    __truediv__() for /
    __ne__() for !=
    __ge__() for >=
    __gt__() for >
"""


print(next(cl)) #62
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __repr__(self):
        return repr('Rectangle with area = ' + str(self.a * self.b))
print(f'\t{Rectangle(3,4) = }')

        
print(next(cl)) #63
string = "This is just a sentence."
print(f'\t{string = }, {string.swapcase() = }')


print(next(cl)) #64
string = " "
print(f'\t{string.isspace() = }')


print(next(cl)) #65
name = "Password"
print(f'\t{name = }, {name.isalnum() = }')
name = "Secure Password"
print(f'\t{name = }, {name.isalnum() = }')   # False, because it contains whitespace
name = "S3cur34ssw0rd"
print(f'\t{name = }, {name.isalnum() = }')
name = "123"
print(f'\t{name = }, {name.isalnum() = }')


print(next(cl)) #66
string = "Name"
print(f'\t{string = }, {string.isalpha() = }')
string = "Firstname Lastname"
print(f'\t{string = }, {string.isalpha() = }')
string = "P4ssw0rd"
print(f'\t{string = }, {string.isalpha() = }')


print(next(cl)) #67
string = "This is a sentence with "
print(f'\t{string = }, {string.rstrip() = }')
string = "This is a sentence....,,,,aaaaasd"
print(f'\t{string = }, {string.rstrip(".,dsa") = }')
string = "This is a sentence....,,,,aaaaasd "
print(f'\t{string = }, {string.rstrip(".,dsa ") = }')
string = "ffffffffFirst"
print(f'\t{string = }, {string.lstrip("f") = }')


print(next(cl)) #68
string = "seven"
print(f'\t{string = }, {string.isdigit() = }')
string = "1337"
print(f'\t{string = }, {string.isdigit() = }')
string = "5a"
print(f'\t{string = }, {string.isdigit() = }')
string = "2**5"
print(f'\t{string = }, {string.isdigit() = }')


print(next(cl)) #69
string = "삼이육칠삼" # 32673,
print(f'\t{string = }, {string.isnumeric() = }') # 한자로 쓰면 True.
print(f'\t{string = }, {string.isdigit() = }')


print(next(cl)) # 70
string = "This is a sentence"
print(f'\t{string = }, {string.istitle() = }')
string = "10 Python Tips"
print(f'\t{string = }, {string.istitle() = }')
string = "How to Print A String in Python"
print(f'\t{string = }, {string.istitle() = }')
string = "PYTHON"
print(f'\t{string = }, {string.istitle() = }')


print(next(cl)) # 71
numbers = (1, 2, 3, 4)
print(f'\t{numbers[-1] = }')
print(f'\t{numbers[-4] = }')


print(next(cl)) # 72
mixed_tuple = (("a"*10, 3, 4), ['first', 'second', 'third'])
print(f'\t{mixed_tuple[0] = }')
print(f'\t{mixed_tuple[1] = }')


print(next(cl)) # 73
names = ["Lee", "Park", "Kim", "Choi", "Im", "Lee", "Lee"]
print(f'\t{names.count("Lee") = }')


print(next(cl)) # 74
ll = [x for x in range(1,11)]
slicing = slice(-4, None)
print(f'\t{ll[slicing] = }')
print(f'\t{ll[-3] = }')

string = "Data Science"
# start = 1, stop = None (don't stop anywhere), step = 1
# contains 1, 3, and 5 indices ???
slice_object = slice(5, None)
print(f'\t{string[slice_object] = }')


print(next(cl)) # 75
my_tuple = ('a', 1, 'f', 'a', 5, 'a')
print(f'\t{my_tuple = }')
print(f'\t{my_tuple.count("a") = }')


print(next(cl)) # 76
print(f'\t{my_tuple.index("f") = }')
print(f'\t{my_tuple.index("a") = }')


print(next(cl)) # 77
my_tuple = (x for x in range(1, 11))
print(f'\t{my_tuple = }')    # generator object
my_tuple = tuple(list(my_tuple))
print(f'\t{my_tuple[::3] = }')


print(next(cl)) # 78
print(f'\t{my_tuple[3:] = }')


print(next(cl)) # 79
my_list = [1, 2, 3, 4]
print(f'\t{my_list = }')
my_list.clear()
print(f'\t{my_list = }')

my_set = {1, 2, 3}
print(f'\t{my_set = }')
my_set.clear()
print(f'\t{my_set = }')

my_dict = {"a":1, "b":2}
print(f'\t{my_dict = }')
my_dict.clear()
print(f'\t{my_dict = }')


print(next(cl)) # 80
set1 = {4, 5, 6}
set2 = {1, 2, 3}
print(f'\t{set1 = }, {set2 = }')
print(f'\t{set1.union(set2) = }')

set1.update(set2)
print(f'\t{set1 = } after set1.update(set2)')


print(next(cl)) # 81
def is_positive(number):
    print("\tPositive" if number > 0 else "\tNegative")

is_positive(-3)


print(next(cl)) # 82
math_score = 40
biology_score = 79
physics_score = 56
history_score = 72

my_condition = [math_score > 50, biology_score > 50, 
                physics_score > 50, history_score > 50]
print(f'\t{my_condition = }')
if all(my_condition):
    print("\tCongratulation! you have passed all of the exam.")
else:
    print("\tSorry!,but it seems that you have to repeat at least one exam.")


print(next(cl)) # 83
if any(my_condition):
    print("\tCongratulation! you have passed one of exams.")
else:
    print("\tSorry!,but it seems that you have to repeat at least one exam.")


print(next(cl)) # 84
print(f'\t{bool("Non Empty") = }')
print(f'\t{bool("") = }')


print(next(cl)) # 85
print(f'\t{bool([]) = }')
print(f'\t{bool(set([])) = }')
print(f'\t{bool({}) = }')
print(f'\t{bool({"a":1}) = }')


print(next(cl)) # 86
print(f'\t{bool(False) = }')
print(f'\t{bool(None) = }')
print(f'\t{bool(0) = }')


print(next(cl)) # 87
string = "string"
def do_nothing():
    string = "inside a method"

do_nothing()
print(f'\t{string = }')

def do_nothing1():
    global string
    string = "inside a method"

do_nothing1()
print(f'\t{string = }')


print(next(cl)) # 88
from collections import Counter
rst = Counter("Banana")
print(f'\t{rst = }')
rst = Counter([1, 2, 1, 3, 1, 4, 1, 5, 1, 6])
print(f'\t{rst = }')
rst_dict = dict(rst)
print(f'\t{rst_dict = }')


print(next(cl)) # 89
def check_if_anagram(first:str, second:str):
    first = first.lower()
    second = second.lower()
    return Counter(first) == Counter(second)
    # return sorted(first) == sorted(second)

print(f'\t{check_if_anagram("testinG", "Testing") = }')
print(f'\t{check_if_anagram("Here", "Rehe") = }')
print(f'\t{check_if_anagram("Know", "Now") = }')


print(next(cl)) # 90
from itertools import count
my_vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I' ,'O', 'U']
current_counter = count()
string = "This is just a sentence"
for ch in string:
    if ch in my_vowels:
        print(f'\tCurrent vowel: {ch}')
        print(f'\tNumber of vowels found so far: {next(current_counter)}')


print(next(cl)) # 91
rst = Counter([1, 2, 3, 2, 2, 2, 2, 3,])
print(f'\t{rst = }')
print(f'\t{rst.most_common() = }')


print(next(cl)) # 92
my_list = ['1', 1, 0, 'a', 'b', 2, 'a', 'c', 'a']
print(f'\t{max(set(my_list), key=my_list.count) = }')


print(next(cl)) # 93
first_list = [[1, 2, 3], ['a', 'b', 'c']]
second_list = first_list.copy()
first_list[0][2] = 831
print(f'\t{first_list = }')
print(f'\t{second_list = }')

import copy
first_list = [[1, 2, 3], ['a', 'b', 'c']]
second_list = copy.deepcopy(first_list)
first_list[0][2] = 831
print(f'\t{first_list = }')
print(f'\t{second_list = }')


print(next(cl)) # 94
from collections import defaultdict
my_dict = {"name": "Name", "surname": "Surname"}
#print(my_dict["age"]) # KeyError: 'age'
my_dict =  defaultdict(str)
my_dict['name'] = "Name"
my_dict['surname'] = "Surname"
print(f'\t{my_dict["age"] = }')


print(next(cl)) # 95
class OddNumbers:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 2
        return x
odd_numbers_object = OddNumbers()
iterator = iter(odd_numbers_object)
print(f'\t{next(iterator) = }')
print(f'\t{next(iterator) = }')
print(f'\t{next(iterator) = }')


print(next(cl)) # 96
my_set = set([1, 2, 1, 2, 3, 4, 5])
print(f'\t{list(my_set) = }')


print(next(cl)) # 97
print(f'\t{defaultdict = }')
# import torch
# print(torch)


print(next(cl)) # 98
odd_numbers = [1, 3, 5, 7, 9]
even_numbers = []
for i in range(9):    
    if i not in odd_numbers:        
        even_numbers.append(i)
print(f'\t{even_numbers = }')


print(next(cl)) # 99
groceries = ['milk', 'bread', 'tea']
print(f'\t{groceries = }')
new_groceries = sorted(groceries)
print(f'\t{new_groceries = }')
groceries.sort()
print(f'\t{groceries = }')


print(next(cl)) # 100
import uuid
# Generate a UUID from a host ID, sequence number, and the current time
print(f'\t{uuid.uuid1() = }')
# Generate a random UUID
print(f'\t{uuid.uuid4() = }')


print("\n#101. Bonus : String is a primitive data type in Python")