'''
Approach = 
    initialize two pointers left and right 
    left will be index 0 
    right will be len(height) - 1
    iterate through the array height using while loop
    initialize h, with min height of left, height of right
    then initialize width with right - left
    and area will be h * width 
    then use max function to find maxarea and area
    then check if height of left is smaller than height of right
    increment left else increment right 
    return maxarea
    Space Complexity = O(n), Time Complexity = O(n)
    n being the number of integers in the array height
'''
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0 
        right = len(height) - 1
        max_area = 0 
        while left < right:
            h = min(height[left], height[right])
            width = right - left 
            area = h * width
            max_area = max(area, max_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
        