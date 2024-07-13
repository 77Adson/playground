class Solution(object):
    @staticmethod
    def direction_check(dir):
        for el in dir:
            if el != dir[0]:
                return False
        return True

    def survivedRobotsHealths(self, positions, healths, directions):

        """
        :type positions: List[int]
        :type healths: List[int]
        :type directions: str
        :rtype: List[int]
        """

        if self.direction_check(directions):
            return healths

        directions = list(directions)
        position_lim = max(positions)
        while not self.direction_check(directions):
            for i in range(len(positions)):
                if directions[i] == 'R':
                    positions[i] += 1
                    if positions[i] > position_lim:
                        positions[i] = 1
                else:
                    positions[i] -= 1
                    if positions[i] < 1:
                        positions[i] = position_lim

            i = 0
            while i in range(len(positions) - 1):
                j = i + 1
                if positions[i] == positions[j]:
                    if healths[i] > healths[j]:
                        healths.remove(healths[j])
                        healths[i] -= 1

                        positions.remove(positions[j])
                        directions.remove(directions[j])


                    elif healths[i] == healths[j]:
                        healths.remove(healths[j])
                        healths.remove(healths[i])

                        positions.remove(positions[j])
                        positions.remove(positions[i])
                        directions.remove(directions[j])
                        directions.remove(directions[i])

                    elif healths[i] < healths[j]:
                        healths.remove(healths[i])
                        healths[j] -= 1

                        positions.remove(positions[i])
                        directions.remove(directions[i])
                i += 1
        return healths


positions = [3, 5, 2, 6]
healths = [10, 10, 15, 12]
directions = "RLRL"
wynik = Solution()
print(wynik.survivedRobotsHealths(positions, healths, directions))
