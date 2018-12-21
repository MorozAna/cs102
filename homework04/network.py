from api import get_friends
from config import VK_CONFIG
from igraph import Graph, plot
import numpy as np

def get_network(users_ids, as_edgelist=True):
    vertices = [i for i in range(len(users_ids))]
    edges = []
    for user in users_ids:
    	friends = get_friends(user, 'sex')
    	if friends != None:
    	    for i in range(len(users_ids)):
    		    friend = users_ids[i]
    		    resp = friends.get('response')
    		    if resp != None:
    		        for a in friends.get('response').get('items'):
    			        if a.get('id') == friend:
    				        b = (users_ids.index(user), i)
    				        edges.append(b)
    lis = (vertices, edges)
    return lis


def plot_graph(graph):
    vertices, edges = graph
    g = Graph(vertex_attrs={"label":vertices},
    edges=edges, directed=False)


    N = len(vertices)
    visual_style = {}
    visual_style["layout"] = g.layout_fruchterman_reingold(
        maxiter=1000,
        area=N**3,
        repulserad=N**3)

    g.simplify(multiple=True, loops=True)
    plot(g, **visual_style)


t = get_network([c.get('id') for c in get_friends(218772230, 'sex').get('response').get('items')], as_edgelist=True)
plot_graph(t)