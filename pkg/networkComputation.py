#Thomas Philippon and Tristan Bouchard 
#Implementation of the Prim's algorithm 

import string
import sys
from .edge import Edge
from .networkConfig import GraphCandidate
from .graph import Graph


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
    
    candidateNumber = ord(candidate.vertice_1) - 65    #convert letter to number (A=0, B=1, C=2 ...)
    included_vertices[candidateNumber] = 1             #update the MST list of vertex
    candidateNumber = ord(candidate.vertice_2) - 65    #convert letter to number (A=0, B=1, C=2 ...)
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
        vertice1 = ord(candidate.vertice_1) - 65                                  #convert letter to number (A=1, B=2, C=3 ...)
        vertice2 = ord(candidate.vertice_2) - 65                                  #convert letter to number (A=1, B=2, C=3 ...)
        if(included_vertices[vertice1] == 0 or included_vertices[vertice2] == 0): 
            mst_vertices_list.append(candidate)
            remaining_vertices.remove(candidate)
            included_vertices[vertice1] = 1                                          #the vertex 1 is now in the MST
            included_vertices[vertice2] = 1                                          #the vertex 2 is now in the MST
            total_reliability = total_reliability * candidate.reliability             #update total reliability 
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
    
    candidateNumber = ord(candidate.vertice_1) - 65     #convert letter to number (A=0, B=1, C=2 ...)
    included_vertices[candidateNumber] = 1              #update the MST list of vertex
    candidateNumber = ord(candidate.vertice_2) - 65     #convert letter to number (A=0, B=1, C=2 ...)
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
        vertice1 = ord(candidate.vertice_1) - 65                                  #convert letter to number (A=1, B=2, C=3 ...)
        vertice2 = ord(candidate.vertice_2) - 65                                  #convert letter to number (A=1, B=2, C=3 ...)
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

    #First pass for MST only
    candidateList = []
    reliability, cost = computeReliability(edge_list, city_list)
    temList = edge_list.copy()
    candidateList.append(GraphCandidate(cost, reliability, temList))
    tempList = []
    # while there are still remaining vertex
    while(len(remaining_vertices) != 0):
        tempList = []
        #try adding one edge at a time 
        for j in range(len(remaining_vertices)):
            candidate2 = remaining_vertices[j]
            temList = edge_list.copy()
            temList.append(candidate2) 
            #call helper function to compute the all terminal reliability
            reliability, cost = computeReliability(temList, city_list)

            #append to configuration its cost and reliability to the list that is returned by this function
            candidateList.append(GraphCandidate(cost, reliability, temList))
            tempList.append(GraphCandidate(cost, reliability, temList))

        #sort the list to get the best edge and add it to the edge_list for the next iteration of the while loop
        tempList.sort(key=lambda x: x.reliability, reverse=False)
        tempList.sort(key=lambda x: x.cost, reverse=False)

        betterSolution = tempList[0]           
        for item in tempList: 
            if((item.cost <= betterSolution.cost) & (item.reliability > betterSolution.reliability)):
                betterSolution = item
        #add the best edge to edge_list and remove it from remaining_edge list
        edge_list.append(betterSolution.edge_list[-1])
        remaining_vertices.remove(betterSolution.edge_list[-1])
    return candidateList 
    

#helper function to compute the all terminal reliability of a network configuration
def computeReliability(edge_list, city_list): 

    totalEdges = 2 ** len(edge_list)
    reliabilityResults = []
    totalReliability = 0                      #total reliability of this configuration
    for i in range(int(totalEdges)):

        currentCount = list('{0:0b}'.format(i))
        currentCount = currentCount[::-1]
        # List of cities visited by current count
        citiesVisited = [0] * len(city_list)

        # Reliability of edges included in the visit
        currentEdgeReliability = [-1] * len(edge_list)
        # Here, create list that contains zeros of length city_list
        tempEdgeList = list()
        for j in range(len(edge_list)):
            if(j < len(currentCount)):
                if currentCount[j] == '1':
                    edge = edge_list[j]
                    tempEdgeList.append(edge)
                    city1 = ord(edge.vertice_1) - 65
                    city2 = ord(edge.vertice_2) - 65
                    citiesVisited[city1] = 1
                    citiesVisited[city2] = 1
                    currentEdgeReliability[j] = edge.reliability
                else:
                    currentEdgeReliability[j] = 1 - edge_list[j].reliability
            else:
                currentEdgeReliability[j] = 1 - edge_list[j].reliability
        
        # Verify if all cities visited
        if(sum(citiesVisited) == len(city_list)):        #check if all cities where visited (requirement for all terminal reliability computation)

            # Perform DFS --> Returns list of visited nodes, starting at Node A
            g = Graph()
            visited = g.DFS(tempEdgeList, 'A', len(city_list))
            
            if(sum(visited) == len(city_list)):
                Rtot = 1
                for element in range(len(currentEdgeReliability)): 
                    Rtot = Rtot * currentEdgeReliability[element]

                totalReliability = totalReliability + Rtot       #add the reliability of the subpath to the total reliability of the configuration

    cost = 0
    for edge in edge_list:
        cost = cost + edge.cost
    return totalReliability, cost

def parseCandidateListCost(reliability_goal, cost_constraint, optimisationCandidates):
    optimisationCandidates.sort(key=lambda x: x.reliability, reverse=False)
    bestSolution = GraphCandidate(1, 0, None)
    for entry in optimisationCandidates:
        if((entry.cost <= cost_constraint) & (entry.reliability >= bestSolution.reliability) & (entry.reliability > reliability_goal)):
            bestSolution = entry
    return bestSolution

def parseCandidateListPartA(reliability_goal, cost_constraint, optimisationCandidates):
    optimisationCandidates.sort(key=lambda x: x.reliability, reverse=True)
    bestSolution = GraphCandidate(sys.float_info.max, 2, None)
    for entry in optimisationCandidates:
        if((entry.reliability >= reliability_goal) & (entry.reliability < bestSolution.reliability)):
            bestSolution = entry
    return bestSolution