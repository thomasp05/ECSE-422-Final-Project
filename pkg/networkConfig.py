
def GraphCandidate(object):

    def __init__(self, _cost, _reliability, _edge_list):
        self.cost = _cost
        self.reliability = _reliability
        self.edge_list = _edge_list

    def getCost(self):
        return self.cost

    def getReliability(self):
        return self.reliability