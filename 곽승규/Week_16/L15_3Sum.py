class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 정렬하기
        nums.sort()
        answer = []
        
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) -1
            while left < right:
                sv = nums[i] + nums[left] + nums[right]
                print(i, left, right)
                if sv > 0:
                    right -= 1
                elif sv < 0:
                    left += 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])

                    # 중복제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer

