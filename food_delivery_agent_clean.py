from collections import deque
import heapq

graph = {
    "Restaurant": {"A": 2, "B": 4},
    "A": {"Restaurant": 2, "C": 3, "D": 7},
    "B": {"Restaurant": 4, "D": 2},
    "C": {"A": 3, "Customer": 5},
    "D": {"A": 7, "B": 2, "Customer": 3},
    "Customer": {"C": 5, "D": 3}
}

heuristic = {
    "Restaurant": 7,
    "A": 6,
    "B": 4,
    "C": 4,
    "D": 2,
    "Customer": 0
}


# BFS Algorithm
def bfs(start, goal):
    queue = deque([[start]])
    visited = {start}

    while queue:
        path = queue.popleft()
        place = path[-1]

        if place == goal:
            return path

        for neighbor in graph[place]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


# DFS Algorithm
def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        place = path[-1]

        if place == goal:
            return path

        if place not in visited:
            visited.add(place)

            for neighbor in graph[place]:
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None


# A* Algorithm
def a_star(start, goal):
    queue = [(heuristic[start], 0, start, [start])]
    best_distance = {start: 0}

    while queue:
        estimate, distance, place, path = heapq.heappop(queue)

        if place == goal:
            return path, distance

        if distance > best_distance.get(place, float("inf")):
            continue

        for neighbor, cost in graph[place].items():
            new_distance = distance + cost

            if new_distance < best_distance.get(
                neighbor, float("inf")
            ):
                best_distance[neighbor] = new_distance

                total = new_distance + heuristic[neighbor]

                heapq.heappush(
                    queue,
                    (total, new_distance, neighbor,
                     path + [neighbor])
                )

    return None, float("inf")


# Priority Queue
def schedule_orders(orders):
    heapq.heapify(orders)

    print("\nDelivery Order:")

    while orders:
        priority, customer = heapq.heappop(orders)
        print(customer, "- Priority:", priority)


# Main Program
start = "Restaurant"
goal = "Customer"

print("BFS Route:", " -> ".join(bfs(start, goal)))
print("DFS Route:", " -> ".join(dfs(start, goal)))

path, distance = a_star(start, goal)

print("A* Route:", " -> ".join(path))
print("Shortest Distance:", distance, "km")

orders = [
    (3, "Customer C"),
    (1, "Customer A"),
    (2, "Customer B")
]

schedule_orders(orders)
