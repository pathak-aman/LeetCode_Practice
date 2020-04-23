from sortedcontainers import SortedSet
class Solution:
    def displayTable(self, orders):
        table_num = SortedSet()
        dishes = SortedSet()
        for i in orders:
            table_num.add(int(i[1]))
            dishes.add(i[2])
        menu = dict()

        for i in dishes:
            menu[i] = 0
        table_menu = dict()

        for i in table_num:
            table_menu[i] = menu.copy()

        for i in orders:
            table_menu[int(i[1])][i[2]] +=1

        output = []
        temp_output = ['Table']
        for i in dishes:
            temp_output.append(i)
        output.append(temp_output)

        for i in table_menu:
            temp_output = []
            temp_output.append(str(i))
            for j in table_menu[i]:
                temp_output.append(str(table_menu[i][j]))
            output.append(temp_output)
        return output


obj1 = Solution()
a = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
print(obj1.displayTable(a))
