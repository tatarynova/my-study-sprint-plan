#Floats and Approximation Methods
#converting into binary algorithm

num = eval(input("Enter a number: "))

def binary_converter(denary_num):
    if denary_num < 0:
        is_neg = True
        denary_num = abs(denary_num)
    else:
        is_neg = False
    result = ''
    if denary_num == 0:
        result = '0'
    while denary_num > 0:
        result = str(denary_num%2) + result
        denary_num = denary_num//2
    if is_neg:
        result = '-' +result
    return result

print(binary_converter(num))

#implementation of approximation algorithm
x = 36
epsilon = 0.01
num_guesses = 0
guess = 0.0
increment = 0.0001

while abs(guess**2 - x) >= epsilon:
    guess += increment
    num_guesses += 1

print('num_guesses = ', num_guesses)
print(guess, "is close enough to square root of", x)
#this algorithm could be faster if we have used binary search

#approximating square root using binary search
x = 36

def binary_search_sqrt(num, increment=0.0001, epsilon=0.01):
    digits = len(str(increment).split('.')[1])

    #create a list of all possible guesses
    # list = [i*increment for i in range(0, num*10**digits)]
    
    low = 0
    high = num * 10**digits
    num_guesses = 0

    while low <= high: 
        mid = (low + high) // 2 #index of the mid value
        guess = mid*increment
        num_guesses += 1

        if abs(guess**2 - num) < epsilon:  # Use epsilon like original
            return guess, num_guesses
        
        if guess**2 > num:
            high = mid - 1
        else:
            low = mid + 1
    return None, num_guesses

print(binary_search_sqrt(x))