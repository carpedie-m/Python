#
## 100 Helpful Python Tips
#
contents = [ "'Else' condition inside a 'for' loop",
            "Get elements from a list using named variables",
            "Get n largest or n smallest elements in a list using the module heapq",
            "Pass values from a list as method arguments",
            "Get all the elements in the middle of the list",
            "Assign multiple variables in just one line",
            "List comprehensions",
            "Enumerate related items of the same concept via Enum",
            "Repeat strings without lopping",
            "Compare 3 numbers just like in Math",
            "Merge dictionaries in a single readable line",
            "Find the index of an element in a tuple",
            "Convert a string into a list of strings",
            "Avoid 'trivial' mistakes by using named parameters",
            "Print multiple elements with a single print() statement",
            "Print multiple elements in the same line",
            "Print multiple values with a custom separator in between each value",
            "You cannot use a number at the beginning of the name of a variable",
            "You cannot use an operator at the beginning of the name of a variable",
            "You cannot have 0 as the first digit in a number",
            "You can use the underscore character anywhere in the name of a variable",
            "You can separate big numbers with the underscore",
            "Reverse the ordering of a list",
            "Slice a string using a step function",
            "Reverse slicing",
            "Partial Slicing with just the beginning or ending index",
            "Floor division",
            "Difference between == and 'is'",
            "Changing the value of a variable that is assigned to another variable",
            "Check whether a string is larger than another string",
            "Check whether a string starts with a particular character without using the index 0",
            "Find the unique id of a variable using id()",
            "Integers, floats, strings, booleans, sets, and tuples are immutable",
            "Strings and tuples are immutable",
            "Lists, sets, and dictionaries are mutable",
            "You can turn a set into an immutable set",
            "An 'if-elif' block can exist without the else block at the end",
            "Check whether 2 strings are anagrams using sorted()",
            "Get the value of a character in Unicode",
            "Get keys of a dictionary in a single line",
            "Get values of a dictionary in a single line",
            "Swap keys and values of a dictionary",
            "You can convert a boolean value into a number",
            "You can use boolean values in arithmetic operations",
            "You can convert any data type into a boolean value",
            "Convert a value into a complex number",
            "Add a value in the first position in a list",
            "Lambda functions can only be in one line",
            "Conditionals statements in lambda should always include the 'else' part"]

#for idx, content in enumerate(contents, 1):
#    print(f'#{idx:03d}.{content}')

def content_list():  # generator
    for idx, content in enumerate(contents, 1):
        yield f'\n#{idx:03d}. {content}'
cl = content_list()

print(next(cl)) #1
numbers = [2, 4, 6, 8, 10]
for number in numbers:
    if number % 2 == 1:
        print(f'\t{number}')
        break
else:
    print("\tNo odd numbers")
print("\tit is quite unusual!")


print(next(cl)) #2
ll = [x for x in range(1,6)]
one, two, three, four, five = ll
print(f'\t{one = }, {two = }, {three = }, {four = }, {five = }')


print(next(cl)) #3
import heapq
from typing import Reversible

scores = [51, 33, 64, 87, 91, 75, 15, 49, 33, 82]
print(f'\t{scores = }')
print(f'\t{heapq.nlargest(3, scores) = }')
print(f'\t{heapq.nsmallest(5, scores) = }')


print(next(cl)) #4
print(f'\t{scores = }')
#print(f'\t{*scores = }')
print("\t *scores = ", *scores)

def sum_of_element(*args):
    total = 0
    for i in args:
        total += i
    return total
result = sum_of_element(*scores)
print(f'\t{result = }')
print(f'\t{sum(scores) = }')


print(next(cl)) #5
_, _, *elements_in_the_middle, _, _ = scores
print(f'\t{elements_in_the_middle = }')


print(next(cl)) #6
one, two, three, four, five = 1, 2, 3, 4, 5
print(f'\t{one = }, {two = }, {three = }, {four = }, {five = }')


print(next(cl)) #7
numbers = [x for x in range(6)]
squared_numbers = [num * num for num in numbers]
print(f'\t{numbers = }')
print(f'\t{squared_numbers = }')

print(f'\tyou can use comprehension with dictionaries, sets, and generators as well')
dictionary = {'a':4, 'b':5}
squared_dictionary = {key: num*num for key, num in dictionary.items()}
print(f'\t{dictionary = }')
print(f'\t{squared_dictionary = }')


print(next(cl)) #8
from enum import Enum
class Status(Enum):
    NO_STATUS = -1
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETED = 2
print(f'\t{Status.IN_PROGRESS.name = }')
print(f'\t{Status.COMPLETED.value = }')


print(next(cl)) #9
name = "Banana"
print(f'\t{name * 4}')


print(next(cl)) #10
x = 3
print(f'\t1 < x < 10 = {1 < x < 10}')


print(next(cl)) #11
first_dictionary = {'name': 'Fatos', 'location': 'Munich'}
second_dictionary = {'name': 'Fatos', 'surname': 'Morina', 'location': 'Bavaria, Munich'}
result = first_dictionary | second_dictionary
print(f'\t{result = }')


print(next(cl)) #12
books = ('Atomic habits', 'Ego is the enemy', 'Outliers', 'Mastery')
print(f'\t{books.index("Mastery") = }') 


print(next(cl)) #13
import ast
def string_to_list(string):
    return ast.literal_eval(string)
string = "[[1, 2, 3],[4, 5, 6]]"
my_list = string_to_list(string)
print(f'\t{my_list = }') 


print(next(cl)) #14
# a - b != b - a
def subtract(a, b):
    return a - b
print(f'\t{subtract(1, 3) = }')
print(f'\t{subtract(3, 1) = }')
print(f'\t{subtract(a=1, b=3) = }')
print(f'\t{subtract(b=3, a=1) = }')


print(next(cl)) #15
text = 'print(1, 2, 3, "a", "z", "this is here", "here is something else")'
print(f'\t{text}')


print(next(cl)) #16
print_lst = 'print("Hello", end="")', \
            'print("World") # HelloWorld', \
            'print("Hello", end=" ")', \
            'print("World") # Hello World',\
            'print("words", "with", "commas", "in", "between", sep=",")', \
            '# words, with, commas, in, between'
for using in print_lst:
    print(f'\t{using}')


print(next(cl)) #17
print_lst = 'print("29", "01", "2020", sep="") # 29/01/2022', \
            'print("name", "domain.com", sep="@") # name@domain.com'
for using in print_lst:
    print(f'\t{using}')


print(next(cl)) #18
stat_list = 'four_letter = "abcd" # this work', '4_letters = "abcd" # this doesn\'t work'
for using in stat_list:
    print(f'\t{using}')


print(next(cl)) #19
print("\t+variable = 0110 # this doesn\'t work")

print(next(cl)) #20
print("\tnumber = 0110 # this doesn\'t work")


print(next(cl)) #21
print(next(cl)) #22


print(next(cl)) #23
my_list = ['a', 'b', 'c', 'd']
print(f'\t{my_list = }')
my_list.reverse()
print(f'\t{my_list = }')


print(next(cl)) #24
my_string = "This is just a sentence"
print(f'\t{my_string = }')
print(f'\t{my_string[0:5] = }')
print(f'\t{my_string[0:10:3] = }')


print(next(cl)) #25
print(f'\t{my_string[10:0:-1] = }')
print(f'\t{my_string[10:0:-2] = }')


print(next(cl)) #26
print(f'\t{my_string[4:] = }')
print(f'\t{my_string[:3] = }')


print(next(cl)) #27
print(f'\t{3/2 = }')
print(f'\t{3//2 = }')


print(next(cl)) #28
first_list = [1, 2, 3]
second_list = [1, 2, 3]
print(f'\t{first_list = }, {second_list = }')
# Is their actual value the same?
print(f'\t{first_list == second_list = }') # True
# Are they pointing to the same object in memory
print(f'\t{first_list is second_list = }')
# False, since they have same values, but in different objects in memory
third_list = first_list
print(f'\t{third_list is first_list = }')
# True, since both point to the same object in memory


print(next(cl)) #29
first_str = "An initial value"
second_str = first_str
print(f'\t{first_str = }, {second_str = }')
first_str = "An updated value"
print(f'\t{first_str = }, {second_str = }')


print(next(cl)) #30
first_str = "abc"
second_str = "def"
print(f'\t{first_str = }, {second_str = }')
print(f'\t{first_str < second_str = }')
second_str = "ab"
print(f'\t{first_str = }, {second_str = }')
print(f'\t{first_str < second_str = }')



print(next(cl)) #31
my_string = "abcdef"
print(f'\t{my_string = }')
print(f'\t{my_string.startswith("b") = }')


print(next(cl)) #32
print(f'\t{id(1) = }')
print(f'\t{id(2) = }')
print(f'\t{id("string") = }')


print(next(cl)) #33
number = 1
print(f'\t{id(number) = } \t{id(1) = }')
number = 3
print(f'\t{id(number) = } \t{id(1) = }')


print(next(cl)) #34
name = "Fatos"
print(f'\t{name = }, {id(name) = }')
name = "fatos"
print(f'\t{name = }, {id(name) = }')

my_tuple = (1, 2, 3, 4)
print(f'\t{my_tuple = }, {id(my_tuple) = }')
my_tuple = ('a', 'b')
print(f'\t{my_tuple = }, {id(my_tuple) = }')


print(next(cl)) #35
cities = ["seoul", "daejon", "jeju"]
print(f'\t{cities = }, {id(cities) = }')
cities.append("Busan")
print(f'\t{cities = }, {id(cities) = }')

my_set = {1, 2, 3, 4}
print(f'\t{my_set = }, {id(my_set) = }')
my_set.add(5)
print(f'\t{my_set = }, {id(my_set) = }')


print(next(cl)) #36
my_set = frozenset(['a', 'b', 'c', 'd'])
print("\tUsing frozenset( )")
#my_set.add("a") # AttributeError: 'fronzen' object has no attribute 'add'


print(next(cl)) #37
def check_number(number: int) -> str:
    if number > 0:
        return "Positive"
    elif number == 0:
        return "Zero"
    return "Negative"

print(f'\t{check_number(1) = }')


print(next(cl)) #38
def check_if_anagram(first_word, second_word):    
    first_word = first_word.lower()    
    second_word = second_word.lower()    
    return sorted(first_word) == sorted(second_word)

print(f'\t{check_if_anagram("testinG", "Testing") = }')  # True
print(f'\t{check_if_anagram("Here", "Rehe") = }')  # True
print(f'\t{check_if_anagram("Know", "Now") = }')  # False


print(next(cl)) #39
print(f'\t{ord("A") = }')
print(f'\t{ord("B") = }')
print(f'\t{ord("Z") = }')
print(f'\t{ord("a") = }')


print(next(cl)) #40
my_dict = {"a":1, "b":2, "c":3}
keys = [idx for idx, _ in my_dict.items()]
print(f'\t{keys = }')


print(next(cl)) #41
values = [value for _, value in my_dict.items()]
print(f'\t{values = }')


print(next(cl)) #42
reversed_my_dict = {j: i for i, j in my_dict.items()}
print(f'\t{reversed_my_dict = }')


print(next(cl)) #43
print(f'\t{int(False) = }')
print(f'\t{float(True) = }')


print(next(cl)) #44
x, y = 10, 10
print(f'\t{x = }, {y = }')
result = (x - False) / (y * True)   # False : 0, True : 1
print(f'\t{result = }')


print(next(cl)) #45
print(f'\t{bool(.0) = }')
print(f'\t{bool(3) = }')
print(f'\t{bool("-") = }')
print(f'\t{bool("string") = }')
print(f'\t{bool(" ") = }')


print(next(cl)) #46
print(f'\t{complex(10, 12) = }')
print(f'\t{hex(11) = }')


print(next(cl)) #47
my_list = [3, 4, 5]
print(f'\t{my_list = }')
my_list.append(6)
my_list.insert(0, 2)
print(f'\t{my_list = }')


print(next(cl)) #48
"""
comparison = lambda x: if x > 3: 
                            print("x > 3") 
                        else: 
                            print("x is not greater than 3")
# SyntaxError
"""
print(f'\tYou can not have lambdas in more than one line')


print(next(cl)) #49
#comparison = lambda x: "x > 3" if x > 3
tt = 'comparison = lambda x: "x > 3" if x > 3'
print(f'\t{tt} -> SyntaxError')