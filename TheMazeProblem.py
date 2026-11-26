def solve(maze, x, y, path):

    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False

    if maze[x][y] == 1:
        return False

    if maze[x][y] == 2:
        return False

    if maze[x][y] == 'E':
        path.append((x,y))
        return True


    maze[x][y] = 2
    path.append((x,y))

    if (solve(maze, x+1, y, path) or
        solve(maze, x-1, y, path) or
        solve(maze, x, y+1, path) or
        solve(maze, x, y-1, path)):
        return True

    path.pop()
    return False


maze = [
    ['S', 0, 1, 0, 0, 0, 1],
    [1,   0, 1, 0, 1, 0, 1],
    [0,   0, 0, 0, 1, 0, 0],
    [0,   1, 1, 0, 0, 0, 1],
    [1,   0, 0, 0, 1, 0, 0],
    [0,   0, 1, 0, 0, 1, 0],
    [1,   0, 0, 0, 0, 1, 'E']
]
path = []
if solve(maze, 0, 0, path):
    print("there is a path:")
    print(path)

else:
    print("there is no path")
