import pandas as pd 

def lengthOfLongestSubstring(s: str) -> int:
        idx_s = 0
        idx_e = 0
        result = 0
        for idx in range(len(s)):
            # if s[idx] not in s[idx_s:idx_e]:
            idx_e = idx
            if s[idx] in s[idx_s:idx]:
                if (idx_e - idx_s) > result:
                    result = idx_e - idx_s
                tmp_idx = s.index(s[idx], idx_s)
                idx_s = tmp_idx + 1
                idx_e = idx
        if idx_e - idx_s > result:
            result = idx_e - idx_s
        return result
s = "abcabcbb"
s.index("a", 1)
s[1:2]