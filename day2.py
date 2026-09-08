'''
#student marks manager

#take input of marks using loop, create a list to append marks into list
marks = []
for mark in range(3):
    mark = int(input("Enter the marks: "))
    print(mark)
    marks.append(mark)

#print marks
# insert 90 marks into list
marks.insert(0,90)


#add two marks by using extend
marks.extend([75,85])
print(marks)

#check for 75 marks in the list
if 75 in marks:
    marks.remove(75)


#to remove the final mark from list using pop
removed_mark = marks.pop()
print(f'the removed mark is {removed_mark}')

#final list of marks
print(f'final student marks list is {marks}')
print(f'count of students marks list is {len(marks)}')

#number list analyzer
#-----------------------
numbers = [20, 10, 30, 20, 40, 20]
print(f'the original list is {numbers}')
numbers.sort()
numbers.reverse()
print(numbers)
num = int(input("Enter a number to search for: "))
if num in numbers:
    print(f'the count of this number is {numbers.count(num)}')
    print(f'the index of this number is {numbers.index(num)}')
    print(f'the largest value is {max(numbers)}')
    print(f'the smallest value is {min(numbers)}')
    print(f'the smallest value is {sum(numbers)}')
else:
    print("number not found")


weight = int(input("Enter your weight: "))
height = float(input("Enter the height in meters: "))
bmi = (weight) / (height*2)
if bmi < 18.5:
    print(f'the person bmi {bmi} is under 18.5, so he is underweight')
elif 18.5 < bmi < 24.9:
    print(f'the person bmi {bmi} is normal , so he is healthy weight')
elif 25 <= bmi <= 29.9:
    print(f'the person bmi {bmi} is above 25, so he is overweight')
elif bmi > 30:
    print(f'the person bmi is {bmi}, he has obesity')    


nums = [10,15,20,25,30,35]
even = []
odd = []
for num in nums:
    if num % 2 == 0:
        even.append(num)
    elif num % 2 != 0:
        odd.append(num)



user_input = int(input("Enter the value: "))
for i in range(user_input):
    weight = float(input("Enter the weight in kgs: "))
    height = float(input("Enter the height in metres: "))
    name = input("Enter the user name: "))
    if weight > 0 and height > 0:
        bmi = (weight) / ((height)**2)
        if bmi < 18:
            print(f'{name} is into underweight category and BMI is {bmi}')
        elif 18.5 <= bmi <= 24.9:
            print(f'{name} is into normal weight category and BMI is {bmi}')
        elif 25.0 <= bmi <= 29.9:
            print(f'{name} is into overweight category and BMI is {bmi}')


'''
user_input = int(input("Enter the number of users to check: "))

for i in range(user_input):
    print(f"\n--- User {i+1} ---")
    name = input("Enter the user name: ")
    
    # Loop until valid weight and height are entered
    while True:
        try:
            weight = float(input("Enter the weight in kgs: "))
            height = float(input("Enter the height in metres: "))
            
            # Ensure numbers are positive and height isn't zero to avoid ZeroDivisionError
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be greater than zero. Please try again.")
                continue
                
            break # Exit the while loop if inputs are valid
            
        except ValueError:
            print("Invalid input! Please enter numbers only for weight and height.")

    # Calculate BMI safely
    bmi = weight / (height ** 2)
    
    # Categorize and print results
    if bmi < 18.5:
        print(f'{name} is in the underweight category and BMI is {bmi:.2f}')
    elif 18.5 <= bmi <= 24.9:
        print(f'{name} is in the normal weight category and BMI is {bmi:.2f}')
    elif 25.0 <= bmi <= 29.9:
        print(f'{name} is in the overweight category and BMI is {bmi:.2f}')
    else:
        print(f'{name} is in the obese category and BMI is {bmi:.2f}')
