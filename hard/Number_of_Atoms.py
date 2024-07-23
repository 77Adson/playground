class Solution(object):
    def __init__(self):
        self.atom = ''
        self.stack = []
        self.dic = {}

    def append_dic(self):
        num = 1
        num2 = ''
        key = self.stack.pop()
        while key.isnumeric():
            num2 += key
            key = self.stack.pop()
        if num2 != '':
            num = int(num2[::-1])

        if key in self.dic:
            self.dic[key] += num
        else:
            self.dic[key] = num

    def multiplier(self, i):
        if i + 1 < len(self.atom) and self.atom[i + 1].isnumeric():  # Check if i+1 is within bounds
            return int(self.atom[i + 1])
        else:
            return 1

    def update_dic(self, mult):
        for key in self.dic:
            self.dic[key] *= mult

    def countOfAtoms(self, formula):
        self.atom = '('+formula+')'
        i = 0
        while i in range(len(self.atom)):
            if self.atom[i] == ')':
                mult = self.multiplier(i)
                while self.stack[-1] != '(':
                    self.append_dic()
                self.stack.pop()
                self.update_dic(mult)
                i += 1


            elif self.atom[i] == '(':
                self.stack.append(self.atom[i])

            elif self.atom[i + 1].islower():
                self.stack.append(self.atom[i] + self.atom[i + 1])
                i += 1
            else:
                self.stack.append(self.atom[i])
            i += 1
            print(self.stack, self.dic)

        parts = [
            elem + str(counter) if not counter == 1 else elem for elem, counter in self.dic.items()
        ]
        parts.sort()

        return "".join(parts)


atom = "Be32"
s = Solution()
print(s.countOfAtoms(atom))
