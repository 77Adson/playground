class Solution(object):
    def __init__(self):
        self.formula = None
        self.stack = []
        self.dic = {}

    def get_count(self):


    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        dic = {}
        self.formula = formula
        for i in range(len(self.formula) - 1):
            if self.formula[i] == '(':
                self.stack.append(dic)
            elif self.formula[i] == ')':
                self.stack.pop()
            print(self.stack)

s = Solution()
f = "K4(ON(SO3)2)2"
s.countOfAtoms(f)