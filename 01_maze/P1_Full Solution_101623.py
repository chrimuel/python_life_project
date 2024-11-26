maze = ("xxxxxxxxxxx\n"
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
        "x x x     x\n"
        "xxxxxxxxxxx\n"
        )

# variable initializations        
height = maze.count('\n')
width = maze.find('\n')
start = maze.find('o')
wall = "x"
exitchar = "E"
orientation = "north"
# a tuple of tuples of (position, orientation)
seen = ()
# current_pos is the position in the 2D maze version
current_pos = (start//(width+1),((start-start//(width+1))%(width)))
# pos is the position in the 1D maze
pos = current_pos[0]*(width+1)+current_pos[1]
print(maze)
print("Current position:", current_pos)

# iterate until found the exit or reached a position/orientation already seen
while(maze[pos] != exitchar and (current_pos, orientation) not in seen):
    # show the steps taken    
    print("At", current_pos, "facing", orientation)
    # add current position/orientation to list of seen
    seen = seen + ((current_pos,orientation),)
    # cases organized by current orientations
    if orientation == "north" :
        # if cell immediately right available, turn and move right
        if maze[pos+1] != wall:
            orientation = "east"
            current_pos = (current_pos[0], current_pos[1]+1)
        # if cell immediately forward available, go there
        elif maze[pos-width-1] != wall:
            current_pos = (current_pos[0]-1, current_pos[1])
        # if cell immediately left available, turn and move left
        elif maze[pos-1] != wall:
            orientation = "west"
            current_pos = (current_pos[0], current_pos[1]-1)
        # can't move right, forward, or left
        # so turn around but don't move
        else:
            orientation = "south"
    elif orientation == "east":
        if maze[pos+width+1] != wall:
            orientation = "south"
            current_pos = (current_pos[0]+1, current_pos[1])
        elif maze[pos+1] != wall:
            current_pos = (current_pos[0], current_pos[1]+1)
        elif maze[pos-width-1] != wall:
            orientation = "north"
            current_pos = (current_pos[0]-1, current_pos[1])
        else:
            orientation = "west"
    elif orientation == "south":
        if maze[pos-1] != wall:
            orientation = "west"
            current_pos = (current_pos[0], current_pos[1]-1)
        elif maze[pos+width+1] != wall:
            current_pos = (current_pos[0]+1, current_pos[1])
        elif maze[pos+1] != wall:
            orientation = "east"
            current_pos = (current_pos[0], current_pos[1]+1)
        else:
            orientation = "north"
    elif orientation == "west":
        if maze[pos-width-1] != wall:
            orientation = "north"
            current_pos = (current_pos[0]-1, current_pos[1])
        elif maze[pos-1] != wall:
            current_pos = (current_pos[0], current_pos[1]-1)
        elif maze[pos+width+1] != wall:
            orientation = "south"
            current_pos = (current_pos[0]+1, current_pos[1])
        else:
            orientation = "east"
    pos = current_pos[0]*(width+1)+current_pos[1]
# check for why exited the loop
if (current_pos, orientation) not in seen:
    print("Exit at", current_pos)
else:
    print("Exit not found")        
#
#
# Copyright Manning Publications