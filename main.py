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

print(city_list)
print(edge_list)

edges_mst, Rtot, remaining_vertices, total_cost = networkComputation.doPrimsReliability(city_list, edge_list)
edges_mst_cost, Rtot_cost, remaining_vertices_cost, total_cost_cost = networkComputation.doPrimsCost(city_list, edge_list)

print("info on Prim's solution: ")
print(edges_mst) 
print(Rtot) 
print(remaining_vertices) 
print(total_cost) 

#check if the reliability goal is met by the MST 
if(Rtot >= float(reliability_goal)): 
	print("The reliability goal is met by the MST with following configuration: ")
	print(edges_mst)
	print("Total Reliability=" + str(Rtot))
else: 
    print("The reliability goal is not met just by the MST, lets perform augmentation \n")
    optimisationCandidates_Reliability = networkComputation.computeAllTerminalReliability(edges_mst, remaining_vertices, city_list, Rtot, float(reliability_goal))
    optimisationCandidates_cost = networkComputation.computeAllTerminalReliability(edges_mst_cost, remaining_vertices_cost, city_list, Rtot_cost, float(reliability_goal))
    result_reliability = networkComputation.parseCandidateListReliability(float(reliability_goal), float(cost_constraint), optimisationCandidates_Reliability)
    result_cost = networkComputation.parseCandidateListReliability(float(reliability_goal), float(cost_constraint), optimisationCandidates_cost)

    print("Final Result with Reliability MST: \n", result_reliability.edge_list, result_reliability.cost, result_reliability.reliability)
    print("Final Result with Cost MST: \n", result_cost.edge_list, result_cost.cost, result_cost.reliability)
    


# print(edges_mst) 
# print("Total reliability = "+ str(Rtot))
# print("Remaining vertices: ")
# print(remaining_vertices)

