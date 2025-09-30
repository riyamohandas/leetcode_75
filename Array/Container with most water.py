class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate area between left and right
            h = min(height[left], height[right])
            w = right - left
            max_area = max(max_area, h * w)

            # Move the pointer of the smaller line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
