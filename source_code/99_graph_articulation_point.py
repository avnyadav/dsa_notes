from typing import List, Dict


def dfs(
    node: int,
    parent: int,
    disc: List[int],
    low: List[int],
    visited: Dict[int, bool],
    adj_list: Dict[int, List[int]],
    ap: List[int],
    timer: int,
) -> None:
    visited[node] = True
    disc[node], low[node] = timer, timer
    timer += 1
    child: int = 0
    for neigh in adj_list[node]:
        if neigh == parent:
            continue
        if not visited[neigh]:
            dfs(neigh, node, disc, low, visited, adj_list, ap, timer)
            low[node] = min(low[node], low[neigh])

            # check Articulation Point
            if low[neigh] >= disc[node] and parent != -1:
                ap.append(node)

            child += 1
        else:
            low[node] = min(low[node], disc[neigh])

    if parent == -1 and child > 1:
        ap.insert(0, node)


def main() -> None:
    n: int = 5

    edges: List[List[int]] = [[0, 3], [3, 4], [0, 4], [0, 1], [1, 2]]
    adj_list: Dict[int, List[int]] = {i: list() for i in range(5)}

    for edge in edges:
        u, v = edge[0], edge[1]
        adj_list[u].append(v)
        adj_list[v].append(u)

    timer: int = 0
    disc: List[int] = []
    low: List[int] = []
    visited: Dict[int, bool] = dict()
    ap: List[int] = list()
    for i in range(n):
        disc.append(-1)
        low.append(-1)
        visited[i] = False

    for i in range(n):
        if not visited[i]:
            dfs(i, -1, disc, low, visited, adj_list, ap, timer)

    print(f"Articulation points are: {ap}")


if __name__ == "__main__":
    main()
