class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        # 정렬
        nums.sort()

        for i, a in enumerate(nums) : 
            # 이전 숫자와 같으면 중복된 조합을 피하기 위해 현재 숫자 건너뜀
            if i > 0 and a == nums[i - 1] : 
                continue

            l, r = i + 1, len(nums) - 1
            while l < r : 
                threeSum = a + nums[l] + nums[r]
               
                # 0보다 큰 경우 r을 왼쪽으로
                if threeSum > 0 : 
                    r -= 1
                # 0보다 작은 경우 l을 오른쪽으로
                elif threeSum < 0 : 
                    l += 1
                else : 
                    ans.append([a, nums[l], nums[r]])
                    l += 1
                    
                    # 중복된 조합 값들 건너뜀
                    while nums[l] == nums[l - 1] and l < r : 
                        l += 1
                    
        return ans