import sys

def all_visited(visited):
    return all(visited)
# It uses the built-in all() function, which returns True if all elements in the iterable are True, otherwise, it returns False.

def tsp(visited,cost,current,path,n):
    global min_cost,ans
    if(all_visited(visited)):
        if(cost+graph[current][0] < min_cost):
            min_cost=cost+graph[current][0]
            ans=path+[0]
            return
    for i in range (n):
        if not visited[i] and i!=current:
            visited[i]=True
            tsp(visited,cost+graph[current][i],i,path+[i],n)
            visited[i]=False

if __name__=="__main__":
    # It is used to define the entry point of a Python script
    # This line checks if the script is being run as the main program
    n=int(input("Enter total no of vertex:"))
    graph=[]

    for i in range (n):
        row=[]
        for j in range (n):
            if(i!=j):
                dist=int(input(f"Enter cost from {i} to {j}:"))
                row.append(dist)
            else:
                row.append(0)
        graph.append(row)

    for i in range(n):
        for j in range(n):
            print(graph[i][j],end="\t")
        print()

    path=[] # For storing the shortest path
    visited=[False]*n  # Initializing visited array with all False values
    visited[0]=True  # Marking the first node as visited
    min_cost=sys.maxsize

    tsp(visited,0,0,[0],n)
    print("cost=",min_cost)
    print("path=",ans)

# OUTPUT
# Enter total no of vertex:4
# Enter cost from 0 to 1:10
# Enter cost from 0 to 2:15
# Enter cost from 0 to 3:20
# Enter cost from 1 to 0:10
# Enter cost from 1 to 2:35
# Enter cost from 1 to 3:25
# Enter cost from 2 to 0:15
# Enter cost from 2 to 1:35
# Enter cost from 2 to 3:30
# Enter cost from 3 to 0:20
# Enter cost from 3 to 1:25
# Enter cost from 3 to 2:30
# 0       10      15      20
# 10      0       35      25
# 15      35      0       30
# 20      25      30      0
# cost= 80
# path= [0, 1, 3, 2, 0]

    