"""Tests for :mod:`two_sum`, covering every example and constraint in README.md.

Run with either::

    python -m unittest test_two_sum -v
    python -m pytest test_two_sum.py     # optional, if pytest is installed
"""

import random
import unittest

from two_sum import Solution, two_sum


def brute_force_two_sum(nums: list[int], target: int) -> tuple[int, ...]:
    """Reference implementation: try every pair, O(n^2), used for cross-checking."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    raise ValueError("no pair")


def all_valid_pairs(nums: list[int], target: int) -> set[tuple[int, int]]:
    """Every index pair ``i < j`` whose values add up to ``target`` (O(n^2) oracle).

    Random inputs can contain several valid pairs, and the README allows the
    answer "in any order", so a correct solution may pick any one of them.
    """
    return {
        (i, j)
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
        if nums[i] + nums[j] == target
    }


class TestReadmeExamples(unittest.TestCase):
    """The three worked examples printed in the README."""

    def test_example_1(self) -> None:
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_example_2(self) -> None:
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_example_3_duplicate_values_not_same_element(self) -> None:
        # Two equal values at *different* indices; using one element twice is illegal.
        self.assertEqual(two_sum([3, 3], 6), [0, 1])


class TestLeetCodeSignature(unittest.TestCase):
    """``Solution.twoSum`` matches the signature advertised in the README."""

    def test_method_on_class(self) -> None:
        self.assertEqual(Solution().twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(Solution().twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(Solution().twoSum([3, 3], 6), [0, 1])


class TestEdgeCases(unittest.TestCase):
    """Boundary cases implied by the constraints section of the README."""

    def test_minimum_length_pair_at_both_ends(self) -> None:
        # `nums.length` is at least 2, so a two-element array must work.
        self.assertEqual(two_sum([-1, -2], -3), [0, 1])

    def test_negative_and_mixed_sign_values(self) -> None:
        self.assertEqual(two_sum([-3, 4, -5, 6], -8), [0, 2])

    def test_extreme_target_and_value_ranges(self) -> None:
        # README bounds: -1e9 <= nums[i] <= 1e9 and -1e9 <= target <= 1e9.
        self.assertEqual(two_sum([-(10**9), 10**9 - 1, 3], -1), [0, 1])
        self.assertEqual(two_sum([10**9, -(10**9), 7], 0), [0, 1])
        self.assertEqual(two_sum([-5, 0, 5], 0), [0, 2])

    def test_solution_found_for_last_element(self) -> None:
        # The answer uses index len(nums)-1; the loop must reach it.
        self.assertEqual(two_sum([1, 2, 3, 4, 100], 104), [3, 4])

    def test_zero_target_with_opposite_values(self) -> None:
        self.assertEqual(two_sum([5, -5, 3], 0), [0, 1])

    def test_unique_answer_is_scanned_left_to_right(self) -> None:
        # [1, 2, 3, 6] has exactly one valid pair (indices 0 and 3), matching the
        # "Only one valid answer exists" guarantee from the README.
        self.assertEqual(two_sum([1, 2, 3, 6], 7), [0, 3])

    def test_no_valid_answer_raises(self) -> None:
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 100)


class TestRandomizedAgainstBruteForce(unittest.TestCase):
    """The O(n) hash-map scan must agree with the O(n^2) brute-force oracle."""

    def test_returns_a_valid_pair_on_random_inputs(self) -> None:
        rng = random.Random(2026_10_16)
        checked = 0
        for _ in range(300):
            n = rng.randint(2, 40)
            nums = [rng.randint(-20, 20) for _ in range(n)]
            # Build the target from a real pair so at least one answer exists.
            a = rng.randrange(n)
            b = rng.randrange(n)
            while a == b:
                b = rng.randrange(n)
            target = nums[a] + nums[b]

            expected = all_valid_pairs(nums, target)
            self.assertTrue(expected, f"{nums} should contain a pair summing to {target}")

            got = two_sum(nums, target)
            self.assertEqual(len(set(got)), 2, f"same element used twice: {got}")
            self.assertIn(tuple(sorted(got)), expected,
                          f"{got} is not a pair summing to {target} in {nums}")
            self.assertEqual(nums[got[0]] + nums[got[1]], target)

            # When the input happens to have a unique answer, both scans must
            # report that exact pair - the case the README actually guarantees.
            if len(expected) == 1:
                self.assertEqual(sorted(got), list(brute_force_two_sum(nums, target)))
            checked += 1
        self.assertEqual(checked, 300)

    def test_matches_brute_force_on_the_readme_examples(self) -> None:
        for nums, target in (([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)):
            self.assertEqual(list(two_sum(nums, target)), list(brute_force_two_sum(nums, target)))


if __name__ == "__main__":
    unittest.main(verbosity=2)
