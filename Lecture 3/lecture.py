#Iteration
#While loops
#find 4!

x = 4
i = 1
factorial = 1
while i <= x:
    factorial = factorial * i
    i = i + 1
print(factorial)

#for loops
factorial = 1
for i in range(1,5):
    factorial *= i
    i += 1
print(factorial)

#Finger exercise: print "Hello World!" N times
N = 5
for i in range(N):
    print("Hello World!")
print("---------------")
while N > 0:
    print("Hello World!")
    N -= 1