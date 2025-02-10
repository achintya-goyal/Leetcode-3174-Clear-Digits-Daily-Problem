# lear Digits (LeetCode 3174)

Description

This Python function solves LeetCode problem 3174 - Clear Digits. It removes all digits from a given string. Additionally, for each digit removed, the closest preceding letter (if any) is also removed.

Functionality

Iterates through the string.

Removes any digit found.

If a digit is removed, the closest preceding letter is also removed.

Returns the modified string.

Example

sol = Solution()
print(sol.clearDigits("a1b2c3"))

Output:

""

Usage

Clone this repository.

Run the script with any string input to remove digits along with their closest preceding letters.

Complexity

The worst-case time complexity is O(n²) due to string slicing operations inside loops.

LeetCode Link

LeetCode 3174 - Clear Digits

Author

[Your Name]

