# coding=utf-8
import random


def karger_min_cut(graph, groups = None):
    # Create graph for first iteration
    if groups is None:
        groups = {graph[i][0]:[graph[i][0]] for i in graph}
    # Base Case
    if len(graph) == 2:
        return graph, groups
    # Select edge to contract
    # Every edge appears twice in the list, so selecting at random from it is identical to selecting an edge at random

    # Contract
    # Select "first node" to allocate name
    # Merge edges to represent edges connected to new "supernode"
    # Remove self-edges
    # Merge groups to represent set of nodes belonging to supernode

    # Next iteration