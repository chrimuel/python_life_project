# Define the maze as a string with newlines for row separation
maze_str = """
*********
*o      * 
*   x**** 
*       *
*********
"""

# Print the maze
# print("Maze (of string):")
# print(maze_str)

# Convert the string into a list of rows, removing empty lines
def linefunc(maze_str):
    return [line for line in maze_str.splitlines() if line]

maze_list = linefunc(maze_str)

# Print the maze from the list
print("Maze (of list):")
for row in maze_list:
    print(row)