class Solution:
    def clearDigits(self, s: str) -> str:
        n = len(s)
        i = 0
        while(i<n):
            if s[i].isdigit():
                s = s[:i] + s[i+1:]
                j=i-1
                n-=1
                i-=1
                while(j>=0):
                    if s[j].isalpha():
                        s = s[:j] + s[i+1:]
                        j = -1
                        n -= 1
                        i = -1
                    else:
                        j -= 1
                        n-=1
            i+=1
        return s
