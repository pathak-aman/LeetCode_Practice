def combination_print_all(index, current_sum, current_array, target_sum, original_array):
    if current_sum > target_sum:
            return
    if index == len(original_array):
        if current_sum == target_sum:
            print(current_array)
            return
        return
    # pick
    current_array.append(original_array[index])
    current_sum += original_array[index]
    combination_print_all(index, current_sum, current_array, target_sum, original_array)

    # not pick
    current_array.pop()
    current_sum -= original_array[index]
    combination_print_all(index+1, current_sum, current_array, target_sum, original_array)
    return


def combination_print_one(index, current_sum, current_array, target_sum, original_array):
    if current_sum > target_sum:
            return False

    if index == len(original_array):
        if current_sum == target_sum:
            print(current_array)
            return True
        return False
    # pick
    current_array.append(original_array[index])
    current_sum += original_array[index]
    if combination_print_one(index, current_sum, current_array, target_sum, original_array):
        return True

    # not pick
    current_array.pop()
    current_sum -= original_array[index]
    if combination_print_one(index+1, current_sum, current_array, target_sum, original_array):
        return True
    return False



def combination_count(index, current_sum, current_array, target_sum, original_array):
    if current_sum > target_sum:
            return 0

    if index == len(original_array):
        if current_sum == target_sum:
            return 1
        return 0
    # pick
    current_array.append(original_array[index])
    current_sum += original_array[index]
    pick = combination_count(index, current_sum, current_array, target_sum, original_array)

    # not pick
    current_array.pop()
    current_sum -= original_array[index]
    not_pick =  combination_count(index+1, current_sum, current_array, target_sum, original_array)
    
    return pick + not_pick




if __name__ == "__main__":
    array = [1,2,1]
    sum = 3
    combination_print_all(0, 0, [], sum, array)
    # combination_print_one(0, 0 , [], sum, array)
    # print(combination_count(0, 0, [], sum, array))
