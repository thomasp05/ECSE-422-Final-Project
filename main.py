# The input file is in the format:
# Number of cities: A B C D ...(N cities)
# Cost/Reliability matrix: A-B,A-C,A-D...B-C,B-D...C-D....(N(N-1)/2)
import edge_generator
import prims

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

print('Solution: ')
edges_mst, Rtot,remaining_vertices = prims.doPrims(city_list, edge_list)
print(edges_mst) 
print("Total reliability = "+ str(Rtot))
print("Remaining vertices: ")
print(remaining_vertices)
