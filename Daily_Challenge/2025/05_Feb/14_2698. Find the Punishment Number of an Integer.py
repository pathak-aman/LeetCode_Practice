class Solution:
    def punishmentNumber(self, n: int) -> int:
        total = 0  # This will accumulate the sum of squares for valid numbers

        def canPartition(square_str: str, num: int, pos: int = 0, curr_sum: int = 0) -> bool:
            """
            Determines if the string representation of a square (square_str) can be partitioned
            into contiguous substrings whose integer values add up to num.

            Args:
                square_str (str): The square of the number as a string.
                num (int): The original number.
                pos (int): The current index in square_str.
                curr_sum (int): The current sum of the partitions.

            Returns:
                bool: True if a valid partition exists; otherwise, False.
            """
            # If we've reached the end of the string, check if the accumulated sum equals num.
            if pos == len(square_str):
                return curr_sum == num

            # Try every possible partition starting at index pos.
            for i in range(pos, len(square_str)):
                # Extract substring from pos to i (inclusive).
                substring = square_str[pos:i+1]
                val = int(substring)
                
                # Prune the recursion if the current sum already exceeds num.
                if curr_sum + val > num:
                    break

                # Recursively try the rest of the string.
                if canPartition(square_str, num, i + 1, curr_sum + val):
                    return True

            # No valid partition was found from this position.
            return False

        # Iterate through each number from 1 to n.
        for i in range(1, n + 1):
            square_str = str(i * i)
            if canPartition(square_str, i):
                total += i * i  # Add the square if a valid partition exists.

        return total