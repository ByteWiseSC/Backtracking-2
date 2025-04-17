from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given a list of integers `nums`, returns all possible subsets (the power set).

        This is solved using backtracking, where at each step we decide whether to include 
        the current number or skip it. The algorithm ensures that all subsets are explored 
        by advancing the index and backtracking after each decision.

        ------------------------------
        Complexity Analysis
        ------------------------------

        Let:
        - N = length of the input list `nums`

        Time Complexity: O(2^N)
            - Each element has two choices: include or exclude.
            - This results in 2^N total subsets.

        Space Complexity: O(N)
            - O(N) for the recursion stack depth.
            - Each subset can have up to N elements, and we maintain a path during recursion.
            - Output list (with 2^N subsets) is not included in auxiliary space.

        Note:
        - This approach avoids duplicate subsets since the index always advances forward.
        - The path is modified in place and backtracked by popping the last element.
        """
        result = []

        def helper(subset: List[int], idx: int):
            result.append(subset[:])  # Copy the current subset to avoid reference issues

            for i in range(idx, len(nums)):
                subset.append(nums[i])         # Choose the current element
                helper(subset, i + 1)          # Explore further with it included
                subset.pop()                   # Backtrack: remove the last element

        helper([], 0)
        return result



from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given a list of integers `nums`, returns all possible subsets (the power set)
        using an iterative approach.

        This solution builds the power set by iteratively adding each number to 
        all existing subsets in the result list.

        ------------------------------
        Complexity Analysis
        ------------------------------

        Let:
        - N = length of the input list `nums`

        Time Complexity: O(2^N)
            - There are 2^N possible subsets.
            - For each number, we create new subsets by copying existing ones and adding the number.

        Space Complexity: O(2^N)
            - We store 2^N subsets in the result.
            - Each subset takes up to O(N) space, but auxiliary space (not counting result) is minimal.

        Note:
        - This approach uses list slicing to copy subsets without modifying the originals.
        - Unlike the recursive method, there's no stack usage, making this memory-efficient for shallow inputs.
        """
        result = [[]]  # Start with the empty subset

        for i in range(len(nums)):
            le = len(result)
            for j in range(le):
                newList = result[j][:]     # Copy the j-th existing subset
                newList.append(nums[i])    # Add current element to it
                result.append(newList)     # Add the new subset to the result

        return result
