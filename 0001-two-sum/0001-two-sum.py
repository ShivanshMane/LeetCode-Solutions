'''
Understanding the problem - 
    Input = array of integers nums, integer target
    Goal = find the indices of two numbers such that they add up to the target
    Output = return those indices

Constraints - 
    Can the array contain duplicates
    What if the array is empty 
    What if the array consist of just 1 integer
    What is the max length of the array nums
    What if no solution exists

Examples - 
    Input: nums = [2,7,11,15], target = 9, Output: [0,1]
    Input: nums = [2], target = 9, Output: []
    Input: nums = [], target = 9, Output: []

Approach - 
    We can use a dictionary 
    Condition to satisfy = a + b = target 
    reverse it, it becomes, complement = target - a
    now we iterate through the nums array, check if complement(target - number at current index) exist in the hashset
    If yes, return the index of current integer, and return the index of complement from the hashset 
    else return empty list
    Space Complexity = O(n), Time Complexity = O(n)
'''
class Solution:
   def twoSum(self, nums: list[int], target: int) -> list[int]:
    # creating a hashset
    nums_hashset = {}

    # iterate through the array nums
    for index, integer in enumerate(nums):

        #equation for complement 
        complement = target - integer

        #condition to check if the complement exists in hashset
        if complement in nums_hashset:
            return[index, nums_hashset[complement]]
        
        # if complement not in hashset, add it 
        nums_hashset[integer] = index
    
    return []


    

        