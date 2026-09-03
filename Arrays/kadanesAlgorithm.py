class Solution:

    def maxSubArray(self, nums):

        # Start with the first element
        # This is the maximum sum ending at the first position
        current_sum = nums[0]

        # Store the maximum sum found so far
        max_sum = nums[0]

        # Start from the second element
        for i in range(1, len(nums)):

            # Choose between:
            # 1. Starting a new subarray with nums[i]
            # 2. Continuing the previous subarray
            current_sum = max(nums[i], current_sum + nums[i])

            # Update max_sum if current_sum is larger
            max_sum = max(max_sum, current_sum)

        # Return the maximum subarray sum
        return max_sum


# Input array
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Create an object of Solution and call the method
print(Solution().maxSubArray(nums))