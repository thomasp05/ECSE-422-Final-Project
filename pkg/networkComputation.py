#Thomas Philippon and Tristan Bouchard 
#Implementation of the Prim's algorithm 

import string
from .edge import Edge
from .networkConfig import GraphCandidate


alphabet_list = list(string.ascii_uppercase)

#Function for computing the minimun spanning tree with Prim's algorithm using edges reliability
def doPrimsReliability(city_list, edge_list): 
    mst_vertices_list = list()                            #empty list that will contain the edges of the MST
    other_vertices_list = edge_list.copy()                #Copy of the list containing all edges
    remaining_vertices = edge_list.copy()                 #Edges that will no be in the MST after performin prim's algorithm

    #sort the list of edges by their reliability (from most reliable to least reliable)
    other_vertices_list.sort(key=lambda x: x.reliability, reverse=True)

    #make a list of length #of vertices to be used when performing Prim's algorithm
    included_vertices = list()
    while(len(included_vertices) != len(city_list)): 
        included_vertices.append(0)                        #0 means the vertice is not in the MST, 1 means it is in the MSE


    #Perform Prim's algorithm
     
    #First pass for the first edge
    candidate = other_vertices_list[0]                     #get the most reliable edge and start from there
    
    candidateNumber = ord(candidate.vertice_1) - 65 -1     #convert letter to number (A=0, B=1, C=2 ...)
    included_vertices[candidateNumber] = 1                 #update the MST list of vertex
    candidateNumber = ord(candidate.vertice_2) - 65 -1     #convert letter to number (A=0, B=1, C=2 ...)
    included_vertices[candidateNumber] = 1                 #update the MST list of vertex

    mst_vertices_list.append(candidate)                    #append the vertex object to the MST set 
    included_vertices[candidateNumber] = 1                 #update the MST list of vertex
    total_reliability = candidate.reliability              #total reliability 
    total_cost = candidate.cost                            #total cost 
   
    remaining_vertices.remove(candidate)                   #remove candidate from the list of remaining edges
    index = 1                                              #index starts at because first pass was 0 
    
    while(len(mst_vertices_list) != len(city_list)-1): 

        candidate = other_vertices_list[index]

        #check if the any of the two verticies forming the edge "candidate" is not already in the MST (if both are we pass)
        vertice1 = ord(candidate.vertice_1) - 65 -1                                  #convert letter to number (A=1, B=2, C=3 ...)
        vertice2 = ord(candidate.vertice_2) - 65 -1                                  #convert letter to number (A=1, B=2, C=3 ...)
        if(included_vertices[vertice1] == 0 or included_vertices[vertice2] == 0): 
            mst_vertices_list.append(candidate)
            remaining_vertices.remove(candidate)
            included_vertices[vertice1] = 1                                          #the vertex 1 is now in the MST
            included_vertices[vertice2] = 1                                          #the vertex 2 is now in the MST
            total_reliability = total_reliability* candidate.reliability             #update total reliability 
            total_cost = total_cost + candidate.cost                                 #update total cost 
        index = index+1
    return mst_vertices_list, total_reliability, remaining_vertices, total_cost

#Function for computing the minimun spanning tree with Prim's algorithm using edges cost
def doPrimsCost(city_list, edge_list): 
    mst_vertices_list = list()                            #empty list that will contain the edges of the MST
    other_vertices_list = edge_list.copy()                #Copy of the list containing all edges
    remaining_vertices = edge_list.copy()                 #Edges that will no be in the MST after performin prim's algorithm

    #sort the list of edges by their reliability (from most reliable to least reliable)
    other_vertices_list.sort(key=lambda x: x.cost, reverse=False)

    #make a list of length #of vertices to be used when performing Prim's algorithm
    included_vertices = list()
    while(len(included_vertices) != len(city_list)): 
        included_vertices.append(0)                        #0 means the vertice is not in the MST, 1 means it is in the MSE


    #Perform Prim's algorithm
     
    #First pass for the first edge
    candidate = other_vertices_list[0]                     #get the most reliable edge and start from there
    
    candidateNumber = ord(candidate.vertice_1) - 65 -1     #convert letter to number (A=0, B=1, C=2 ...)
    included_vertices[candidateNumber] = 1                 #update the MST list of vertex
    candidateNumber = ord(candidate.vertice_2) - 65 -1     #convert letter to number (A=0, B=1, C=2 ...)
    included_vertices[candidateNumber] = 1                 #update the MST list of vertex

    mst_vertices_list.append(candidate)                    #append the vertex object to the MST set 
    included_vertices[candidateNumber] = 1                 #update the MST list of vertex
    total_cost = candidate.cost                            #total cost
    total_reliability = candidate.reliability              #total reliability 
   
    remaining_vertices.remove(candidate)                   #remove candidate from the list of remaining edges
    index = 1                                              #index starts at because first pass was 0 
    
    while(len(mst_vertices_list) != len(city_list)-1): 

        candidate = other_vertices_list[index]

        #check if the any of the two verticies forming the edge "candidate" is not already in the MST (if both are we pass)
        vertice1 = ord(candidate.vertice_1) - 65 -1                                  #convert letter to number (A=1, B=2, C=3 ...)
        vertice2 = ord(candidate.vertice_2) - 65 -1                                  #convert letter to number (A=1, B=2, C=3 ...)
        if(included_vertices[vertice1] == 0 or included_vertices[vertice2] == 0): 
            mst_vertices_list.append(candidate)
            remaining_vertices.remove(candidate)
            included_vertices[vertice1] = 1                                          #the vertex 1 is now in the MST
            included_vertices[vertice2] = 1                                          #the vertex 2 is now in the MST
            total_cost = total_cost + candidate.cost                                 #update total cost
            total_reliability = total_reliability*candidate.reliability              #update reliability 
        index = index+1
    return mst_vertices_list, total_reliability, remaining_vertices, total_cost



#Augmentation phase algorithm 
def computeAllTerminalReliability(edges_mst, remaining_vertices, city_list, Rtot, Rg): 
    
    edge_list = edges_mst.copy()    #Copy of the list containing the mst edges


    for candidate in remaining_vertices: 
        edge_list.append(candidate) 
        print(candidate)
        reliability, cost = computeReliability(edge_list, city_list)                        #call helper function to compute the all terminal reliability
        edge_list.remove(candidate)
    return
    


#helper function to compute the all terminal reliability of a network configuration
def computeReliability(edge_list, city_list): 

    #totalEdges = ((len(edge_list))*(len(edge_list)-1))/2
    totalEdges = 2 ** len(edge_list)
    print(totalEdges)
    reliability = 0
    cost = 0
    reliabilityResults = []
    for i in range(int(totalEdges)):
        
        currentCount = list('{0:0b}'.format(i))
        print(currentCount)

        # List of cities visited by current count
        citiesVisited = [0] * len(city_list)

        # Reliability of edges included in the visit
        currentEdgeReliability = [-1] * len(edge_list)
        # Here, create list that contains zeros of length city_list
        for j in range(len(edge_list)):
            if(j < len(currentCount)):
                if currentCount[j] == 1:
                    edge = edge_list[j]
                    city1 = ord(edge.vertice_1) - 65 -1
                    city2 = ord(edge.vertice_2) - 65 -1
                    citiesVisited[city1] = 1
                    citiesVisited[city2] = 1
                    currentEdgeReliability[i] = edge.reliability
                else:
                    currentEdgeReliability[i] = 1 - edge_list[j].reliability
            else:
                currentEdgeReliability[i] = 1 - edge_list[j].reliability
        
        # Verify if all cities visited
        print(citiesVisited) 
    return reliability, cost


# #helper function for finding cycles in graph using DFS
# def DFS()