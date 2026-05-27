class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = ""
        for i in s:
            if i.isalnum():
                s1+=i.lower()
        i,j = 0,len(s1)-1
        while i < j:
            if s1[i] == s1[j]:
                i+=1
                j-=1
            else:
                return False
        return True