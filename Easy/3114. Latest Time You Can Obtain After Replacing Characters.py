class Solution:
    def findLatestTime(self, s: str) -> str:
        listt = list(s)
        for i in range(len(listt)):
            if i == 0 and listt[i] == "?":
                listt[i] = "1" if listt[i+1] in "01?" else "0"
                continue
            if i == 1 and listt[i] == "?":
                listt[i] = "9" if listt[i-1] == "0" else "1"
                continue
            if i == 3 and listt[i] == "?":
                listt[i] = "5"
                continue
            if i == 4 and listt[i] == "?":
                listt[i] = "9"

        return ''.join(listt)
