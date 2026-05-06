#Loops, Guess and Check, Binary
# total = 0
# for i in range(5,6):
#     if i%2==0:
#         total+=1
#         print(i)
# print(f"Total amount of even numbers is {total} ")

#count unique letters in a string
# s = input("Enter a string: ")
# seen = ''
# for char in s:
#     if char not in seen:
#         seen += char
# print(len(seen))

#find a secret number
# found = False
# secret_num = eval(input("Enter a secret number: "))
# for i in range(1,11):
#     if i == secret_num:
#         print(f"Secret number is {i}.")
#         found = True
# if not found:
#     print("Secret number has not been found.")

#Binary search
def binary_search(list,item):
    low = 0
    high = len(list)-1

    while low <= high : 
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item: 
            high = mid-1
        else:
            low = mid+1
    return None 

my_list=[1,2,3,4,5,6,7,8,9,10]

print(binary_search(my_list, 4))