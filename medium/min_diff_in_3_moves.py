class Solution(object):
    @staticmethod
    def asserts(list):
        assert 1 <= len(list) <= 10**5
        for i in list:
            assert -10**9 <= i <= 10**9
    @staticmethod
    def max_minus_min(list):
        return max(list) - min(list)

    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.asserts(nums)
        if len(nums) <= 4:
            return 0

        steps = 3
        nums = sorted(nums)
        while steps != 0:
            nums_min = nums[1::]
            nums_max = nums[:-1:]
            if self.max_minus_min(nums_max) > self.max_minus_min(nums_min):
                nums = nums_min
            else:
                nums = nums_max
            steps -= 1
        return self.max_minus_min(nums)