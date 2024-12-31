def subseq_sum_k(index, current_sum, current_array, original_array, sum):
    if index == len(original_array):
        if current_sum == sum:
            print(current_array)
        return

    current_array.append(original_array[index])
    current_sum += original_array[index]
    subseq_sum_k(index+1, current_sum, current_array, original_array, sum)

    current_array.pop()
    current_sum -= original_array[index]
    subseq_sum_k(index+1, current_sum, current_array, original_array, sum)


def subseq_sum_k_print_1 (index, current_sum, current_array, original_array, sum):
    if index == len(original_array):
        if current_sum == sum:
            return current_array
            print(current_array)
        return False

    current_array.append(original_array[index])
    current_sum += original_array[index]
    if result := subseq_sum_k_print_1(index+1, current_sum, current_array, original_array, sum):
        return result
    

    current_array.pop()
    current_sum -= original_array[index]
    if result := subseq_sum_k_print_1(index+1, current_sum, current_array, original_array, sum):
        return result
    return False


def subseq_sum_k_print_1 (index, current_sum, current_array, original_array, sum):
    if index == len(original_array):
        if current_sum == sum:
            print(current_array)
            return True
        return False

    current_array.append(original_array[index])
    current_sum += original_array[index]
    if subseq_sum_k_print_1(index+1, current_sum, current_array, original_array, sum):
        return True
    

    current_array.pop()
    current_sum -= original_array[index]
    if subseq_sum_k_print_1(index+1, current_sum, current_array, original_array, sum):
        return True
    return False

if __name__ == "__main__":
    # array = [1,2,1,3,5,2,1,2,9,0,4]
    array = [1,2,1]
    k = 2
    # subseq_sum_k(0, 0, [], array, k)
    print(subseq_sum_k_print_1(0,0,[],array, k))
