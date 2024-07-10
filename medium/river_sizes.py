def riverSizes(matrix):
    #   Algorytm wyszukiwania w głąb DFS
    def dfs(i, j):
        stack = [(i, j)]
        river_size = 0

        while stack:
            x, y = stack.pop()
            if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] != 1:
                continue
            river_size += 1
            matrix[x][y] = -1  # Mark as visited
            # Add all neighboring cells to the stack
            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

        return river_size

    sizes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                size = dfs(i, j)
                if size > 0:
                    sizes.append(size)

    return sizes


matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

x = riverSizes(matrix)
print(x)
