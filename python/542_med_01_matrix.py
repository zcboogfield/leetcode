"""
# 542. Find Shortest Distance
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

# Constraints
    m == mat.length
    n == mat[i].length
        #Always a rectangle

    1 <= m, n <= 104
    1 <= m * n <= 104
    mat[i][j] is either 0 or 1.
    There is at least one 0 in mat.
        # Everything gets a distance

    # Begin search at central node.
        # * Currently beginning @ (0,0)
    # Every node in the graph
        #  * It's a zero, record it's value in the graph.
            #  * Record it's value in the ans. 
            # A Node MUST be either be recorded in the ans  
            # the put in the 

    # PROMISES
        # * If we access a Node's value, it's neighbors are queue'd for seach.
        # ANS has three states:
            # Needs distance
            # Has distance
            # Is zero
            # NodeMap -> AnsMap
"""

class Solution:
    # I don't think this implementation garuntees O(N x M)
    def updateMatrix(self, mat):
        nx = len(mat);      #n
        my = len(mat[0]);   #m

        ans = [[None for y in range(my)] for x in range(nx)] #This needs to be created.
        queue = [(0,0)]

        def getNeighbors(node):
            x, y = node[0], node[1]
            potential_neighbors = ((x+1, y), (x-1, y), (x, y+1), (x, y-1))
            # Makes sure the node exists.
            print("POTENTIAL", potential_neighbors)
            neighbors = tuple(node for node in potential_neighbors if (node[0] > -1 and node[1] > -1 and node[0] < nx and node[1] < my))            
            print("NEIGHBORS", neighbors)
            return neighbors
        
        def getNodeMapVal(node):
            x, y = node[0], node[1]
            return mat[x][y]

        def updateAnsMap(node, val):
            x, y = node[0], node[1]
            ans[x][y] = val 
            print("ANS", ans, "QUEUE", queue, "VAL", val)
            return node

        # this runs recursively until we find a 0.
        def searchDepth(nodes, depth: int=1) -> int:
            searchResults = [{
                    "nodeMapVal": getNodeMapVal(node),
                    "neighbors": getNeighbors(node),
                    "checked": ans[node[0]][node[1]] is not None,
                    "node": node
            } for node in nodes]

            print("SEARCH", searchResults)
            unchecked = [result for result in searchResults if not result["checked"]]
            # add any unchecked 1s to the queue to make sure we find their depth.
            queue.extend(tuple(result["node"] for result in unchecked if result["nodeMapVal"] == 1))
            update = [updateAnsMap(node, 0 if result["nodeMapVal"] == 0 else True) for result in unchecked]

            # TODO Fix the loines below.
            if 0 in [result["nodeMapVal"] for result in searchResults]:
                # Add ANY unchecked neighbors
                unchecked_neighbors = (tuple(node 
                    for result in unchecked 
                    for node in result["neighbors"] 
                    if ans[node[0]][node[1]]
                ))
                queue.extend(unchecked_neighbors)
                return depth 
            # OPTIMIZATION: Might be able to add a check here for not 0 but did find a distance and use that distance.
            else:
                #filter for unchecked neighbors and ans[node[0]node[1] is not None
                # Assign values to ans, get DISTINCT neighbors
                # TODO FIX THIS
                return searchDepth(tuple(node for result in searchResult for node in searchResults), depth + 1) #spread through the neighbors to grab.)
            return


        while queue: 
            node = queue.pop()
            nodeVal = getNodeMapVal(node)
            print("QUEUE", queue, "NODE", node, "VAL", 0)
            updateAnsMap(node, 0 if nodeVal == 0 else searchDepth(getNeighbors(node), 1))
            neighbors = getNeighbors(node)
            print("NEIGHBORS", neighbors)
            queue.extend([node for node in getNeighbors(node) if ans[node[0]][node[1]] is None])
        return ans;

    #Tests would be really cool.
    #Setup a linter for this project.
run = Solution()

print(run.updateMatrix([[0,1,0],[1,0,0]]))
