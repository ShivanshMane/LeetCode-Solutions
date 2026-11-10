'''
Understanding the problem - 
    Input = integer array nums
    Goal = build a list which stores product of array execpt self at that index
    Output = return the list 

Constrainst - 
    what if the array is empty 
    what if the array has just 1 inetger
    what is the maximum length of the array 
    can the array have negative integers

Examples - 
    Input: nums = [1,2,3,4], Output: [24,12,8,6]
    Input: nums = [-1,1,0,-3,3], Output: [0,0,9,0,0]
    Input: nums = [1], Output: [1]

Approach - 
    create a result array, length of the nums array which has 1 at all positions
    initaizle prefix = 1 
    iterate through the nums array 
    update result[i] with prefix 
    then prefix will be multiplied with the num
    initialize postfix with 1 
    iterate in the reverse order
    result[i] will be multiplied by postfix 
    then postifx will be multiplied by nums[i]
    return res
    Space Complexiy = O(n) , Time Complexity = O(n)
'''
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
        