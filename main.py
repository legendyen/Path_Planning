graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'
goal = 'F'

queue = [start]
visited = set(start)

while queue:
    current = queue.pop(0)
    print(f"Visiting: {current}")
    # if current == goal:
    #     print(f"Goal {goal} found!")
    #     break
    for neighbor in graph[current]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

