"""
lab_1d.py

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Derived from LeetCode problem: https://leetcode.com/problems/two-sum/ (leetcode easy)
"""

def binary_search_left(a, x):
    l = 0
    r = len(a) - 1
    while l < r:
        mid = (l + r) // 2
        if a[mid][0] < x:
            l = mid + 1
        else:
            r = mid
    
    return l if a[l][0] == x else -1


# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Function that takes in a list of integers and a target integer, and returns the indices of the two numbers that add up to the target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target integer.
    
    Returns:
        list[int]: Indices of the two numbers that add up to the target.
    """

    newNums = [(num, i) for i, num in enumerate(nums)]
    newNums.sort(key=lambda x: (x[0], x[1]))
    for i, item in enumerate(newNums):
        search = binary_search_left(newNums, target - item[0])
        if search != -1 and i != search:
            return [newNums[i][1], newNums[search][1]]

    return []  # In case there is no solution, though the problem guarantees one exists.

# Example usage:
def main():
    nums = [11, 7, 13, 2]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

if __name__ == "__main__":
    main()