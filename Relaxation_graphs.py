from Method_of_relaxation import nodes, graphs

"""This file contains examples of creating and using the available methods.
There are two graphs presented - `graph_a` and `graph_b`

`graph_a` is a valid graph with 6 nodes while `graph_b` is not a valid graph with 3 nodes.

"""

# Nodes are objects containing its name, the name of other nodes its connected to
# its potiential (leave empty if its not grounded) and the conductance of edges 
# its connected to.
node_a = nodes("a", ["b", "c"], 1)
node_b = nodes("b", ["a", "d"], 0)
node_c = nodes("c", ["a", "d", "e"])
node_d = nodes("d", ["c", "f", "b"])
node_e = nodes("e", ["c", "f"])
node_f = nodes("f", ["d", "e"])

# graph_a is valid

# A graph is designed to be a list of nodes
graph_a = graphs([node_a, node_b, node_c, node_d, node_e, node_f])
graph_a.validity()
graph_a.relaxation()

# graph_b is invalid

node_p = nodes("p", ["q"], 1)
node_q = nodes("q", ["p"], conductance=[2, 1])
node_r = nodes("r", ["q"], 0)

graph_b = graphs([node_p, node_q, node_r])
graph_b.validity()
graph_b.relaxation()
