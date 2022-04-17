# coding=utf-8
import random


def karger_min_cut(graph, groups = None):
    """
    TODO: Provide full description and improve by using list mutability
    :param graph:
    :param groups:
    :return:
    """
    # Create graph for first iteration
    if groups is None:
        groups = {node[0]: [node[0]] for node in graph}
    # Base Case
    if len(graph) == 2:
        return graph, groups
    # Select edge to contract
    # Every edge appears twice in the list, so selecting at random from it is identical to selecting an edge at random
    double_number_of_edges = sum([len(node[1]) for node in graph])
    assert(double_number_of_edges % 2 == 0, "the algorithm failed to calculate the number of edges")
    chosen_edge = random.randint(0, double_number_of_edges - 1)
    for node_i in range(0, len(graph)):
        if len(graph[node_i][1]) > chosen_edge:
            # Leverage mutability of lists
            super_node = graph[node_i]
            break
        else:
            chosen_edge = chosen_edge - len(graph[node_i][1])
    else:
        # This condition triggers if the edge was never found and therefore the "break" never triggered
        raise BaseException("OH NO, the algorithm failed to select a random edge!")
    # Contraction starts here, find other edge
    for node_j in range(0, len(graph)):
        if graph[node_j][0] == super_node[1][chosen_edge]:
            # Merge groups to represent set of nodes belonging to supernode
            groups[super_node[0]] = groups[super_node[0]] + groups[graph[node_j][0]]
            # Erase old edge from groups
            del groups[graph[node_j][0]]
            # Remove old node from graph
            old_node = graph.pop(node_j)
            # Merge edges to represent edges connected to new "supernode"
            super_node[1] = super_node[1] + old_node[1]
            # Remove self-edges
            while super_node[0] in super_node[1]:
                super_node[1].remove(super_node[0])
            while old_node[0] in super_node[1]:
                super_node[1].remove(old_node[0])
            # Break as there should only be one match in the graph to this node name
            break
        else:
            next
    else:
        # This condition triggers if the edge was never found and therefore the "break" never triggered
        raise BaseException("OH NO, the algorithm failed to find the other end (-node) of the edge!")
    # Convert all old edges pointing at the old node name so that they point to the new "supernode" name
    for node_k in range(0, len(graph)):
        graph[node_k][1] = \
            [super_node[0] if node_name in groups[super_node[0]] else node_name for node_name in graph[node_k][1]]
    # Next iteration, and shuffle graph to increase randomness
    # (see: https://www.coursera.org/learn/algorithms-divide-conquer/discussions/forums/CXveinblEeag2QpBph2LIw/threads/LjLJjoPMEeyNrhIa8nLyQw)
    random.shuffle(graph)
    return karger_min_cut(graph=graph, groups=groups)


if __name__ == '__main__':
    random.seed(234)
    graph_test_1 = [[1, [2, 3]],
                    [2, [1]],
                    [3, [1]]]

    graph_test_2 = [[1, [2, 3]],
                    [2, [1, 3]],
                    [3, [1, 2]]]

    graph_test_3 = [[1, [2, 3]],
                    [2, [1, 4]],
                    [3, [1, 4]],
                    [4, [2, 3]]]
    for graph_test in [graph_test_1, graph_test_2, graph_test_3]:
        print(karger_min_cut(list(graph_test), groups=None))

    min_cut = 1000
    for i in range(1000):
        # Lists are mutable, therefore we must reload at every run
        with open("KargerMinCut_data.txt") as f:
            starting_graph = [string_line.strip('\t\n').split("\t") for string_line in f.readlines()]
            starting_graph = [[node[0], node[1:]] for node in starting_graph]
        latest_graph, latest_groups = karger_min_cut(starting_graph, groups=None)
        min_cut = min(min_cut, len(latest_graph[0][1]))
        print(min_cut)
        print(latest_graph)
        print(latest_groups)
    print("The min cut is: " + str(min_cut))
