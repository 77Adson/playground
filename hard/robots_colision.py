class Solution(object):
    @staticmethod
    def direction_check(dir):
        for el in dir:
            if el != dir[0]:
                return False
        return True

    @staticmethod
    def sort(positions):
        idx = []
        p_sorted = sorted(positions)
        for el in p_sorted:
            idx.append(positions.index(el))
        print('indexes:',idx)
        return idx


    def survivedRobotsHealths(self, positions, healths, directions):
        if self.direction_check(directions):
            return healths

        stack = []
        for i in self.sort(positions):
            print(i, directions[i])
            if directions[i] == 'R':
                stack.append(i)
            else:
                while len(stack) != 0:
                    if healths[i] > healths[stack[-1]]:
                        healths[i] -= 1
                        healths[stack[-1]] = 0
                        stack.pop()
                    elif healths[i] < healths[stack[-1]]:
                        healths[stack[-1]] -= 1
                        healths[i] = 0
                        stack.pop()
                    elif healths[i] == healths[stack[-1]]:
                        healths[i] = 0
                        healths[stack[-1]] = 0
                        stack.pop()
            print('s', stack)
            print('h', healths)
        healths = [el for el in healths if el != 0]
        return healths

p = [3,5,2,6]
h = [10,10,15,12]
d = "RLRL"
s = Solution()
print('return:', s.survivedRobotsHealths(p,h,d))
