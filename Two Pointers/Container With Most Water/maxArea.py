class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_water = -1

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            max_water = max(max_water, height * width )

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_water