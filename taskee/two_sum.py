"""Two Sum in Python.

Given ``nums`` and ``target``, return the indices of the two numbers that add up
to ``target``. Exactly one valid answer exists, and the same element may not be
used twice. Indices are returned as ``(lower_index, higher_index)``.
"""

from __future__ import annotations


def two_sum(nums: list[int], target: int) -> tuple[int, int]:
    seen: dict[int, int] = {}
    for index, value in enumerate(nums):
        partner = seen.get(target - value)
        if partner is not None:
            return partner, index
        seen.setdefault(value, index)
    raise ValueError(f"no pair in {nums} adds up to {target}")
