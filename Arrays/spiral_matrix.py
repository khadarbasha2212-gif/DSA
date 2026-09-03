class Solution:

    def spiralOrder(self, matrix):

        # Create an empty list to store the answer
        result = []

        # Define four boundaries
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        # Continue while there are rows and columns remaining
        while top <= bottom and left <= right:

            # 1. Traverse from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])

            # Move the top boundary down
            top += 1

            # 2. Traverse from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])

            # Move the right boundary left
            right -= 1

            # 3. Traverse from right to left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])

                # Move the bottom boundary up
                bottom -= 1

            # 4. Traverse from bottom to top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])

                # Move the left boundary right
                left += 1

        # Return the elements in spiral order
        return result

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(Solution().spiralOrder(matrix))