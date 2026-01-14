class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        x=[]
        string=0


        if s == " ":
            return 1
        for item in range(len(s)):

            for i in range(item,len(s)):
                if item != i and s[i] not in x:
                    x.append(s[i])
                else:
                    if string < len(x):

                        string = len(x)

                    x = []
                    x.append(s[i])

        return int(string) if string > len(x) else len(x)




c=Solution()
print(c.lengthOfLongestSubstring("pwwkew"))