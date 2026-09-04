class Solution:
    def findMissingRepeatingNumbers(self, nums):
        
        n = len(nums)

        # Count frequency of each number
        freq = [0] * (n + 1)

        for num in nums:
            freq[num] += 1

        repeating = -1
        missing = -1

        # Check numbers from 1 to n
        for i in range(1, n + 1):
            if freq[i] == 2:
                repeating = i
            elif freq[i] == 0:
                missing = i

        return [repeating, missing]
nums = [3, 1, 2, 5, 3]

obj = Solution()
print(obj.findMissingRepeatingNumbers(nums))    