class Solution:
    def maxPower1(self, s: str) -> int:
        power = 1
        for uniqueletter in set(s):
            currentpower = 1
            reset_power = 1
            letter_occurrence = [pos for pos,letter in enumerate(s) if letter == uniqueletter]
            for occurrence in range(len(letter_occurrence)-1):
                if letter_occurrence[occurrence+1]-letter_occurrence[occurrence] == 1:
                    currentpower+=1
                else:
                    if currentpower > reset_power:
                        reset_power = currentpower
                    currentpower = 1
            if reset_power>currentpower:
                biggest_power =  reset_power
            else:
                biggest_power = currentpower
            if biggest_power > power:
                power=biggest_power
        return power


    def maxPower(self, s: str) -> int:
        first_ptr = 0
        second_ptr = 1
        power ,current_power = 1,1
        while second_ptr < len(s):
            if s[second_ptr] == s[first_ptr]:
                current_power +=1
            else:
                if current_power>power:
                    power = current_power
                current_power = 1
            first_ptr+=1
            second_ptr+=1
        if current_power > power:
            return current_power
        return power
obj1 = Solution()
print(obj1.maxPower(s = "acdsaasdddaaasxc"))
