# break
for letter in 'laioffer':
    if letter == 'i':
        break
    print(letter)

## input\

# sum = 0
# n = int(input('how many numbers'))
# for i in range(n):
#     sum += int(input('numbers you want?'))
# print(sum)


def printinfo(name, age = 35):
    print(name)
    print(age)
    return

printinfo('mimi')

#reassignment
x = [0,2]
y = x
y[0] = 1
print(y)

def reassign(x):
    x = [3]
reassign(x)
x = [0,1,2]
print(x)

# modify
def modify(x):
    x[1]= 1
x = [0,2,4,6]
modify(x)
print(x)

#prime number:
def isPrime(x):
    if x ==1:
        return False
    for i in range(2,x):
        if x%i ==0:
            return False
    return True
print(isPrime(4))

#Composite num
def isComposite(x):
    if x ==1 :
        return False
    return not isPrime(x)
print(isComposite(21))

#prefect num: if the num equals to the sum of all its factors,then it's perfect

def factorSum(x):
    sum_of_factor = 0
    for i in range(1,x):
        if x%i ==0:
            sum_of_factor += i
    return sum_of_factor
def is_perfect(x):
    return factorSum(x) == x

print(is_perfect(28))

import math
#Triangular num: a number can be expressed in the form of (n+1)*n/2
def isPosInt(x):
    return x == int(x) and x > 0
def checkSolution(a,b,c):
    if b**2 - 4*a*c < 0:
        return False
    delta = math.sqrt(b**2 - 4*a*c)
    solution_a = (-b +delta)/(2*a)
    solution_b = (-b -delta)/(2*a)
    return isPosInt(solution_a) or isPosInt(solution_b)
def isTriangular(x):
    return(checkSolution(0.5,0.5,-x))
print(isTriangular(28))

#append
def foo(x):
    x = [2]
    x.append(1)
    x.append(0)
    return x
x = [3]
foo(x)
print(foo(x))

# print in the function
def fun(lst):
    print(lst)

lst1 = [1,2,3,4]
lst2 = lst1
fun(lst2)
lst1[0] = 9
fun(lst2)


# triangular num
# def IsTriangular, check a,b,c = 1/2,1/2, -x
