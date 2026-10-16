// LeetCode Two Sum - C++17 solution with self-validation.
//
// Build & run:
//   g++ -std=c++17 -O2 solutions/two_sum.cpp -o /tmp/ts && /tmp/ts
// Exits with status 0 when every example passes, non-zero otherwise.

#include <cstdlib>
#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(std::vector<int> nums, int target) {
    // Hash table mapping value -> index. Single pass, O(n) time, O(n) space.
    std::unordered_map<int, int> seen;
    seen.reserve(nums.size());
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        const int need = target - nums[i];
        auto it = seen.find(need);
        if (it != seen.end()) {
            // The partner was already used once, so nums[i] is never reused.
            return std::vector<int>{it->second, i};
        }
        seen[nums[i]] = i;
    }
    return {};  // unreachable: exactly one answer exists
}

namespace {

bool check(const std::vector<int>& got, const std::vector<int>& want) {
    return got.size() == 2 && want.size() == 2 && got[0] == want[0] && got[1] == want[1];
}

bool run_case(const char* label, const std::vector<int>& nums, int target,
              const std::vector<int>& want) {
    const std::vector<int> got = twoSum(nums, target);
    const bool ok = check(got, want);
    std::cout << label << " -> [" << got[0] << ", " << got[1] << "] expected ["
              << want[0] << ", " << want[1] << "] " << (ok ? "OK" : "FAIL") << '\n';
    return ok;
}

}  // namespace

int main() {
    bool all_ok = true;
    all_ok &= run_case("nums=[2,7,11,15] target=9", {2, 7, 11, 15}, 9, {0, 1});
    all_ok &= run_case("nums=[3,2,4]     target=6", {3, 2, 4}, 6, {1, 2});
    all_ok &= run_case("nums=[3,3]       target=6", {3, 3}, 6, {0, 1});
    return all_ok ? EXIT_SUCCESS : EXIT_FAILURE;
}
