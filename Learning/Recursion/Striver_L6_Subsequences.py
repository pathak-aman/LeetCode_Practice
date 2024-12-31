def subseq(idx, current_array, original_array):
    if idx == len(original_array):
        print(current_array)
        return
    else:
        # Follow this order only.
        # Add an element and then remove
        current_array.append(original_array[idx])
        subseq(idx+1, current_array, original_array)
        current_array.pop()
        subseq(idx+1, current_array, original_array)


if __name__ == "__main__":
    array = [1,2,3,4]
    subseq(0, [], array)
