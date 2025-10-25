

graph = {}
n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"Enter node name: ")
    neighbours = input(f"Enter neighbours of {node} (space separated): ").split()
    graph[node] = neighbours
    


heuristic = {}
for node in graph:
    h = int(input(f"Enter heuristic value of {node}: "))
    heuristic[node] = h
    

start = input("Enter starting node: ")
goal = input("Enter goal node: ")
beam_width = int(input("Enter beam width: "))

visited = []
open_list = [start] 
 

print("\nThe Beam Search is:")

while open_list:

   # print("\nOpen List:", open_list)
    
    open_list.sort(key=lambda node: heuristic[node])
    
    

    open_list = open_list[:beam_width]
    
    
    node = open_list.pop(0)
    
   # print("Current Beam:", open_list + [node])
    
    if node not in visited:
        print(node, end=" ")
        
       # print("Heuristic:", heuristic[node])

        visited.append(node)
        
        if node == goal:
            break
        
        
        for neighbour in graph[node]:
            if neighbour not in visited and neighbour not in open_list:
                open_list.append(neighbour)
            


