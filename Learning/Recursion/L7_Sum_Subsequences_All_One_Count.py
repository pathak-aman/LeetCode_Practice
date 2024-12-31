def f_all(index, curr_array, curr_sum, input_array, n, k):
    if index >= n:
        if curr_sum == k:
            print(curr_array)
        return 
    
    # take
    curr_array.append(input_array[index])
    curr_sum += input_array[index]
    f_all(index+1, curr_array, curr_sum, input_array, n, k)

    # non-take
    curr_array.pop()
    curr_sum -= input_array[index]
    f_all(index+1, curr_array, curr_sum, input_array, n, k)



def f_one(index, curr_array, curr_sum, input_array, n, k):
    if index >= n:
        if curr_sum == k:
            print(curr_array)
            return True
        return False
    
    # take
    curr_array.append(input_array[index])
    curr_sum += input_array[index]
    if f_one(index+1, curr_array, curr_sum, input_array, n, k):
        return True

    # non-take
    curr_array.pop()
    curr_sum -= input_array[index]
    if f_one(index+1, curr_array, curr_sum, input_array, n, k):
        return True


def f_count(index, curr_array, curr_sum, input_array, n, k):
    count = 0
    if index >= n:
        if curr_sum == k:
            print(curr_array)
            return 1
        return 0
    
    # take
    curr_array.append(input_array[index])
    curr_sum += input_array[index]
    a = f_count(index+1, curr_array, curr_sum, input_array, n, k)

    # non-take
    curr_array.pop()
    curr_sum -= input_array[index]
    b = f_count(index+1, curr_array, curr_sum, input_array, n, k)
    return a+b




if __name__ == "__main__":
    array = [1,3,2,5,4,3,5,9,2]
    k = 8
    f_all(0,[],0, array, len(array)-1,k)
    if f_one(0,[],0,array, len(array)-1,k):
        print(True)
    else:
        print(False)
    count = f_count(0,[],0,array, len(array)-1,k)
    print(count)