class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        t_dict = dict(Counter(t))
        t_dict_temp = dict(Counter(t))
        min_str: str = ""
        min_str_len: int = sys.maxsize

        left = 0
        right = 0

        while right < N:
            if s[right] not in t_dict_temp and t_dict == t_dict_temp:
                left = right
                left += 1
            elif s[right] in t_dict_temp:
                t_dict_temp[s[right]] -= 1
                if t_dict_temp[s[right]] == 0:
                    t_dict_temp.pop(s[right])
            right += 1

            if t_dict_temp == {}:
                t_dict_temp = deepcopy(t_dict)
                if right - left < min_str_len:
                    min_str = s[left:right]
                    min_str_len = len(min_str)
                while left < right:
                    left += 1
                    try:
                        if s[left] in t_dict_temp:
                            break
                    except:
                        pass
                right = left

        return min_str