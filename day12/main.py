import networkx as nx
import matplotlib.pyplot as plt
import collections

with open('input') as f:
    lines = [line.rstrip() for line in f.readlines()]


def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


def generate_graph(input_lines):
    G = nx.Graph()

    for line in input_lines:
        # Split the lines
        _edges = line.split(' <-> ')
        # Split second part into a list of ints
        _edges[1] = list(map(int, _edges[1].split(', ')))
        # Cast first element to int
        _edges[0] = int(_edges[0])
        # Flatten the whole list into one
        _edges = list(flatten(_edges))
        # print('Edges', _edges)
        if _edges[0] == _edges[1]:
            G.add_node(_edges[0])
            # print('Snake at:', _edges[0])
        for _edge in _edges[1:]:
            # print('Adding edge: {} -> {}'.format(_edges[0], _edge))
            G.add_edge(_edges[0], _edge)
    return G


graph = generate_graph(input_lines=lines)
# print('Nodes:', list(graph.nodes))
# print('Edges:', list(graph.edges))
# print('Degree:', graph.degree)
# print('Isolates:', list(nx.isolates(graph)))
# print('Descendants of 0', list(nx.descendants(graph, 0)))
# print('Descendant count:', len(list(nx.descendants(graph, 0))))
# print('Unreachable from 0:', set(graph.nodes) - set(nx.descendants(graph, 0)))
# print('Unreachable count:', len(set(graph.nodes) - set(nx.descendants(graph, 0))))
# print('\n')

print('Part 1 answer')
print('Programs containing 0:', len(list(nx.descendants(graph, 0))) + 1)
print('Part 2 answer')
print('Connected components: ', len([len(c) for c in sorted(nx.connected_components(graph), key=len, reverse=True)]))

# Draw!
# nx.draw(graph, with_labels=True, font_weight='bold')
# plt.savefig("graph.png")
