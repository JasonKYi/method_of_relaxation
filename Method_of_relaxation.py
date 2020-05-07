import warnings as wr

class nodes: 

    def __init__(self, name, connections, potiential = 0, *, grounded = False, conductance = None):
        """Initialises the creation of a node with several arguments.
        
        Arguments:
            name {string} -- The name of the node
            connections {list} -- A list of all the names of the the nodes this node is connected to
        
        Keyword Arguments:
            potiential {float} -- The potiential of this node (default: {0})
            grounded {bool} -- Whether or not this particular node is grounded (default: {False})
            conductance {list} -- A list of all the conductances of the edges this node is connected to (default: {None})
        """
        self.name = name
        self.connect = connections
        self.phi = potiential
        self.grounded = grounded
        
        if conductance == None:
            self.conduct = [1 for _ in self.connect]
        else:
            self.conduct = conductance

class graphs:

    def __init__(self, graph):
        """Initialises the creation of a graph.
        
        Arguments:
            graph {list} -- A list of all the nodes within this graph
        """
        self.graph = graph

    def validity(self):
        """Checks if the connected edges are invalid.
        
        Returns:
            int -- Outputs the number of errors found within the specified graph
        """
        Errors_count = 0

        for node in self.graph:
            for i in node.connect:
                for other_node in self.graph:
                    if other_node.name == i and node.name not in other_node.connect:
                        print("node {} is connected to node {} but not the other way around!" .format(other_node.name, node.name))
                        Errors_count += 1

        return Errors_count

    def relaxation(self, n = 100):
        """Estimates the potiential of each node by using the method of relaxation.
        
        Keyword Arguments:
            n {int} -- The number of iterations that will be applied (default: {100})
        """
        if self.validity() != 0:
            wr.warn("This graph is invalid and thus the result of this relaxation is most likely also invalid!", Warning)

        for _ in range(n):
            for node in self.graph:
                if node.grounded == False:
                    potiential_sum, index = 0, 0
                    for connected_name in node.connect:
                        #print("I am averaging over node {}" .format(node.name))

                        for other_node in self.graph:
                            if other_node.name == connected_name:
                                potiential_sum += other_node.phi * node.conduct[index]
                        index += 1

                    node.phi = potiential_sum / sum(node.conduct)
        
        print("The final potientials after relaxation is:")
        for node in self.graph:
            print("node {} has potiential {}" .format(node.name, node.phi))

