#Strings

#input() function is used to take input from the user
text = input("Enter some text: ")
print("You entered:", text)

verb = input("Enter a verb: ")
print(f"I can {verb} better than you!")
print((verb+' ')*5)

#if statements
secret_num=5
guess = int(input("Guess the secret number: "))
if guess == secret_num:
    print("Congratulations! You guessed the secret number.")
elif guess < secret_num:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")

#Finger exercise
number = int(input("Enter a number: "))
if number == 0:
    print("The number is zero.")
elif number > 0:
    print("The number is positive.")
else:
    print("The number is negative.")

