'''
Understanding the probem -  
    Input = array of strings strs
    Goal = group the anagrams together 
    Output = return the group of anagrams. 

Constraints - 
    What if the strs is empty 
    What is the max length of strs 
    Can strs have all lowercase, or can it have different 

Examples - Input: strs = ["eat","tea","tan","ate","nat","bat"]
           Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
         - Input: strs = [""], Output: [[""]]
         - Input: strs = ["a"], Output: [["a"]]

Approach - 
    - create an empty dictionary called res for storing the final output 
    - iterate through string in array 
    - initialize count of 0 * 26 characters 
    - iterate thourgh the character in string 
    - update the count by 1for each character in the count table, by subracting ascii value of char from a 
    - convert the count into tuple and append it to the result with the string and key(count)
    - return the list of res
    - Space Complexity = o(n), Time Complexity = O(m * n)
    - m being the number of string and n being the length of longest string
'''
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # result empty list which stores the final output
        result = defaultdict(list)

        #iterate through each string
        for string in strs:

            # key is the count of each character in the string
            key = [0] * 26

            # ietrate through each character in the string
            for character in string:

                # building the key, like 0 1 0 1 0 0 0 0 0 .......
                key[ord(character) - ord('a')] += 1
            
            # append the key and value to result
            result[tuple(key)].append(string)
        
        return list(result.values())
        


        