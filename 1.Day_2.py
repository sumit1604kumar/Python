# print(len("Sumit"))
# #  it wont run -due to it is not a string -->print(len(12345))
# print(type(str(len("sumit")))) # it is converting integer to string with the str function
# print("Anju"[2])
# print("123" + "456")
# print(12 + 12 )
# print(123_456_789)# it will treat as number 123456789
# TASK 1 adds the digits in a 2 digit number. e.g. input was 35, then the output should be 3 + 5 = 8
# two_digit_number = input("Type a two digit number: ")
# print(int(two_digit_number[0]) + int(two_digit_number[1]))
#print( 3 * (3 + 3) / 3 - 3)
#TASK 2 Write a program that calculates the Body Mass Index (BMI) from a user's weight and height
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# print(int(float(weight)/ float(height) ** 2))
# print(round(8/3, 2)) # it will round until 2 decimals point
# print(8//3)  # gives quotient
# print(8%3)  # gives remainder
# TASK 4 using maths and f-Strings,tells us how many days, weeks, months left if we live until 90 years
#age = input("What is your current age?")
# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)
# print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Final TASK
print("Welcome to the tip calculator.")
total_bill = input("what was the total bill ?")
tip = float(input("what percentage tip would you like to give ? "))
people = int(input("How many people to spilt the bill ? "))

pay = float(total_bill.replace('$', ''))
# print(pay)
final_bill = (pay + tip/100 * pay)/people
print(f"Each person should pay {final_bill:.3f}")