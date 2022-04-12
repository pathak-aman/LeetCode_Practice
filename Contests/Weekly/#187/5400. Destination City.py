class Solution:
    def destCity(self, paths) -> str:
        city_path = dict()
        for i in paths:
            city_path[i[0]] = i[1]
        print(city_path)
        a = city_path.keys()
        for i in city_path.values():
            if not i in a:
                return i


obj1 = Solution()
print(obj1.destCity(paths = [["A","Z"]]))