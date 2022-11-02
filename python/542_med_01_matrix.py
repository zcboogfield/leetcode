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
        # ANS[x][y] has three states:
            # None: Has not been checked.
            # True: Currently in the Queue
            # int: Distance 
            # NodeMap -> AnsMap
"""
# Didn't work.
class Solution:
    #Current leet_code status: Time Limit Exceeded :upside_down_face:
    # Apparently got through
    def updateMatrix(self, mat):
        print("MAP", mat)
        nx = len(mat);      #n
        my = len(mat[0]);   #m

        ans = [[None for y in range(my)] for x in range(nx)] 
        # Might be able to optimize  this by starting at center.
        queue = [(0,0)]

        # This is REEEEEALLY handy.
        def getNeighbors(node):
            x, y = node[0], node[1]
            # Makes sure the node exists.
            return tuple(node for node in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)) 
                              if (node[0] > -1 and node[1] > -1 and node[0] < nx and node[1] < my))
        
        #This function call is probablly expensive and can be replaced.
        def getNodeMapVal(node):
            x, y = node[0], node[1]
            return mat[x][y]

        # This updates the AnsMap
        def updateAnsMap(node, val):
            x, y = node[0], node[1]
            print("ANS_CHANGE", ans, "NODE", (x,y), "VAL", val)
            ans[x][y] = val 
            # Checks every state change.
            print("NEW_ANS   ", ans, "NODE", (x,y), "VAL", val, "\n")
            return node

        # this runs recursively until we find a 0.
        def searchDepth(nodes, depth: int=1) -> int:
            searchResults = [{
                    "node": node,
                    "nodeMapVal": getNodeMapVal(node),
                    "neighbors": getNeighbors(node),
                    "answered": type(ans[node[0]][node[1]]) is int,
            } for node in nodes]

            print("SEARCH_RESULTS_DEPTH", depth, searchResults)
            unanswered = [result for result in searchResults if not result["answered"]]
            print("UNanswered", unanswered)
            queue.extend(tuple(result["node"] for result in unanswered if result["nodeMapVal"] == 1))
            update = [updateAnsMap(result["node"], 0 if result["nodeMapVal"] == 0 else True) for result in unanswered]

            # TODO This current implementation will not stop until it finds the depth with an actual zero.
            # There might be an OPTIMIZATION for using a depth that already has a distance.

            # Find the smallest ints
            distances = [ans[result["node"][0]][result["node"][1]] for result in searchResults 
                         if type(ans[result["node"][0]][result["node"][1]]) == int
            ]
            print("DISTANCES", distances)
            if distances:
                min_depth = min(distances)
                # Add ANY unchecked neighbors
                unchecked_neighbors = tuple(node 
                    for result in unanswered 
                    for node in result["neighbors"] 
                    if ans[node[0]][node[1]] is None
                )
                queue.extend(unchecked_neighbors)
                # True means they've been added to the queue.
                update = [updateAnsMap(node, True) for node in unchecked_neighbors]
                print("DEPTH_FOUND", depth, "MIN_DEPTH", min_depth)
                return depth + min_depth
            else:
                return searchDepth(tuple(node for result in searchResults for node in result["neighbors"]), depth + 1) #

        while queue: 
            node = queue.pop(0)
            nodeVal = getNodeMapVal(node)
            print("QUEUE_POP", "NODE", node, "VAL", nodeVal, "QUEUE", queue, "\n")
            if nodeVal == 1 and ans[node[0]][node[1]] is None:
                #Sets the current distance needed node to "checked" so it is no longer added to the queue.
                updateAnsMap(node, True)
            updateAnsMap(node, 0 if nodeVal == 0 else searchDepth(getNeighbors(node), 1))
            unchecked = [node for node in getNeighbors(node) if ans[node[0]][node[1]] is None]
            queue.extend(unchecked)
            # Once we put something in the queue, we mark it true as it will be checked.
            update = [updateAnsMap(node, True) for node in unchecked]
        return ans;

run = Solution()

#TESTS
#Tests would be really cool.
    # SearchDepth should only run for amount of 1s x Depth to zero.
    # Each position is only "searched" once.

# Setup a linter for this project.
# Baby test just to confirm it runs.
# # print(run.updateMatrix([[0,1,0],[1,0,0]]))
# Output: [[0,1,0],[1,0,0]]

##print(run.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
#Output: [[0,0,0],[0,1,0],[0,0,0]]

#print(run.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
#Output: [[0,0,0],[0,1,0],[1,2,1]]

print(run.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]) ==  [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
