import string
from .edge import Edge
alphabet_list = list(string.ascii_uppercase)


def read_data(filePath):
    number_of_cities = None
    costs = None
    reliabilities = None
    input_file = open(filePath)
    for line in input_file:
        if '#' in line:
            continue
        if number_of_cities is None:
            number_of_cities = line
            continue
        if reliabilities is None:
            reliabilities = line.rstrip('\n').split(' ')
            continue
        if costs is None:
            costs = line.rstrip('\n').split(' ')
            continue
    return number_of_cities,costs,reliabilities


def generate(filePath):
    number_of_cities, costs,reliabilities = read_data(filePath)
    city_list = alphabet_list[0:int(number_of_cities)]
    edge_list = list()
    row = 0
    col = 1

    for reliability,cost in zip(reliabilities,costs):
        edge_list.append(Edge(city_list[row],city_list[col],float(cost),float(reliability)))
        if(col == len(city_list)-1):
            row = row+1
            col = row+1
        else:
            col= col+1
    return city_list, edge_list
