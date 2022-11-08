# 최단경로 알고리즘 다익스트라
import heapq

def dijkstra(graph, start):

    dist = {node: float('inf') for node in graph }
    dist[start] = 0
    queue = []
    heapq.heappush(queue, [dist[start], start])  # [[0, 'A']]

    while queue:
        cur_dist, cur_node = heapq.heappop(queue)

        # 현재노드의 거리에 대해
        # 거리데이터에 저장되있는 거리보다, 우선순위큐에서 꺼낸 거리가 더 길면 패스
        if dist[cur_node] < cur_dist:
            continue

        # items 함수는 Key와 Value의 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려준다.
        # dict_items([('B', 8), ('C', 1)])
        # adj_node : 인접노드(adjacent)
        # w : weight
        for adj_node, w in graph[cur_node].items():
            # 새 거리 = 현재노드까지의 거리 + 현재인접노드까지의 거리
            new_dist = cur_dist + w

            # 새 거리가 거리 데이터에 저장된 거리보다 짧으면, 갱신하고 우선순위큐에 추가
            if new_dist < dist[adj_node]:
                dist[adj_node] = new_dist
                heapq.heappush(queue, [new_dist, adj_node])
    return dist



