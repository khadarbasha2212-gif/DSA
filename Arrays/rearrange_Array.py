class Solution:

    def rearrangeArray(self, nums):

        # Create an empty array to store the result
        result = [0] * len(nums)

        # Index for positive numbers
        positive_index = 0

        # Index for negative numbers
        negative_index = 1

        # Go through every number in nums
        for num in nums:

            # If the number is positive
            if num > 0:

                # Put it at the next positive position
                result[positive_index] = num

                # Move to the next positive position
                positive_index += 2

            # If the number is negative
            else:

                # Put it at the next negative position
                result[negative_index] = num

                # Move to the next negative position
                negative_index += 2

        # Return the rearranged array
        return result
nums = [3, 1, -2, -5, 2, -4]

print(Solution().rearrangeArray(nums))    