from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        freq = []
        i = 0

        while i < len(nums):

            num = nums[i]
            count = 1

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                count += 1
                i += 1

            freq.append((num, count))
            i += 1

        freq.sort(key=lambda x: x[1], reverse=True)
        ans = []

        for i in range(k):
            ans.append(freq[i][0])

        return ans


sol = Solution()
print(sol.topKFrequent([1,2,2,3,3,3], 2))