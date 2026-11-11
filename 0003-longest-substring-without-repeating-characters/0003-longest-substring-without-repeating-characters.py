'''
Understanding the problem - 
    Input = string s, which has charcaters and can have duplicates
    Goal = find the max length of substring without repeated characters
    Output = return the max lenght of the substring without character replacement 

Constraints - 
    what if the string is empty 
    what if the string has just 1 character
    what is the max length of the string 
    can the string have uppercase, specialized characters (symbols)

Examples -  
    Input: s = "abcabcbb", Output: 3
    Input: s = "bbbbb", Output: 1
    Input: s = "pwwkew", Output: 3
    Input: s = "p", Output: 1
    Input: s = "", Output: 0

Approach - 
    Initialize left to 0 
    Iterate through the string s 
    check if the character at index 0 is present in the hashset 
    if yes, remove the left character from the hashset 
    increment l by 1 
    else add character to hashset 
    longest = max(longest, r - l + 1)
    return longest    

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        longest = 0 
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[r])
            longest = max(longest, r - left + 1)
        return longest
