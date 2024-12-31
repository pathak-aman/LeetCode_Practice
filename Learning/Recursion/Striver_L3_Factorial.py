# Functional
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
    
# Parameterized
def sum(n, curr_sum):
    if n < 0:
        print(curr_sum, n)
        return
    sum(n-1, curr_sum + n)



if __name__ == "__main__":
    n = 5
    print(fact(n))
    sum(n, 0)
