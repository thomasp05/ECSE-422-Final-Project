#Thomas Philippon and Tristan Bouchard 
#Implementation of the Prim's algorithm 

import string
from edge import Edge
alphabet_list = list(string.ascii_uppercase)

#Function for computing the minimun spanning tree with Prim's algorithm 
#Input1: city_list is the list of cities 
#Input2: edge_list is the list of all possible edges with their reliability and cost.
def doPrims(city_list, edge_list): 
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
        index = index+1
    return mst_vertices_list, total_reliability, remaining_vertices
