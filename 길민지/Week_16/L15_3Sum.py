from itertools import combinations
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combi = combinations(print(list(range(len(nums)))), 3)

        # combi 돌면서 nums[i] + nums[j] + nums[k] == 0 되는거 찾기 