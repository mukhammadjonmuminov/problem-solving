class Solution:
    def romanToInt(self, s: str) -> int:
        s_v = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result=s_v[s[-1]]
        for i in range(len(s)-1):
            if s_v[s[i]] >= s_v[s[i+1]]:
                result += s_v[s[i]]
            else:
                result -= s_v[s[i]]
        return result
