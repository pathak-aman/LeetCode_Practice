class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colour = dict()
        colour_dict = dict()
        ans = []

        for x,y in queries:
            if ball_colour.get(x,0):
                colour_dict[ball_colour[x]] -= 1
                if colour_dict[ball_colour[x]] == 0:
                    colour_dict.pop(ball_colour[x])
            
            ball_colour[x] = y
            colour_dict[y] = colour_dict.get(y,0) + 1
            ans.append(len(colour_dict))
        return ans