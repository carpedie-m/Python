#
## Using String Format Function in Python3
#

'''
Since Python3 involves the str.format() function, we have a more elegant way to define string templates
and insert our variable values as arguments in this function.
'''

## 1. Passing arguments by position
print("\n1. Passing arguments by position")
# in default order
print(' {0:s} {1:s} {2:s}'.format('I', 'love', 'Python'))
# define the position
print(' {0:s} {1:s} {2:5s}'.format('I', 'love', 'Python'))
# customise the position
print(' {1:s} {0:s} {2:s}'.format('love', 'I', 'Python'))
# the extra arguments will be ignored
print(' {0:s} {1:s} {2:s}'.format('I', 'love', 'Python', 'yes'))
# use the argument at particular positions multiple times
print(' {0:s} {1:s} {2:s}. {3:s} {1:s} {2:s}, too'.format('I', 'love', 'Python', 'She'))


## 2. Passing arguments by Key
print("\n2. Passing arguments by Key")
print(' {subject} {verb} {object}'.format(subject='I', verb='love', object='Python'))

## 3. Passing a dictionary
print("\n3. Passing a dictionary")
str_dict = {'subject':'I', 'verb':'love', 'object':'Python'}
print(' {subject} {verb} {object}'.format(**str_dict))

## 4. Passing a list
print("\n4. Passing a list")
str_list = ['I', 'love', 'Python'] 
print(' {0} {1} {2}'.format(*str_list))
# also access the elements in a list by subscripts

print(' {0[0]} {0[1]} {0[2]}'.format(str_list))

## Advanced Usage : Formatting Symbols
print("\nAdvanced Usage : Formatting Symbols")
def table():
    print(' || {:=^15} || {:=^50} ||'.format(' symbols ', ' meanings'))
    print(' || {:<15} || {:<50} ||'.format(':', 'format indicator'))
    print(' || {:<15} || {:<50} ||'.format('-/=\\#', 'filling'))
    print(' || {:<15} || {:<50} ||'.format('<', 'left aligned'))
    print(' || {:<15} || {:<50} ||'.format('>', 'right aligned'))
    print(' || {:<15} || {:<50} ||'.format('^', 'center aligned'))
    print(' || {:<15} || {:<50} ||'.format('10 (number)', 'width'))
    print(' || {:<15} || {:<50} ||'.format(',', 'formating number'))
    print(' || {:<15} || {:<50} ||'.format('.', 'decimal precision'))
    print(' || {:<15} || {:<50} ||'.format('f', 'floating number'))
    print(' || {:<15} || {:<50} ||'.format('b', 'binary number'))
    print(' || {:<15} || {:<50} ||'.format('d', 'decimal number'))
    print(' || {:<15} || {:<50} ||'.format('o', 'octal number'))
    print(' || {:<15} || {:<50} ||'.format('x', 'hexa number'))
    print(' || {0:=^15} || {0:=^50} ||'.format(''))

table()

## 5. Filling, alignment and width
print("\n5. Filling, alignment and width")
print(' |{:<15}|'.format('left'))
print(' |{:^15}|'.format('center'))
print(' |{:>15}|'.format('right'))
print()
print(' |{:=<15}|'.format('left'))
print(' |{:*^15}|'.format('center'))
print(' |{:$>15}|'.format('right'))

## 6. Decimal precision
print("\n6. Decimal precision")
print(' {:.3f}'.format(3.1415926))
print(' {:.2%}'.format(7/8))


## 7. Number formatting
print("\n7. Number formatting")
print(' {:,d}'.format(123456789))
print(' {:_d}'.format(123456789))
print(' {:+f}\n {:+f}'.format(100,-100))

## 8. Number base conversion
print("\n8. Number base conversion")
print(' {:b}'.format(100))
print(' {:d}'.format(0b11011100))
print(' {:o}'.format(100))
print(' {:x}'.format(100))

## 9. Directly convert datetime and string
print("\n9. Directly convert datetime and string")
from datetime import datetime
print(' {:%d-%B, %Y %A %H:%M:%S}'.format(datetime.now()))
