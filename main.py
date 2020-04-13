# The input file is in the format:
# Number of cities: A B C D ...(N cities)
# Cost/Reliability matrix: A-B,A-C,A-D...B-C,B-D...C-D....(N(N-1)/2)
import pkg
from pkg import edge_generator
from pkg import networkComputation

try:
	file_path = input("Please set input file path: ")
	reliability_goal = input("Please enter reliability goal: ")
	cost_constraint = input("Please enter cost constraint: ")
except ValueError:
    print(ValueError)
    exit()

city_list, edge_list = edge_generator.generate(file_path)

print("\nCity List: \n", city_list)
print("\nEdge List: \n", edge_list)
print("\nReliability Goal: ", reliability_goal)
print("Cost Constraint: ", cost_constraint)

#Compute two MSTs. One unsing cost and the other using reliability
edges_mst, Rtot, remaining_vertices, total_cost = networkComputation.doPrimsReliability(city_list, edge_list)
edges_mst_cost, Rtot_cost, remaining_vertices_cost, total_cost_cost = networkComputation.doPrimsCost(city_list, edge_list)

#perform augmentation on the MSTs
optimisationCandidates_Reliability = networkComputation.computeAllTerminalReliability(edges_mst, remaining_vertices, city_list, Rtot, float(reliability_goal))
optimisationCandidates_cost = networkComputation.computeAllTerminalReliability(edges_mst_cost, remaining_vertices_cost, city_list, Rtot_cost, float(reliability_goal))

##Part A: meet a given reliability goal 
#check if the reliability goal is met by the MST 
if(Rtot >= float(reliability_goal)): 
    print("\n\n---Part A: Meet a given reliability goal---\n")
    print("Total reliability: ", Rtot)
    print("Total cost: ",total_cost)
    print("Edge list: \n", edges_mst)
else: 
    #get the first result that meets the reliability goal 
    result_partA = networkComputation.parseCandidateListPartA(float(reliability_goal), float(cost_constraint), optimisationCandidates_Reliability)
    if(result_partA.reliability !=2):
        print("\n\n---Part A: Meet a given reliability goal---\n")
        print("Total reliability: ", result_partA.reliability)
        print("Total cost: ", result_partA.cost)
        print("Edge list: \n", result_partA.edge_list) 
    else: 
        print("\n\n---Part A: Meet a given reliability goal---\n")
        print("no result found for part A")

##Part B: maximize reliability subject to a given cost constraint 
#results part B 
result_reliability = networkComputation.parseCandidateListCost(float(reliability_goal), float(cost_constraint), optimisationCandidates_Reliability)
result_cost = networkComputation.parseCandidateListCost(float(reliability_goal), float(cost_constraint), optimisationCandidates_cost)

if((result_cost.reliability >= result_reliability.reliability) or (result_reliability.reliability== 0)): 
    if(result_cost.reliability != 0): 
        print("\n\n---Part B: Maximize reliability goal subject to a given cost constraint---\n")
        print("Total reliability: ", result_cost.reliability)
        print("Total cost: ", result_cost.cost)
        print("Edge list: \n", result_cost.edge_list) 
    else: 
        print("\n\n---Part B: Maximize reliability goal subject to a given cost constraint---\n")
        print("no result found for part B")
else: 
    print("\n\n---Part B: Maximize reliability goal subject to a given cost constraint---\n")
    print("Total reliability: ", result_reliability.reliability)
    print("Total cost: ", result_reliability.cost)
    print("Edge list: \n", result_reliability.edge_list) 

