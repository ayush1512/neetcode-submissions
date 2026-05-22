class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in strs:
            s+=i
            s+=";"

        return s

    def decode(self, s: str) -> List[str]:
        res =  list(s.split(";"))
        return res[:len(res)-1]