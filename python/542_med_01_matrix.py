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
# Runtime: 885 ms, faster than 80.33% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17.5 MB, less than 34.24% of Python3 online submissions for 01 Matrix.
class Solution:
    #Current leet_code status: Time Limit Exceeded :upside_down_face:
    # Apparently got through
    def updateMatrix(self, mat):
        NX = len(mat);      #n
        MY = len(mat[0]);   #m

        checked = set()
        queue = []

        # print("MAT", mat)
        # print("N/M", NX,MY)

        for x in range(0, NX):
            for y in range(0, MY):
                if mat[x][y] == 0:
                    checked.add((x,y))
                    queue.append((x,y))

        while queue: 
            x,y = queue.pop(0)
            print("NODE", x,y)
            neighbors = [(nX, nY) for nX, nY in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)] 
                         if (nX > -1 and nY > -1 and nX < NX and nY < MY and (nX,nY) not in checked)
             ]
            # print("NEIGHBORS", neighbors)
            for node in neighbors:
                # print("NEW", node[0], node[1])
                mat[node[0]][node[1]] = mat[x][y] + 1
                checked.add(node)
                queue.append(node)
        return mat;
run = Solution()

#TESTS
#Tests would be really cool.
    # SearchDepth should only run for amount of 1s x Depth to zero.
    # Each position is only "searched" once.

# Setup a linter for this project.
# Baby test just to confirm it runs.
# # # print(run.updateMatrix([[0,1,0],[1,0,0]]))
# Output: [[0,1,0],[1,0,0]]

### print(run.updateMatrix([[0,0,0],[0,1,0],[0,0,0]]))
#Output: [[0,0,0],[0,1,0],[0,0,0]]

## print(run.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
#Output: [[0,0,0],[0,1,0],[1,2,1]]

# print(run.updateMatrix([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]) ==  [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])

# Input
print(run.updateMatrix([[1,1,0,1,1,1,1,1,1,1],[1,1,0,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,1,1,0],[1,1,1,1,1,1,0,0,1,0],[1,0,0,1,1,1,0,1,0,1],[0,0,1,0,0,1,1,0,0,1],[0,1,0,1,1,1,1,1,1,1],[1,0,0,1,1,0,0,0,0,0],[0,0,1,1,1,1,0,1,1,1],[1,1,0,0,1,0,1,0,1,1]]))
# Output
#[[2,1,0,1,2,2,2,3,4,2],[3,1,0,1,1,1,1,2,2,1],[3,2,1,1,0,0,0,1,1,0],[4,1,1,2,1,1,0,0,1,0],[1,0,0,1,1,1,0,1,0,1],[0,0,1,0,0,1,1,0,0,1],[0,1,0,1,1,1,1,1,1,1],[1,0,0,1,1,0,0,0,0,0],[0,0,1,1,2,1,0,1,1,1],[1,1,0,0,1,0,1,0,1,2]]
# Expected
#[[2,1,0,1,2,2,2,3,3,2],[2,1,0,1,1,1,1,2,2,1],[3,2,1,1,0,0,0,1,1,0],[2,1,1,2,1,1,0,0,1,0],[1,0,0,1,1,1,0,1,0,1],[0,0,1,0,0,1,1,0,0,1],[0,1,0,1,1,1,1,1,1,1],[1,0,0,1,1,0,0,0,0,0],[0,0,1,1,2,1,0,1,1,1],[1,1,0,0,1,0,1,0,1,2]]
