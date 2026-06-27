class Solution(object):
    def spiralOrder(self, matrix):
        # We need to start moving one point distance minus from the edges after every iteration.
        total_elements = len(matrix) * len(matrix[0])

        lst = []

        row = len(matrix)
        col = len(matrix[0])
        distance_from_edges = 0

        while len(lst) < total_elements:
            top = distance_from_edges
            bottom = row - (distance_from_edges + 1)
            left = distance_from_edges
            right = col - (distance_from_edges + 1)

            # Now the logic to solve this problem is to traverse along these layers.
            # First we traverse from left to right at top position.
            # Then we traverse from top to bottom at the right position.
            # Then we traverse from right to left at the bottom position.
            # Then we finally move from bottom to top at the left position.
            # We don't move in bottom if bottom same as top.
            # We don't move right if left is same as right.

            # Move left to right
            for col_c in range(left, right + 1):
                lst.append(matrix[top][col_c])

            # Top + 1 since we did reach the end earlier.
            # Bottom + 1 since we already reach each edges.
            for row_r in range(top + 1, bottom + 1):
                lst.append(matrix[row_r][right])
            
            # This check ensures that we don't visit the same top or bottom node again.
            if top != bottom:
                for col_c in range(right - 1, left - 1, - 1):
                    lst.append(matrix[bottom][col_c])
            
            # This check ensures that we don't visit the same left or right edge again.
            if left != right:
                for row_r in range(bottom - 1, top, -1):
                    lst.append(matrix[row_r][left])
        
            distance_from_edges += 1

        return lst


"""
class Solution(object):
    def spiralOrder(self, matrix):
        # We need to start moving one point distance minus from the edges after every iteration.
        total_elements = len(matrix) * len(matrix[0])

        lst = []

        row = len(matrix)
        col = len(matrix[0])
        distance_from_edges = 0

        while distance_from_edges < (min(row, col) + 1) // 2:

            top = distance_from_edges
            bottom = row - 1 - distance_from_edges
            left = distance_from_edges
            right = col - 1 - distance_from_edges

            for c in range(left, right + 1):
                lst.append(matrix[top][c])

            for r in range(top + 1, bottom + 1):
                lst.append(matrix[r][right])

            if top != bottom:
                for c in range(right - 1, left - 1, -1):
                    lst.append(matrix[bottom][c])

            if left != right:
                for r in range(bottom - 1, top, -1):
                    lst.append(matrix[r][left])

            distance_from_edges += 1

        return lst
"""
