import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total_vertices = len(points)

        self.pq = []

        # MST set to monitor if the node is visited or not.
        visited_vertex = [False for i in range(total_vertices)]

        temp_lst = points[0]
        temp_lst.append(0)

        # Initialize the starting point of Prim's algorithm
        self.pq.append((0, temp_lst))

        heapify(self.pq)
        
        total_weight = 0
        total_counted = 0

        # We need to only continue till all the points are counted.
        while total_counted < len(points):

            # Here lst will have point x, y and the index
            wgt, lst = heappop(self.pq)

            if visited_vertex[lst[2]]:
                continue

            visited_vertex[lst[2]] = True
            total_weight += wgt
            total_counted +=1

            """
                Here, to solve this problem we need to create an MST.
                Now we maintain a Priority Queue to insert only those elements,
                which we did not visit.
                We then look for all the points from this point and add distances as its weight.
                Now we need to look for the points cause we don't want to miss any cases.
            """

            for each_point in range(len(points)):
                temp_wgt = self.get_dis([lst[0], lst[1]], points[each_point])

                min_wgt = temp_wgt
                idx = each_point

                temp_lst = points[idx]
                temp_lst.append(idx)

                heappush(self.pq, (min_wgt, temp_lst))
            
        return total_weight
    

    def get_dis(self, point_a, point_b):
        return abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1])
