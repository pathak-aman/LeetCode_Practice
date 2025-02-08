import heapq
from collections import defaultdict

class NumberContainers:

    def __init__(self):
        self.index_to_number = dict()
        self.num_to_indices_heap = defaultdict(list)
        
    def change(self, index: int, number: int) -> None:
        self.index_to_number[index] = number
        heapq.heappush(self.num_to_indices_heap[number], index)
        
    def find(self, number: int) -> int:
        if number not in self.num_to_indices_heap:
            return -1

        while self.num_to_indices_heap[number]:
            min_index = self.num_to_indices_heap[number][0]
            if not self.index_to_number[min_index] == number:
                heapq.heappop(self.num_to_indices_heap[number])
            else:
                return min_index
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)