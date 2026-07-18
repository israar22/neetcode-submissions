class Solution:
    def isValid(self, s: str) -> bool:
        p={
        ')':'(','}':'{',']':'['
        }
        a=[]

        for i in s:
            if i in '({[':
                a.append(i)
            elif i in '}])':
                if not a or a[-1]!=p[i]:
                    return False
                a.pop()
        return len(a)==0

        