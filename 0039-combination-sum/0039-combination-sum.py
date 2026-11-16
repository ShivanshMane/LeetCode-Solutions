'''
Approach – DFS + Backtracking
1. Initialize an empty result list to store all valid combinations.
2. Use a DFS helper function that keeps track of the current index, the current combination, and the sum of selected numbers.
3. At every recursive call, check the base cases:
- If the current sum equals the target, add a copy of the current combination to the result and return.
- If the current sum exceeds the target or we have reached the end of the array, return.
4. Include the current number:
- Add the current number to the combination.
- Recursively call DFS with the same index because we are allowed to reuse numbers.
- Update the current sum by adding the selected number.
5. Backtrack:
- Remove the last added number using pop() to undo the previous choice.
6. Skip the current number:
- Recursively call DFS with the next index without changing the current combination or sum.
7. Start DFS from index 0 with an empty combination and sum 0.
8. Return the result containing all valid combinations.
'''
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        # index , current is the list, total is the total sum(possibilities)
        def dfs(index, current, total):
            # base case 1, we return the copy as current is mutable list we update it frequently 
            if target == total :
                res.append(current.copy())
                return 
            #base case 2 
            if target < total or index == len(candidates):
                return 
            # append the number to current 
            current.append(candidates[index])
            # call dfs with nums[i]
            dfs(index, current, total + candidates[index])
            # backtracking, going back and removing the last added elememt
            current.pop()
            # calling dfs again with next index number 
            dfs(index + 1, current, total)
           # going back into dfs 
        dfs(0,[],0)
        return res



        