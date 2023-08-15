#task 1:ss
name = "Golam Hossain"
age = 26
print("My name is " + name + " and I am " + str(age) + " years old.")

#task 2:
num1 = 10  
num2 = 5.14
num1_float = float(num1)
num2_int = int(num2)
print("num1:", num1, "Type:", type(num1))
print("num2:", num2, "Type:", type(num2))
print("num1_float:", num1_float, "Type:", type(num1_float))
print("num2_int:", num2_int, "Type:", type(num2_int))

#task 3:
sentence = "Python programming is fun!"
print("Length of the string:", len(sentence))
print("8th character:", sentence[7])
substring = sentence[0:6]
result = substring + " I enjoy it!"
print("Result:", result)

#Task 4:
fruits = ["apple", "banana", "cherry", "date"]
fruits.append("grape")
fruits.remove("banana")
print("Length of the list:", len(fruits))
sliced_fruits = fruits[1:3]
extra_fruits = ["kiwi", "lemon"]
combined_list = sliced_fruits + extra_fruits
print("Combined list:", combined_list)

#task 5:
num = 20
if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")


#Task 6:
print("Numbers from 1 to 10:")
for num in range(1, 11):
    print(num)
sum_numbers = 0
for num in range(1, 101):
    sum_numbers += num
print("Sum of numbers from 1 to 100:", sum_numbers)


#task 7:
def calculate_square(number):
    return number ** 2
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True
number_1 = 7
number_2 = 29

square_of_7 = calculate_square(number_1)
is_29_prime = is_prime(number_2)

print("Square of", number_1, "is:", square_of_7)
if is_29_prime:
    print(number_2, "is a prime number.")
else:
    print(number_2, "is not a prime number.")


#task 8:
student = {
    "name": "Golam Hossain",
    "age": 26,
    "grade": "A",
}
student["course"] = "Computer Science & Engineering"
print("Keys in the dictionary:")
for key in student.keys():
    print(key)

print("\nKey-value pairs:")
for key, value in student.items():
    print(key, ":", value)
