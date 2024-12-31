def combination_find_all_unique(index, current_sum, current_array, target_sum, original_array, list_answers):    
    if index == len(original_array):
        if current_sum == target_sum:
            list_answers.append(current_array)
        return

    # pick
    if target_sum - current_sum >= original_array[index]:
        current_array.append(original_array[index])
        current_sum += original_array[index]

        # if result := combination_find_all_unique(index, current_sum, current_array, target_sum, original_array, list_answers):
        #     list_answers.append(result)
        combination_find_all_unique(index, current_sum, current_array, target_sum, original_array, list_answers)
        print("PICK:",list_answers)
        
        current_array.pop()
        current_sum -= original_array[index]
        
    # not pick
    # if result := combination_find_all_unique(index+1, current_sum, current_array, target_sum, original_array, list_answers):
    #     list_answers.append(result)
    combination_find_all_unique(index+1, current_sum, current_array, target_sum, original_array, list_answers)
    print("NOT_PICK:",list_answers)



if __name__ == "__main__":
    array = [1,2]
    sum = 2
    print(combination_find_all_unique(0, 0, [], sum, array, []))
