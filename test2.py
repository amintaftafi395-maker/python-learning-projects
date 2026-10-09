
print("/welcome to calculator app /")
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
print(":_______________________________________:" + "\n")
addinq = first_number + second_number
print(f"The sum of {first_number} and {second_number} is {addinq}.")
subtracting = first_number - second_number
print(f"The difference of {first_number} and {second_number} is {subtracting}.")
multiplying = first_number * second_number
print(f"The product of {first_number} and {second_number} is {multiplying}.")
if second_number != 0:
    dividing = first_number / second_number
    print(f"The quotient is {dividing}.")
else:
    print("Error: Cannot divide by zero.")
if second_number != 0:
    modulus = first_number % second_number
    print(f"The modulus is {modulus}.")
else:
    print("Error: Cannot calculate modulus by zero.")

square = first_number ** 2
print(f"The square of {first_number} is {square}.")
print("program completed" )