class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        right = 1
        N = len(s)
        if N <= 1:
            return 0 if N == 0 else 1
        window = set(s[0])
        max_len = -1

        while right < N:
            if s[right] in window:
                while left < right and s[right] != s[left]:
                    window.discard(s[left])
                    left += 1
                window.discard(s[left])
                left += 1
                window.add(s[right])
            else:
                window.add(s[right])
            right += 1
            if len(window) > max_len:
                max_len = len(window)
        return max_len