class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        
        left, right, lMax, rMax = 0, len(height)-1, 0, 0
        waterT = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= lMax:
                    lMax = height[left]
                else:
                    waterT += lMax - height[left]
                left += 1

            else:
                if height[right] >= rMax:
                    rMax = height[right]
                else:
                    waterT += rMax - height[right]
                right -= 1
        
        return waterT