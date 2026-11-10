
'''
Understand the problem -
    Input = integer array called nums
    Goal = find if any value(integer) appears twice in that array
    Output = return true if value appears twice otherwise false

Constraints -
    What if the array is empty
    What if array has just 1 number
    What if the max size of the array
    Can the array have negative integers 

Examples - 
    Input: nums = [1,2,3,1], Output: true
    Input: nums = [1,2,3,4], Output: false
    Input: nums = [], Ouput: False

Approach - 
    Create an empty hashset 
    Iterate through the integer array nums
    check if the integer present in the hashset
    If its present, return True
    If not, add that integer to tha hashset
    outside the loop return False 
    Time Complexity = O(n), Space Complexity = O(n)
    n here being the total integers in the integer array nums

We use a hashset here , coz hashset cannot have duplicates
'''
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for integer in nums:
            if integer in seen:
                return True
            seen.add(integer)
        return False
        