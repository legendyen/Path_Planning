import matplotlib.pyplot as plt
import numpy as np

# 0 = free, 1 = obstacle
grid_map1 = np.array([
    [0,0,0,0,0],
    [1,0,0,0,0],
    [0,0,1,0,1],
    [0,1,1,0,1],
    [0,0,0,0,0]
])

def get_neighbors(current):
    r, c = current
    neighbors = []
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < grid_map1.shape[0] and 0 <= nc < grid_map1.shape[1]:
            if grid_map1[nr, nc] == 0:  # walkable
                neighbors.append((nr, nc))
    return neighbors


def bfs(start, goal):
    queue = [start]
    visited = {start}
    parent = {}

    # --- Keep one figure/axis for the whole animation ---
    plt.ion()
    fig, ax = plt.subplots()
    ax.imshow(grid_map1, cmap='viridis')
    ax.plot(start[1], start[0], 'go', markersize=10, label="Start")
    ax.plot(goal[1], goal[0], 'rx', markersize=10, label="Goal")
    # ax.legend()
    plt.show(block=False)
    # ----------------------------------------------------

    while queue:
        current = queue.pop(0)

        # Mark current as visited
        ax.plot(current[1], current[0], 'g.', markersize=6)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.0001)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

                # Mark neighbor as discovered (red dot)
                ax.plot(neighbor[1], neighbor[0], 'r.', markersize=4)
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(0.0001)

    # Reconstruct and draw path
    path = [goal]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()

    rr, cc = zip(*path)
    ax.plot(cc, rr, '-y', linewidth=2)

    plt.ioff()
    plt.show()
    return path

# Example
start = (0, 0)
goal = (4, 4)
path = bfs(start, goal)
print("Path:", path)