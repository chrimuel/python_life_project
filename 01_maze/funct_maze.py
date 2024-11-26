def solve_maze(maze):
    # Parse maze into lines
    lines = maze.splitlines()
    height, width = len(lines), len(lines[0])
    
    # Find start and exit
    start = [(i, j) for i, row in enumerate(lines) for j, char in enumerate(row) if char == 'o'][0]
    end = [(i, j) for i, row in enumerate(lines) for j, char in enumerate(row) if char == 'x'][0]
    
    # Movement: right-hand rule (clockwise order)
    moves = {"north": (-1, 0), "east": (0, 1), "south": (1, 0), "west": (0, -1)}
    directions = ["north", "east", "south", "west"]
    
    # Initialize position and direction
    pos, orientation = start, "north"
    visited = set()
    
    while pos != end:
        visited.add((pos, orientation))
        for _ in range(4):  # Check right, forward, left, then backward
            next_orientation = directions[(directions.index(orientation) + 1) % 4]
            next_pos = (pos[0] + moves[next_orientation][0], pos[1] + moves[next_orientation][1])
            if lines[next_pos[0]][next_pos[1]] != "*":
                pos, orientation = next_pos, next_orientation
                break
            orientation = next_orientation
        else:  # If all directions are blocked
            break
        if (pos, orientation) in visited:
            return "Loop detected, no solution."
    
    return f"Exit found at {pos}" if pos == end else "Exit not found."


# Test the function
maze = """
*******
*o    *
*  ****
*    x*
*******
"""

print(solve_maze(maze))