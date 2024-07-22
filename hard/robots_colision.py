class Solution(object):
    @staticmethod
    def direction_check(dir):
        return all(el == dir[0] for el in dir)

    @staticmethod
    def sort(positions):
        # Sort positions and return the corresponding indexes
        indexed_positions = sorted(enumerate(positions), key=lambda x: x[1])
        return [index for index, _ in indexed_positions]

    @staticmethod
    def asserts(p, h, d):
        assert 1 <= len(p) == len(h) == len(d) <= 10 ** 5, "Length assertion failed"
        assert 1 <= max(p) <= 10 ** 9 and 1 <= max(h) <= 10 ** 9, "Value range assertion failed"
        assert set(d) <= {'R', 'L'}, "Direction set assertion failed"
        assert len(p) == len(set(p)), "Unique positions assertion failed"

    def survivedRobotsHealths(self, positions, healths, directions):
        self.asserts(positions, healths, directions)
        if self.direction_check(directions):
            return healths

        stack = []
        for i in self.sort(positions):
            if directions[i] == 'R':
                stack.append(i)
            else:
                while len(stack) != 0 and healths[i] > 0:
                    if healths[i] < healths[stack[-1]]:
                        healths[stack[-1]] -= 1
                        healths[i] = 0
                    elif healths[i] > healths[stack[-1]]:
                        healths[i] -= 1
                        healths[stack[-1]] = 0
                        stack.pop()
                    elif healths[i] == healths[stack[-1]]:
                        healths[i] = 0
                        healths[stack[-1]] = 0
                        stack.pop()
        healths = [el for el in healths if el != 0]
        return healths


s = Solution()
p = [11, 44, 16]
h = [1, 20, 17]
d = "RLR"
print(s.survivedRobotsHealths(p, h, d))
