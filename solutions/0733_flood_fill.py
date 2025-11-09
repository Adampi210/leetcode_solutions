# You are given an image represented by an m x n grid of integers image,
# where image[i][j] represents the pixel value of the image.
# You are also given three integers sr, sc, and color.
# Your task is to perform a flood fill on the image starting
# from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly
# adjacent (pixels that share a side with the original pixel,
# either horizontally or vertically) and shares the same color
# as the starting pixel.
# Keep repeating this process by checking neighboring
# pixels of the updated pixels and modifying their color
# if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent
# pixels of the original color to update.
# Return the modified image after performing the flood fill.

# NOTE: This uses a pre-order traversal approach, where the current pixel is processed
# before its neighbors.
# Recursive solution
class SolutionRecursive(object):
    def floodFill(self, image, sr, sc, color):
        # First base case condition,
        # if the current pixel is already the target color
        # return the image as is (no changes needed)
        if image[sr][sc] == color:
            return image
        # Store the original pixel value to identify which pixels to change
        pixel_val = image[sr][sc]
        # Change the color of the current pixel
        image[sr][sc] = color
        # First get all 4 neighboring pixels (up, down, left, right)
        neighbors = [(sr + i, sc) for i in (-1, 1)] + [(sr, sc + j) for j in (-1, 1)]
        # Filter neighbors to include only those within bounds and with the same original color
        boundary_idx_y = len(image) - 1
        boundary_idx_x = len(image[0]) - 1
        neighbors_same_color = [neighbor for neighbor in neighbors if neighbor[0] >= 0 and neighbor[1] >= 0 and neighbor[0] <= boundary_idx_y and neighbor[1] <= boundary_idx_x and image[neighbor[0]][neighbor[1]] == pixel_val]
        # Recursively call floodFill on each valid neighboring pixel
        for (n_sr, n_sc) in neighbors_same_color:
            self.floodFill(image, n_sr, n_sc, color)
        # Finally return the modified image
        return image

# Will need a queue for iterative approach
from collections import deque

# Iterative solution
class SolutionIterative(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """

        # Get the original pixel value
        pixel_val = image[sr][sc]
        # If the original pixel value is the same as the target color,
        # return the image as is (since the pixels are already the target color)
        if pixel_val == color:
            return image
        # Get the boundaries of the image
        len_0, len_1 = len(image) - 1, len(image[0]) - 1
        # Initialize a queue for BFS
        pixel_queue = deque()
        # Start with the given pixel
        pixel_queue.append((sr, sc))
        # Process the queue until it's empty
        while len(pixel_queue) > 0:
            # Get the current pixel coordinates
            curr_sr, curr_sc = pixel_queue.popleft()
            # Change the color of the current pixel
            image[curr_sr][curr_sc] = color
            # Get all 4 neighboring pixels (up, down, left, right)
            neighbors = [
                (curr_sr - 1, curr_sc),
                (curr_sr + 1, curr_sc),
                (curr_sr, curr_sc - 1),
                (curr_sr, curr_sc + 1),
            ]
            # Check each neighbor
            for n_sr, n_sc in neighbors:
                # Check if the neighbor is within bounds
                if n_sr < 0 or n_sc < 0 or n_sr > len_0 or n_sc > len_1:
                    # If not, skip to the next neighbor
                    continue
                # If the neighbor is within bounds, 
                # check if it has the same original pixel value
                else:
                    # If it does, add it to the queue for processing
                    if image[n_sr][n_sc] == pixel_val:
                        pixel_queue.append((n_sr, n_sc))
        # Finally return the modified image
        return image
