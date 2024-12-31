def reverse_array(start, to_array, n):
    if start >= n/2:
        print(to_array)
        return
    to_array[start], to_array[n-start-1] = to_array[n-start-1], to_array[start]
    reverse_array(start+1, to_array, n)



def palindrom (start, to_string, n):
    if start >= n/2:
        return True
    if to_string[start] == to_string[n - 1 - start]:
        return palindrom(start+1, to_string, n)
    else:
        return False



if __name__ == "__main__":
    to_array = [1,2,3,4,5,6,7,8,9,10]
    reverse_array(0, to_array, len(to_array))

    to_string = "hannah"
    print(palindrom(0, to_string, len(to_string)))

    to_string = "hanmah"
    print(palindrom(0, to_string, len(to_string)))
