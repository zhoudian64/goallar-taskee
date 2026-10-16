"""Solution for the "Two Sum" problem described in README.md.

Problem
-------
Given an array of integers ``nums`` and an integer ``target``, return the
indices of the two numbers that add up to ``target``.

* Each input has exactly one valid answer.
* The same element may not be used twice (``nums[i] + nums[i]`` does not count).
* The answer may be returned in any order.

Approach
--------
One-pass hash table. While scanning the array we remember every value already
seen together with its index. For the current value ``num`` the partner we are
looking for is ``target - num``; if that complement was seen earlier we have
found the pair, otherwise we record ``num`` and continue.

Storing the index *after* the lookup is what enforces "not using the same
element twice": with ``nums = [3, 3]`` and ``target = 6`` the first ``3`` is
only registered once its own complement lookup has failed, so the second ``3``
pairs it with index ``0`` instead of pairing with itself.

Complexity: time ``O(n)``, space ``O(n)`` — one pass over ``n`` values and one
dictionary holding at most ``n`` entries. This satisfies the constraints in the
README (``nums.length <= 1e4``, values and target within ``±1e9``); Python's
arbitrary-precision integers mean no overflow concerns.
"""


class Solution:
    """LeetCode-compatible wrapper (``def twoSum(self, nums, target) -> list[int]``)."""

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return two_sum(nums, target)


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return the two indices whose values sum to ``target``.

    Raises :exc:`ValueError` when no such pair exists, which the README
    guarantees cannot happen for valid input ("Only one valid answer exists").

    >>> two_sum([2, 7, 11, 15], 9)
    [0, 1]
    >>> two_sum([3, 2, 4], 6)
    [1, 2]
    >>> two_sum([3, 3], 6)
    [0, 1]
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        # Index of a previously seen value that completes the sum, if any.
        partner = seen.get(target - num)
        if partner is not None:
            return [partner, i]
        # Registered after the lookup so `num` can never pair with itself.
        seen[num] = i
    raise ValueError(f"no two numbers in {nums} add up to {target}")


if __name__ == "__main__":
    import doctest

    assert doctest.testmod(verbose=True)[0] == 0
