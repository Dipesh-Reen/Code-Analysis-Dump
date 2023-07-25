# Function to check if a number is even
def CheckEven(number):
    if number%2==0: return True
    else: return False

# Function to calculate the square of a number
def square(num):return num*num

# Function to print the elements of a list in reverse
def PrintListReversed(lst):
    for i in range(len(lst)-1, -1, -1):
        print(lst[i])

# Main code
number = 10
if CheckEven(number)==True:
    print("The number is even.")
else:
    print("The number is odd.")

squared_number = square(number)
print("The square of the number is:", squared_number)

my_list = [1, 2, 3, 4, 5]
PrintListReversed(my_list)
