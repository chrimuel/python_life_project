import time

# Step 1: Define the maze
maze = ("\n"
        "xxxxxxxxxxx\n"
        "xo      x x\n"
        "x xxxxx x x\n"
        "x x   x x x\n"
        "x x x xxx x\n"
        "x   x x   x\n"
        "xxxxx xxx x\n"
        "x       x x\n"
        "x xxxxx x x\n"
        "x x   x   x\n"
        "x x x xxx x\n"
        "x x x     E\n"
        "xxxxxxxxxxx\n"
        )

# Configurable maze characters
wall_char = "x"
empty_char = " "
start_char = "o"
exit_char = "E"

# Step 2: Define the initial state (position and orientation)
def find_position(maze, char):
    lines = maze.splitlines()
    for i, row in enumerate(lines):
        if char in row:
            return (i, row.index(char))  # (row, col)
    return None

start_pos = find_position(maze, start_char)  # Starting position
exit_pos = find_position(maze, exit_char)    # Exit position
orientation = "north"                        # Initial orientation
visited = set()                              # Track visited positions and orientations

# Define symbols for orientations
orientation_symbols = {
    "north": "^",
    "east": ">",
    "south": "_",
    "west": "<"
}

# Step 3: Define a function to compute the next state
def get_next_state(maze, current_pos, orientation, visited):
    # Define moves and orientation order
    moves = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
    directions = ["north", "east", "south", "west"]
    
    # Dynamically calculate "right, straight, left, back"
    current_index = directions.index(orientation)
    direction_order = [
        directions[(current_index + 1) % 4],  # Right
        directions[current_index],           # Straight
        directions[(current_index - 1) % 4], # Left
        directions[(current_index + 2) % 4]  # Back
    ]
    
    lines = maze.splitlines()
    visited.add((current_pos, orientation))  # Mark current state as visited

    # Iterate directions in the calculated order
    for next_orientation in direction_order:
        next_move = moves[next_orientation]
        next_pos = (current_pos[0] + next_move[0], current_pos[1] + next_move[1])

        # Check if the next position is within bounds and not a wall
        if 0 <= next_pos[0] < len(lines) and 0 <= next_pos[1] < len(lines[1]) and lines[next_pos[0]][next_pos[1]] != wall_char:
            return next_pos, next_orientation

    return current_pos, orientation  # No valid move, remain in place

# Step 4: Define a function to print the maze with the current position
def print_maze_with_position(maze, current_pos, orientation):
    lines = maze.splitlines()
    maze_list = [list(row) for row in lines]
    symbol = orientation_symbols[orientation]
    row, col = current_pos
    maze_list[row][col] = symbol  # Replace current position with orientation symbol
    print("\n".join("".join(row) for row in maze_list))  # Print maze row by row
    print()  # Add a blank line for readability

# Step 5: Maze solving loop
visualize = True  # Toggle visualization
current_pos = start_pos
while current_pos != exit_pos:
    if visualize:
        time.sleep(0.3)  # Wait for 0.3 seconds between steps
        print_maze_with_position(maze, current_pos, orientation)
    print(f"At {current_pos}, facing {orientation}")
    if (current_pos, orientation) in visited:
        print("Loop detected, no solution.")
        break
    current_pos, orientation = get_next_state(maze, current_pos, orientation, visited)

if current_pos == exit_pos:
    if visualize:
        print_maze_with_position(maze, current_pos, orientation)
    print(f"Exit found at {current_pos}")
else:
    print("Exit not found.")