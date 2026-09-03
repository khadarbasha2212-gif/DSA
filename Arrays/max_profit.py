class Solution:

    def stockBuySell(self, arr, n):

        # Store the total profit
        profit = 0

        # Start from the second day
        for i in range(1, n):

            # If today's price is higher than yesterday's price,
            # we can make a profit by buying yesterday and selling today
            if arr[i] > arr[i - 1]:

                # Add today's profit to the total profit
                profit = profit + (arr[i] - arr[i - 1])

        # Return the maximum profit
        return profit
arr= [7, 1, 5, 3, 6, 4]
n = len(arr)

print(Solution().stockBuySell(arr, n))    