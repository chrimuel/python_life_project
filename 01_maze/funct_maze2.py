# Step 1: Define the maze
maze = """
*******
*o    *
*  ****
*    x*
*******
"""

# Step 2: Define the initial state (position and orientation)
def find_position(maze, char):
    lines = maze.splitlines()
    for i, row in enumerate(lines):
        if char in row:
            return (i, row.index(char))  # (row, col)
    return None

start_pos = find_position(maze, 'o')  # Starting position
exit_pos = find_position(maze, 'x')   # Exit position
orientation = "north"  # Initial orientation
visited = set()         # Track visited positions and orientations

# Step 3: Define a function to compute the next state
def get_next_state(maze, current_pos, orientation, visited):
    moves = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
    directions = ["north", "east", "south", "west"]
    lines = maze.splitlines()
    
    visited.add((current_pos, orientation))  # Mark current state as visited
    
    for _ in range(4):  # Check right, forward, left, then backward
        next_orientation = directions[(directions.index(orientation) + 1) % 4]
        next_move = moves[next_orientation]
        next_pos = (current_pos[0] + next_move[0], current_pos[1] + next_move[1])
        
        if lines[next_pos[0]][next_pos[1]] != "*":  # Check if the next cell is not a wall
            return next_pos, next_orientation
    
        orientation = next_orientation  # Rotate to the next orientation

    return current_pos, orientation  # No valid move, remain in place

# Step 4: Maze solving loop
current_pos = start_pos
while current_pos != exit_pos:
    print(f"At {current_pos}, facing {orientation}")
    if (current_pos, orientation) in visited:
        print("Loop detected, no solution.")
        break
    current_pos, orientation = get_next_state(maze, current_pos, orientation, visited)

if current_pos == exit_pos:
    print(f"Exit found at {current_pos}")
else:
    print("Exit not found.")