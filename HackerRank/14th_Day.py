#hackerrank day 14 - Scope
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0		


    def computeDifference(self):
        # maxelement = 0
        # minelement = 101
        # for i in self.__elements:
        #     if i < minelement:
        #         minelement = i
        #     elif i>maxelement:
        #         maxelement = i
        # self.maximumDifference = maxelement - minelement
        self.maximumDifference = abs(max(a)-min(a))


_ = input("enter:")
a = [int(e) for e in input("enter:").split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
