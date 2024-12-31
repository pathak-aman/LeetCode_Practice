# Sequence: 0, 1, 1, 2, 3, 5, 8, 13 ...
# Index   : 0, 1, 2, 3, 4, 5, 6, 7



def fib(N):
    if N == 0 or N == 1:
        return N
    return fib(N-1) + fib (N-2)



if __name__ == "__main__":
    N = 6
    print(fib(N))


#           N = 4
#             4
#           /   \ 
#          3     2
#         / \   / \
#        2   1  1  0
#       / \
#      1   0

