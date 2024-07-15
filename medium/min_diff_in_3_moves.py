class Solution(object):
    @staticmethod
    def asserts(list):
        assert 1 <= len(list) <= 10**5
        for i in list:
            assert -10**9 <= i <= 10**9
    @staticmethod
    def diff(list):
        return max(list) - min(list)

    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.asserts(nums)
        if len(nums) <= 4:
            return 0
        nums.sort()
        scenario1 = nums[3::]
        scenario2 = nums[:-3:]
        scenario3 = nums[2:-1:]
        scenario4 = nums[1:-2:]

        return min(self.diff(scenario1), self.diff(scenario2),
                   self.diff(scenario3), self.diff(scenario4))
