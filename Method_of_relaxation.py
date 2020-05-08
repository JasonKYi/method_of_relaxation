class nodes:

    def __init__(self, name, connections, potiential=None, *, conductance=None):
        """Initialises the creation of a node with several arguments.

        Arguments:
            name {string} -- The name of the node
            connections {list} -- A list of all the names of the the nodes this node is connected to

        Keyword Arguments:
            potiential {float} -- The potiential of this node, if specified the node will be assumed to be grounded (default: {None})
            conductance {list} -- A list of all the conductances of the edges this node is connected to (default: {None})
        """
        self.name = name
        self.connect = connections

        if potiential == None:
            self.phi = 0
            self.grounded = False
        else:
            self.phi = potiential
            self.grounded = True

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

        from warnings import warn
        from itertools import product

        Errors_count = 0

        for node, other_node in product(self.graph, self.graph):
            if other_node.name in node.connect and node.name not in other_node.connect:
                warn("node {} is connected to node {} but not the other way around!" .format(
                    other_node.name, node.name))
                Errors_count += 1

        return Errors_count

    def relaxation(self, n=100, check=True):
        """Estimates the potiential of each node by using the method of relaxation.

        Keyword Arguments:
            n {int} -- The number of iterations that will be applied (default: {100})
            check {bool} -- Whether or not the inputed graph will be checked for its validity (default : {True})
        """

        from warnings import warn
        from itertools import product

        if check == True:
            if self.validity() != 0:
                warn(
                    "This graph is invalid and thus the result of this relaxation is most likely also invalid!", Warning)

        for _, node in product(range(n), self.graph):
            if node.grounded == False:
                potiential_sum, index = 0, 0
                for other_node in [other for other in self.graph if other.name in node.connect]:
                    potiential_sum += other_node.phi * \
                        node.conduct[index]
                index += 1

                node.phi = potiential_sum / sum(node.conduct)

        print("The final potientials after relaxation is:")
        for node in self.graph:
            print("node {} has potiential {}" .format(node.name, node.phi))
