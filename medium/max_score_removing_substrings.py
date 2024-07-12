class Solution(object):

    @staticmethod
    def asserts(s, x, y):
        assert 1 <= len(s) <= 10 ** 5
        assert 1 <= x, y <= 10 ** 5
        assert s.islower()

    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
            points for substring 'ab'
        :type y: int
            points for substring 'ba'
        :rtype: int
        """
        self.asserts(s, x, y)
        if x >= y:
            prio = ('ab', 'ba')
            print('najpierw ab')
        else:
            prio = ('ba', 'ab')
            print('najpierw ba')

        score = 0
        s = list(s)
        stack = []
        for i in s:
            stack.append(i)
            if len(stack) >= 2 and stack[-1] + stack[-2] == prio[1]:
                stack.pop()
                stack.pop()
                score += max(x, y)
        s = []
        for i in stack:
            s.append(i)
            if len(s) >= 2 and s[-1] + s[-2] == prio[0]:
                stack.pop()
                stack.pop()
                score += min(x, y)

