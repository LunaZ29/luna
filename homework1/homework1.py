# File: homework1.py 

# Variables and Data Types

a = 10 
print(a) 
# this is an integer 

b = 1.5 
print(b) 
# this is a float 

c = "3j"
print(c)
# this is a string 

d = "hello" 
print(d)
# this is a string

e = [1, 2, 3] 
print(e)
# this is a list 

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f) 
# this is a dictionary 

g = (1, 2) 
print(g) 
# this is a tuple 
# u can put lists inside tuples but not the other way around

h = ["apple", "banana", "strawberry"]
print(h) 
# this is a list 

i = True 
print(i)
# this is a boolean 

j = None 
print(j) 
# this is a NoneType 
# use it when trying to find a variable that doesn't exist yet, or when you want to reset a variable to nothing

k = [True, "blue", 12] 
print(k) 
# this is a list (with mixed data types) 

l = str(14) 
print(l) 
# this is a string (converted from an integer) 

m = 1e4 
print(m) 
# this is a float (scientific notation for 10000.0)

'''
1. How many different data types did you find?
I found 8 different data types: integer, float, string, list, dictionary, tuple, boolean, and NoneType.
2. List all the data types you found.
   - integer
   - float
   - string
   - list
   - dictionary
   - tuple
   - boolean
   - NoneType
3. What variables have the same data types?
A and l are both ints (before l is converted to a string). I made it also that c and d are strings so they're also the same data type. E and h are both lists, too. 
4. What was the data type of l? Why is it not an integer? What does str() do?
The data type of l is a string. It is not an int because I used str() to convert 14 into a string. 
5. Look up one more data type not given above. Repeat the same procedure. 
set which is a collection of unique elements 
'''
# Question 5 
set = {1, 2, 3} 
print(set) 
# this is a set 

# Booleans

print(10 > 9) # True, 10 is greater than 9 
print (10 == 9) # False, 10 is not equal to 9
print(10 <= 9) # False, 10 is not less than or equal to 9
bool("abc") # True, non-empty string is True 
bool(123) # True, non-zero number is True
bool(["apple", "cherry", "banana"]) # True, non-empty list is True
bool(True) # True is True
bool (False) # False is False 
bool(0) # False, zero is False
bool("") # False, empty string is False
bool(" ") # True, non-empty string is True (with the space)
bool(()) # False, empty tuple is False
bool([]) # False, empty list is False 
bool({}) # False, empty dictionary is False
bool (True and False) # False, True and False is False
bool(True and True) # True, True and True is True
bool(False and False) # False, False and False is False
bool(True or False) # True, True or False is True
bool(True or True) # True, True or True is True
bool(False or False) # False, False or False is False
bool(not(False)) # True, not False is True
bool(not(True)) # False, not True is False

'''
What pattern do you notice about expressions returning True or False?
I noticed that if you put something in between the brackets it will be True but if it is empty or zero it will be False. 
Which expression surprised you about its result?
I was surprised that bool(" ") returned True because I thought it would be False since it is just a space. 
'''

# Create an expression, not listed above, that will return True. Why is it true? 
bool(5 > 3) # True, because 5 is greater than 3 

# Create an expression, not listed above, that will return False. Why is it false? 
bool(0 == 1) # False, because 0 is not equal to 1 

# Arithmetic Operators 

print(10 + 5) # 15, addition 
print( 10 - 5) # 5, subtraction
print(2 * 4) # 8, multiplication 
print(6 / 3) # 2, division
print(5 % 2) # 1 % is called modulo(remainder of 5 divided by 2)
print(3 ** 2) # 9, exponent (3 raised to the power of 2)
print( 15 // 2) # 7, floor division (rounds non-whole down to nearest) 

# Comparison Operators 

print(5 == 2) # False, 5 is not equal to 2 
print(10 != 10) # False, 10 is equal to 10 
print(2 < 5) # True, 2 is less than 5 
print(12 > 5) # True, 12 is greater than 5 
print( 5<= 6) # True, 5 is less than or equal to 6
print(1 >= 10) # False, 1 is not greater than or equal to 10

# Assignment Operators 

x = 5
x += 5
print(x) # 10, adds 5 to x
x -= 4
print(x) # 1, subtracts 4 from x
x *= 3
print(x) # 15, multiplies x by 3

# Logical Operators 
# What does the operator and do? Write an expression that results in True. Write an expression that results in False. 
print(5 > 3 and 2 < 4) # True, both conditions are true
# What does the operator or do? Write an expression that results in True. Write an expression that results in False.
print(5 > 3 or 2 > 4) # True, one condition is true but the other isn't but as long as one is true it is true 
# What does the operator not do? Write an expression that results in True. Write an expression that results in False.
print(not(5 > 3)) # False, because 5 is greater than 3 (the not is basically saying the opposite of the thing)

'''
More Questions: 
1. What is the difference between / and //? 
/ is regular division so it can bring back a decimal (aka float) but // is "floor division" which rounds down to the nearest whole number (aka integer) 
2. What is the difference between % and //? 
% is the "modulo" which gives you the remainder of a division but // is floor division which gives you the whole number result of a division rounded down
3. What operator would you use to calculate the remainder when diving two numbers? Give an example. 
I would use modulo (%) to calculate the remainder. 
EX) 
print(7 % 3)would give you 1 because 3 goes into 7 two times with a remainder of 1.
4. How do assignment operators work?
Assignment operators are used to assign values to variables and for them to be able to use operations on. 
'''

# Strings 

my_string = "hello" 

print(my_string) # prints hello 
print(my_string[0]) # prints h 
print(my_string[1]) # prints e 
print(my_string[2]) # prints l 
print(my_string[3]) # prints l
print(my_string[4]) # prints o
print(my_string[-1]) # prints o (last character)
print(my_string[1:3]) # prints el (doesn't include 3???) 
print(my_string[0:5:2]) # prints hlo
print(len(my_string)) # prints 5 (length of string) 
print(my_string + "goodbye") # prints hellogoodbye
print(my_string * 7) # prints the string 7 times 

'''
1. Define the term slicing. For which of the maniuplations did you slice your string?
Slicing is when you take a portion of a string. I used it for [1:3] and [0:5:2]
2. Call the following, describe the result. 
name = "Oski" 
print("Hello, my name is", name)
The result is "Hello, my name is Oski" because it prints the string and then adds the variable "name" (which i put as Oski) to the end of it 
3. Call the following, describe the result
name = "Oski" 
print(f"Hello, my name is {name}") 
Same as the previous. But the f in front of the string allows you to use variables inside the string
4. What is the difference between the two last print statements?
The first uses a comma at the end before name but the second uses an f before the whole string but brackets name 
'''

# Terminal Commands 
'''
cd --> changes directories --> move one folder to another --> ex) cd desktop 
ls --> lists all files in the current directory --> ex) ls
ls -a --> lists all files in the current directory including hidden files --> ex) ls -a
mkdir --> makes a new directory --> ex) mkdir new_folder
cat --> prints the contents of a file --> ex) cat file.txt
pwd --> prints the current working directory --> ex) pwd
cd .. --> moves up one directory --> ex) cd ..
cd . --> stays in the current directory --> ex) cd .
cd ~ --> moves to the home directory --> ex) cd ~
cp --> copies a file or directory --> ex) cp file.txt new_file.txt
mv --> moves a file or directory --> ex) mv file.txt new_file.txt
rm --> removes a file or directory --> ex) rm file.txt
clear --> clears the terminal screen --> ex) clear
grep --> searches for a specific string in a file --> ex) grep "search_term" file.txt

# Questions 
1. Look up 3 other commands not present. Define and explain how to use them on the command line. 
- touch --> creates a new empty file --> ex) touch new_file.txt
- echo --> prints a string to the terminal --> ex) echo "Hello, World!"
- man --> displays the manual for a command --> ex) man ls
2. What is the difference between ls and ls -a? 
ls lists all files in the current directory but ls -a lists all files including hidden files (usually files that start with .) 
3. What is a hidden file? 
A hidden file is a file that is not normally visible when listing files in a directory. But you can see it if you do ls -a 
4. Look up 3 other flags. Define and explain how to use them on the command line.
- -l --> lists files in long format, showing permissions, owner, size, and modification date --> ex) ls -l
- -h --> displays file sizes in human-readable format (e.g., KB, MB, GB) --> ex) ls -h
- -R --> lists files in the current directory and all subdirectories recursively --> ex) ls -R
'''

