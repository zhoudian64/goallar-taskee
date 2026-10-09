package twosum_test

import (
	"maps"
	"testing"

	"github.com/zhoudian64/goallar-taskee/twosum"
)

// TestTwoSum asserts the returned indices as a set, so any order is accepted.
func TestTwoSum(t *testing.T) {
	t.Parallel()

	tests := []struct {
		name   string
		nums   []int
		target int
		want   [2]int
	}{
		{
			name:   "example 1",
			nums:   []int{2, 7, 11, 15},
			target: 9,
			want:   [2]int{0, 1},
		},
		{
			name:   "example 2",
			nums:   []int{3, 2, 4},
			target: 6,
			want:   [2]int{1, 2},
		},
		{
			name:   "example 3 duplicates",
			nums:   []int{3, 3},
			target: 6,
			want:   [2]int{0, 1},
		},
		{
			name:   "negative values",
			nums:   []int{-1, -2, -3, -4, -5},
			target: -8,
			want:   [2]int{2, 4},
		},
		{
			name:   "large magnitude",
			nums:   []int{1000000000, 999999999, -1000000000},
			target: 1999999999,
			want:   [2]int{0, 1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			t.Parallel()

			got := twosum.TwoSum(tt.nums, tt.target)

			if len(got) != 2 {
				t.Fatalf("TwoSum(%v, %d) = %v, want exactly 2 indices", tt.nums, tt.target, got)
			}
			if got[0] == got[1] {
				t.Errorf("TwoSum(%v, %d) = %v reuses the same element twice", tt.nums, tt.target, got)
			}

			// Compare indices as sets so [0,1] and [1,0] both pass.
			wantSet := map[int]struct{}{tt.want[0]: {}, tt.want[1]: {}}
			gotSet := make(map[int]struct{}, len(got))
			for _, idx := range got {
				if idx < 0 || idx >= len(tt.nums) {
					t.Fatalf("TwoSum(%v, %d) = %v returns out-of-range index %d", tt.nums, tt.target, got, idx)
				}
				gotSet[idx] = struct{}{}
			}
			if !maps.Equal(gotSet, wantSet) {
				t.Errorf("TwoSum(%v, %d) = %v, want indices set %v (any order)", tt.nums, tt.target, got, wantSet)
			}

			// Independently confirm the returned pair really sums to target.
			if sum := tt.nums[got[0]] + tt.nums[got[1]]; sum != tt.target {
				t.Errorf("TwoSum(%v, %d) = %v sums to %d, want %d", tt.nums, tt.target, got, sum, tt.target)
			}
		})
	}
}
