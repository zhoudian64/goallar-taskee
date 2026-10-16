# goallar-taskee

You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

## Solution (Python)

The problem above is Two Sum. The Python solution lives in:

- `two_sum.py` - one-pass hash table implementation. `Solution.twoSum(nums, target)` matches the signature used in the statement; `two_sum(...)` is the plain function it delegates to.
- `test_two_sum.py` - unit tests covering all three examples plus the boundary cases implied by the constraints, cross-checked against an O(n^2) brute-force oracle and the doctests inside `two_sum.py`.

Idea: scan the array once, remembering every value already seen with its index. For the current value `num`, the partner must be `target - num`; if that complement was seen earlier we have the answer, otherwise record `num` and continue. Registering the index *after* the lookup is what prevents using the same element twice (`nums = [3, 3]`, `target = 6` still returns `[0, 1]`).

Complexity: time `O(n)`, space `O(n)`.

Run the tests with either of:

```sh
python -m unittest test_two_sum -v   # stdlib only
python -m pytest test_two_sum.py     # optional, if pytest is installed
python two_sum.py                    # runs the doctests as a smoke test
```

