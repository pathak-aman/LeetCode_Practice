class Solution:
    def numIslands(self, grid):
        ones = []
        for i in range(len(grid)):
            for k in range(len(grid[i][0])):
                if grid[i][0][k] == '1':
                    ones.append((i,k))
        buckets = []
        for i in range(len(ones)):
            in_set = False
            for j in range(i+1,len(ones)):
                if abs(ones[i][0]-ones[j][0]) == 1 or abs(ones[i][1]-ones[j][1]) == 1:
                    if ones[i][0] == ones[j][0]:
                        if abs(ones[i][1]-ones[j][1]) == 1:
                            if not buckets:
                                buckets.append({ones[i],ones[j]})
                                in_set = True
                            else:
                                present = False
                                for bucket in buckets:
                                    if not bucket.isdisjoint({ones[i],ones[j]}):
                                        present = True
                                        bucket.update(bucket.union({ones[i],ones[j]}))
                                        in_set = True
                                        break
                                if not present:
                                    in_set = True
                                    buckets.append({ones[i],ones[j]})

                    elif ones[i][1] == ones[j][1]:

                        if abs(ones[i][0]-ones[j][0]) == 1:
                            if not buckets:
                                buckets.append({ones[i], ones[j]})
                                in_set = True
                            else:
                                present = False
                                for bucket in buckets:
                                    if not bucket.isdisjoint({ones[i], ones[j]}):
                                        present = True
                                        bucket.update(bucket.union({ones[i], ones[j]}))
                                        in_set = True
                                        break
                                if not present:
                                    in_set = True
                                    buckets.append({ones[i], ones[j]})

            print(in_set)
        print(buckets,len(buckets))

obj1 = Solution()
d = [['11000'],['11000'],['00100'],['00011']]
obj1.numIslands(d)

'''
11000
11000
00100
00011
'''