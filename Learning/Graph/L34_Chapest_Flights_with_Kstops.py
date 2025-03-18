# Intuition: 
# We don't care how much the price is in isolation, we can afford expensive but can't go over the number of k stops. Therefore the order is stops and price.
# Stops are any nodes that aren't src and dest.

# Approach:
# We need to contruct a graph and go radially outward one city at a time, increasing the number of stops. BFS. 
# Data Structure: A simple queue, as stops differ by unit distance.

# All possible paths that lead from src to destintion that are within the number of stops are our candidates.
# Final answer will be when the queue empties, we return the answer stored in the distance array.


# TC ->
# SC -> 


from collections import deque
from math import inf
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        # make adj_list
        adj_list = [[] for _ in range(n)]
        for from_, to, price in flights:
            adj_list[from_].append((to, price))

        # price (distance) array: keeps track of the minimum price needed to reach any stop from src
        price = [inf for i in range(n)]
        price[src] = 0

        q = deque()

        # Will store (node, price)
        q.append((src, 0))
        stops = 0

        while q:
            stops += 1
    
            for _ in range(len(q)):
                node, curr_price = q.popleft()

                if stops > k+1:
                    continue 

                for conn, flight_price in adj_list[node]:
                    if curr_price + flight_price < price[conn]:
                        price[conn] = curr_price + flight_price
                        q.append((conn, curr_price + flight_price))
        
        if price[dst] == inf: return -1
        else: return price[dst]
