'''
Understand the problem - 
    Input = two strings s and t
    Goal = find if t is anagram of s 
    Output = return True if yes, else False

Constraints - 
    What if the strings are empty
    What if s is empty 
    What if t is empty
    What is the max lenght of both the strings 
    Can the strings contain lowercase, uppercase characters

Examples - 
    Input: s = "anagram", t = "nagaram", Output: true
    Input: s = "rat", t = "car, Output: false

Approach - 
    Use two different hashmaps for s and t 
    Calculate count for each string and append it to the hashmap(key value pairs)
    Compare the hashmaps using the count function 
    If same, return True else return False
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Hashmap_s = {}
        Hashmap_t = {}

        for character in s:
            Hashmap_s[character] = Hashmap_s.get(character, 0) + 1

        for character in t:
            Hashmap_t[character] = Hashmap_t.get(character, 0) + 1 
        
        return Hashmap_s == Hashmap_t