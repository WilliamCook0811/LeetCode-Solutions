class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)

        # 0 <= i < j < n
        ans = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    temp = nums[j] - nums[i]
                    if temp > ans:
                        print(ans)
                        ans = temp
                        print(ans)

        return(ans)