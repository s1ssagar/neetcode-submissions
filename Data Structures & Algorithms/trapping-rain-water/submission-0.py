class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left = 0
        right = N - 1
        total_area = 0
        left_max = 0
        right_max = 0

        while left < right:
            # print(left, right, left_max, right_max)

            if height[left] > left_max:
                left_max = height[left]
            if height[right] > right_max:
                right_max = height[right]

            if height[left] < height[right]:
                left += 1
                total_area += max(min(left_max, right_max) - height[left], 0)
            else:
                right -= 1
                total_area += max(min(left_max, right_max) - height[right], 0)
        return total_area