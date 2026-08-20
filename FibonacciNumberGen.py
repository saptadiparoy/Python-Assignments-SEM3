#create a function that prints the fibonacci number for given num/position

"""fibonacci sequence is = 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 ---- 
so if user asks for the fifth number, we should return 3"""

def fibonacci_memo(n, memo= {}):
    if n<=1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2,memo)
    return memo[n]


def fibo_tabulation(n):

    if n<=1:
        return n

    dp = [0] * (n+1)

    dp [0] = 0
    dp [1] = 1

    for i in range (2, n+1):
        dp [i] = dp[i-1] + dp[i-2]

    return dp[n]

n = int(input("Enter Position   :  "))

print (f"Number using memoization   :   {fibonacci_memo(n)}")
print (f"Number using tabulation    :   {fibo_tabulation(n)}")