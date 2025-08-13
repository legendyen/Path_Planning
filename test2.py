import matplotlib.pyplot as plt
import numpy as np

# L-shaped obstacle grid (0 = free, 1 = obstacle)
grid_map2 = np.array([
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
])

def get_neighbors(current, grid_map):
    r, c = current
    neighbors = []
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < grid_map.shape[0] and 0 <= nc < grid_map.shape[1]:
            if grid_map[nr, nc] == 0:
                neighbors.append((nr, nc))
    return neighbors

def bfs(start, goal, grid_map):
    queue = [start]
    visited = {start}
    parent = {}

    plt.ion()
    fig, ax = plt.subplots()
    ax.imshow(grid_map, cmap='viridis')
    ax.plot(start[1], start[0], 'go', markersize=10, label="Start")
    ax.plot(goal[1], goal[0], 'rx', markersize=10, label="Goal")
    ax.legend()
    plt.show(block=False)

    while queue:
        current = queue.pop(0)
        ax.plot(current[1], current[0], 'g.', markersize=6)
        fig.canvas.draw()
        fig.canvas.flush_events()
        plt.pause(0.0001)

        for neighbor in get_neighbors(current, grid_map):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
                ax.plot(neighbor[1], neighbor[0], 'r.', markersize=4)
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(0.0001)
    
    # Check if a path was found before attempting to reconstruct it
    if goal in parent:
        path = [goal]
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
        rr, cc = zip(*path)
        ax.plot(cc, rr, '-y', linewidth=2)
        print("Path found:", path)
    else:
        print("No path found to the goal. The algorithm explored all reachable nodes.")

    plt.ioff()
    plt.show()

# Example using your original coordinates
start = (18, 1)
goal = (1, 18)
bfs(start, goal, grid_map2)