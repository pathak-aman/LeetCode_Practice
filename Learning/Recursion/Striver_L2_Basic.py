def f_backtrack(i,n):
    if i > n:
        return
    f_backtrack(i+1, n)
    print(i)

def f_backtrack_2(i,n):
    if i < 1:
        return
    f_backtrack_2(i-1, n)
    print(i)
    


def f(i,n):
    if i < 1:
        return
    print(i)
    f(i-1,n)


if __name__ == "__main__":
    print("In main")
    f(10,10)
    f_backtrack(1, 10)
    f_backtrack_2(10,10)