from Method_of_relaxation import nodes, graphs

node_a = nodes("a", ["b", "c"], 1, grounded = True)
node_b = nodes("b", ["a", "d"], 0, grounded = True)
node_c = nodes("c", ["a", "d", "e"])
node_d = nodes("d", ["c", "f", "b"])
node_e = nodes("e", ["c", "f"])
node_f = nodes("f", ["d", "e"])

graph_a = graphs([node_a, node_b, node_c, node_d, node_e, node_f])
#graph_a.validity()
graph_a.relaxation(100)

node_p = nodes("p", ["q"], 1, grounded = True)
node_q = nodes("q", ["p", "r"], conductance = [2, 1])
node_r = nodes("r", ["q"], 0, grounded = True)

#graph_b = graphs([node_p, node_q, node_r])
#graph_b.validity()
#graph_b.relaxation()