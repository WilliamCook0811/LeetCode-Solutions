class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1

        bestarea = 0

        while left < right:
            currentarea = (right-left)* min(height[left], height[right])

            bestarea = max(currentarea, bestarea)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return bestarea
