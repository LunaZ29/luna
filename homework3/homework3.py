#3.1 SAYING GOODBYE 
def say_goodbye(name):
    print("goodbye,", name) 

say_goodbye("luna")

#3.2 AREA OF A CIRCLE 
def areaofcircle(r): 
    print(3.14 * r ** 2)

areaofcircle(2)

#4.1 SUB,MULT,DIV 
def subtract(a, b):
    return a - b 

print(subtract(4, 2))

def multiply(a, b):
    return a * b 

print(multiply(4, 2))

def divide(a, b):
    return a / b 

print(divide(4, 2)) 

#5 CONDITIONALS 
#5.1 
temp = [60, 70, 80, 90, 100]
def whattowear(temp): 
    return (min(temp) , max(temp)) 

print(whattowear(temp))

#5.2 
def whatnum(day): 
    if day == "Monday":
        return 1 
    if day == "Tuesday": 
        return 2 
    if day == "Wednesday": 
        return 3 
    if day == "Thursday": 
        return 4 
    if day == "Friday": 
        return 5 
    if day == "Saturday": 
        return 6 
    if day == "Sunday": 
        return 7 

print(whatnum("Tuesday"))

#5.3 
def fuelefficiency(distance, fuel): 
    return distance / fuel 

print(fuelefficiency(5, 10))

#5.4 
def secretcode(int): 
    if int < 10: 
        return int 
    
    lastint = int % 10 
    print(lastint)
    restints = int // 10 
    print(restints)

    multiplier = 1
    countdown = restints

    while countdown > 0:
        multiplier *= 10
        print(multiplier)
        countdown //= 10
        print(countdown)        
    return (lastint * multiplier) + restints

secretcode(12345)

#6 LOOPS 
#6.1 
def power(x,y):
    result = x
    for counter in range(y-1):
        result *=x
    return result
print(power(2,3))

#6.2 
#6.2.1  
def minimum(list):
    min = 0
    for item in list:
        if  item < min:
            min = item
    return min

list_min = [1, 2, 5, -6, 60]

print(minimum(list_min))

def maximum(list_min):
    max = 0
    for item in list_min:
        if item > max:
            max = item
    return max

print(maximum(list_min))

#6.2.2
list = [3, 5, 6, 11, 23, 50]

def minimum_while(list):
    counter = 0
    min = list[0]
    while counter < len(list):
        if min > list[counter]:
            min = list[counter]
        counter += 1
    return min

print(minimum_while(list))

def maximum_while(list): 
    counter = 0
    max = list[0]
    while counter < len(list): 
        if max < list[counter]:
            max = list[counter]
        counter += 1 
    return max 

print(maximum_while(list))

#6.3 
def sumofbig(num):
    return sum(int(digit) for digit in str(abs(num)))

print(sumofbig(1234)) 

#7.1 
num = 5555
result = sumofbig(num)
# it will add the integers that make up that big number 
print(f"The result of Calculating the Sum with num = {num} is {result}")