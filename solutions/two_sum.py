#!/usr/bin/env python3
"""LeetCode Two Sum - Python 3 solution with self-validation.

Run:
    python3 solutions/two_sum.py

Prints each example result and exits 0 only when all three pass;
any failing assert terminates with a non-zero exit status.
"""
from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the indices of the two numbers adding up to target.

    Single pass over nums with a value -> index hash map: O(n) time,
    O(n) space. The partner index is recorded before the current index,
    so an element is never paired with itself.
    """
    seen = {}
    for i, value in enumerate(nums):
        need = target - value
        if need in seen:
            return [seen[need], i]
        seen[value] = i
    raise ValueError("exactly one valid answer must exist")


if __name__ == "__main__":
    examples = [
        # (nums, target, expected)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    for nums, target, want in examples:
        got = two_sum(list(nums), target)
        print(f"nums={nums} target={target} -> {got} expected {want}")
        assert got == want, f"nums={nums} target={target}: got {got}, expected {want}"
    print("all examples passed")
