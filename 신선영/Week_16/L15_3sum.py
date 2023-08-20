class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []    # 정답 저장할 배열
        nums.sort()

        for i in range(len(nums) - 2):  # 포인터 있어야되니까 2개 빼고
            cur = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total == 0:
                    if [nums[i], nums[l], nums[r]] not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                elif total > 0:
                    r -= 1

                elif total < 0:
                    l += 1
    
        return ans
