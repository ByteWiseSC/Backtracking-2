from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Given a string `s`, return all possible palindrome partitioning of `s`.

        Each partition should contain only substrings that are palindromes.
        The solution uses backtracking to explore all possible partitions and
        validates palindromes using a helper function.

        ------------------------------
        Complexity Analysis
        ------------------------------

        Let:
        - N = length of the string `s`

        Time Complexity: O(2^N * N)
            - There are O(2^N) possible partitioning combinations (each character has a "cut" or "no cut" option).
            - For each substring, we may check if it's a palindrome in O(N) time.
            - Hence, total time = O(2^N * N)

        Space Complexity: O(N)
            - O(N) for the recursion stack and the current path list during backtracking.
            - Output list (which can have up to 2^N partitions) is not included in auxiliary space.

        Note:
        - The solution uses backtracking with in-place list mutation (path) and backtracking (pop) to explore all paths.
        - Palindrome checking is done via a two-pointer approach in O(N) time.
        """
        result = []

        def helper(s: str, pivot: int, path: List[str]):
            # Base case: if we've reached the end of the string, store the valid partition
            if pivot == len(s):
                result.append(path[:])
                return

            # Explore all substrings starting from `pivot`
            for i in range(pivot, len(s)):
                substr = s[pivot:i + 1]

                # Check if the current substring is a palindrome
                if self.isPalindrome(substr):
                    path.append(substr)          # Choose
                    helper(s, i + 1, path)       # Explore
                    path.pop()                   # Un-choose (backtrack)

        helper(s, 0, [])
        return result

    def isPalindrome(self, s: str) -> bool:
        """
        Returns True if the input string `s` is a palindrome.
        """
        start, end = 0, len(s) - 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
