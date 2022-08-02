while True:
    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input(": ")
    if user_input == "quit":
        break
    elif user_input == "add":
        p = int(input('how many numbers, would you like to add? '))
        x = []
        for number in range(1, p+1):
            s = 'p'+str(number)
            s = int(input(('enter number ' + str(number) + ':  ')))
            x.append(s)
        print(sum(x))
    elif user_input == "subtract":
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        print("the answer is " + str(first_number - second_number))
    elif user_input == "multiply":
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        third_number = int(input("Enter the third number: "))
        print("the answer is " + str(first_number * second_number * third_number))
    elif user_input == "divide":
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        print("the answer is " + str(first_number / second_number))
    else:
        print("Unknown input")
def tolu_tolu():
    print("I")
    print("love")
    print("Tolulope")

tolu_tolu()
def your_love(word):
    print("I love " + word)

your_love(input("Enter your love:"))
def checking_max(x, y):
    if x > y:
        return x
    else: return y
print(checking_max(4, 5))
