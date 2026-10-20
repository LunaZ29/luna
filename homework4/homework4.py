# Lists 

favorite_foods = ["ramen", "pizza", "cereal", "chicken", "quesadillas"]
print(favorite_foods[1])  # prints "pizza"
print(favorite_foods[-1])  # prints "quesadillas"

favorite_foods.append("tacos")  # adds "tacos" to the end of the list
favorite_foods[0] = "apple" # changes the first item in the list to "apple" 

favorite_foods.remove("cereal")  # removes "cereal" from the list 
len(favorite_foods)  # returns the length of the list, which is now 5 

for food in favorite_foods:
    print(food.upper())  # prints each food in the list on a new line

first = favorite_foods[0]  # makes first thing in list = first 
last = favorite_foods[-1]  # makes last thing in list = last 

print(first, last) # prints "apple tacos" 

# oh i did this wrong cuz its not slicing it says can only concatenate list (not "str") to list, so i changed it to a slice and it worked

first_and_last = favorite_foods[:1] + favorite_foods[-1:]  # makes a new list with first and last things 

print(first_and_last) 

for food in favorite_foods:
    if food == "potato":
        print("A potato") 
    else:
        print("No potato!") 

# woah i made it a while loop and the terminal wouldnt stop showing "No potato!" so i switched it to a for loop and its much better 

#3.2 

for numbers in range(0, 21): 
    print(numbers) 

def get_first_15(numbers):
    for numbers in range(0, 16): 
        print(numbers) 

get_first_15(numbers) 

# i was putting for instead of def and it was giving me an error so i changed it to def because i had forgotten that thats how you define a function 

def get_every_5th(numbers): 
    return [number for number in numbers if number % 5 == 0]
numbers = list(range(21))
print(get_every_5th(numbers))

def reverse_and_stride(numbers): 
    return get_every_5th(numbers)[::-1]

print(reverse_and_stride(numbers))

# 3.3 

numberss = [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

print(numberss[2])
print(numberss[1][1]) 

numberss.append([10, 11, 12]) 

def sum_nested(numberss): 
    total = 0
    for row in numberss: 
        total += sum(row)
    return total 

print(sum_nested(numberss)) 

# 3.4 
def fivebyfive(): 
    grid = [] 
    counter = 1 
    for i in range(5): 
        row = [] 
        for j in range(5): 
            row.append(counter) 
            counter += 1 
        grid.append(row)
    return grid

def replace_multiples_of_three(grid):
    new_grid = [] 
    for row in grid: 
        new_row = []
        for num in row: 
            if num % 3 == 0: 
                new_row.append("?") 
            else: 
                new_row.append(num)
        updated_grid.append(new_row) 
    return updated_grid

def no_question_marks(grid): 
    total_sum = 0 
    for row in grid: 
        for num in row: 
            if num != "?": 
                total_sum += num
    return total_sum 

# 4 

ages = { 
    "Katie": 30,
    "Miriam": 42, 
    "Safia": 25, 
    "Mira": 48
}

print(ages["Katie"]) 
ages["Mira"] = 100
ages["Milana"] = 52 
ages.pop("Miriam") 
# i learned that pop removes the key and value from the dictionary 
for name, age in ages.items():
    print(f"{name} is {age} years old.")

print(ages)


