package main

import "fmt"

// twoSum returns the indices of the two numbers in nums that add up to target.
//
// It scans nums once, keeping a hash set/map of "value -> index" for every
// value already consumed. For the current element we look up its complement
// (target - nums[i]); because the partner was stored before the current index
// is recorded, an element can never be paired with itself. O(n) time, O(n) space.
func twoSum(nums []int, target int) []int {
	seen := make(map[int]int, len(nums))
	for i, num := range nums {
		need := target - num
		if j, ok := seen[need]; ok {
			return []int{j, i}
		}
		seen[num] = i
	}
	// The problem guarantees exactly one valid answer, so this is unreachable.
	panic("twoSum: no matching pair found")
}

// equal reports whether got and want are the same index pair.
func equal(got, want []int) bool {
	if len(got) != 2 || len(want) != 2 {
		return false
	}
	return got[0] == want[0] && got[1] == want[1]
}

// verify runs one example from the README and panics if the result is wrong.
func verify(label string, nums []int, target int, want []int) {
	got := twoSum(nums, target)
	fmt.Printf("%-34s got [%d,%d] want [%d,%d]\n", label, got[0], got[1], want[0], want[1])
	if !equal(got, want) {
		panic(fmt.Sprintf("%s: got %v, want %v", label, got, want))
	}
}

// main self-validates the three examples documented in README.md.
// Any mismatch panics, which terminates the process with a non-zero status.
func main() {
	verify("nums=[2,7,11,15] target=9", []int{2, 7, 11, 15}, 9, []int{0, 1})
	verify("nums=[3,2,4]     target=6", []int{3, 2, 4}, 6, []int{1, 2})
	verify("nums=[3,3]       target=6", []int{3, 3}, 6, []int{0, 1})
	fmt.Println("all examples passed")
}
