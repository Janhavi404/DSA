global N
N=int(input("Enter the number of nodes:"))

def isSafe(graph, color):
   
    for i in range(N):
        for j in range(i + 1, N):
            if (graph[i][j] and color[j] == color[i]):
                return False
    return True

def graphColoring(graph, m, i, color):
   
    if (i == N): 
        if (isSafe(graph, color)): 
            printSolution(color)
            return True
        return False
 
    for j in range(1, m + 1):
        color[i] = j
 
        if (graphColoring(graph, m, i + 1, color)):
            return True
        color[i] = 0
    return False
 
def printSolution(color):
    print("Solution Exists:  Following are the assigned colors ")
    for i in range(N):
        if color[i]==1:
          c="Red"
        elif color[i]==2:
          c="Blue"
        elif color[i]==3:
          c="Green"
        print("Color assigned to node "+ str(i+1) + " is: "+ c)
 
if __name__ == '__main__':
   
    graph=[]
    for i in range(N):
      print("Enter the connections for node: " + str(i+1))
      a=list(map(int,input().split()))
      graph.append(a)

    m = 3
    color = [0 for i in range(N)] 
    if (not graphColoring(graph, m, 0, color)):
        print ("Solution does not exist")