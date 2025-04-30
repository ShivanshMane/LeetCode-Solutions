class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest = 0 
        for num in num_set:
            if (num - 1) not in num_set:   # checking if this is the start of the sequence 
                length = 1               # set the length to 1 as this is the start of sequence
                while( num + length) in num_set :  # if num + length in set, means seq continues
                    length += 1
                longest = max(length, longest)
        return longest