// Package twosum solves the LeetCode "Two Sum" problem.
package twosum

// TwoSum returns the indices of the two numbers in nums that add up to target.
//
// Each element may be used at most once, so the two returned indices always
// refer to distinct elements. The input is guaranteed to contain exactly one
// valid answer; nil is returned when no such pair exists. The answer is
// produced in a single pass over nums using a value-to-index lookup table,
// which gives O(n) time and O(n) extra space.
func TwoSum(nums []int, target int) []int {
	seen := make(map[int]int, len(nums))
	for i, n := range nums {
		if j, ok := seen[target-n]; ok {
			return []int{j, i}
		}
		// Keep the first index of each value so an earlier duplicate can
		// still pair with the current element instead of being shadowed by it.
		if _, ok := seen[n]; !ok {
			seen[n] = i
		}
	}
	return nil
}
