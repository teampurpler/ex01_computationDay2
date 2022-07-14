
# Conclusion: recursion is that functions call themselves to solve the probs
# recursions: step 1 what is the base case, step 2 what is the recursion rule that make the problems smaller

# Fibonacci sequence F(n) = F(n-1) + F(n-2) base case: F(0) = 0, F(1) = 1
def fib_array(n):
    array = [0,1]
    for i in range(2, n+1):
        array.append(array[i-1]+array[i-2])
    return array[n]

# solution 1 (iteration)
def fib(n):
    if n <=1:
        return n
    num_a = 0
    num_b = 1
    for i in range(n-1):
        temp = num_b
        num_b += num_a
        num_a = temp
    return num_b

# solution 2 (recursion) the Fibonacci sequence should be: 0,1,1,2,3,5,8,13,21
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(8))

# tc = O(2^n)  sc = O(n) call stack cost (n) space
