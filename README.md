# ECSE 422 - Fault Tolerant Computing
### Final Project: Network Optimisation

#### Tristan Bouchard (260747124), Thomas Philippon (260747645)

This project is realised in the context of ECSE 422 - Fault Tolerant Computing at McGill University. The goal of the project is to connect and optise a network of cities, given a set of edges with a given reliability and cost.

The project begins by parsing a text file, which serves to configure the network. The format is as follows: 

```
# this is a comment - skip lines starting with a hash
#
# number of nodes
6
#
# symmetric reliability matrix - stored in row major form
#
0.94 0.91 0.96 0.93 0.92 0.94 0.97 0.91 0.92 0.94 0.90 0.94 0.93 0.96 0.91
#
# symmetric cost matrix - stored in row major form
#
10 25 10 20 30 10 10 25 20 20 40 10 20 10 30
#
# end 
```
The program runs on Python3.7.4

To run the program, simply run the main.py file using `python main.py` from the command line. The program will then ask for the path to the configuration file, the requested reliability and the requested cost.

The program will then compute two Minimum Spanning Trees (MSP) for the graph, one with the highest reliability possible and the other with the lowest cost possible. Following this, it augments the MST using the remaining edges that were not selected for the MST. The MST is augmented by adding one edge at a time until there is no more edges available. The edge that is added each iteration is the one that maximizes the reliability while minimizing the cost. The new configurations are appended to a list of configurations containing the edges, cost and reliability for each configuration. This list is then parsed according to the following criteria, to return two results:

_a) Meet the reliability goal specified as input._

The result returned is the one as close as possible to the specified result with the lowest cost possible.

_b) Maximize the reliability of the graph given a cost constraint specified as input._

The result returned is the one with the highest reliability for the given cost.
