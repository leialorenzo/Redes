# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
#%%
def ldata(archive):
    f=open(archive)
    data=[]
    for line in f:
        line=line.strip()
        col=line.split()
        data.append(col)
    return data
#%%
#=============================================================
binaria = ldata('tc01_data/yeast_Y2H.txt')
prot = ldata('tc01_data/yeast_AP-MS.txt')
lit = ldata('tc01_data/yeast_LIT.txt')
#%%
#=============================================================
plt.figure(1)
G_bin = nx.Graph(binaria)
G_bin.add_edges_from(binaria)
nx.draw(G_bin, with_labels=True, font_weight='bold')

plt.figure(2)
G_lit = nx.Graph(lit)
G_lit.add_edges_from(lit)
nx.draw(G_lit, with_labels=True, font_weight='bold')

plt.figure(3)
G_prot = nx.Graph(prot)
G_prot.add_edges_from(prot)
nx.draw(G_prot, with_labels=True, font_weight='bold')

plt.show()
#============================================================
G_bin = nx.Graph(binaria)
G_bin.add_edges_from(binaria)
G_lit = nx.Graph(lit)
G_lit.add_edges_from(lit)
G_prot = nx.Graph(prot)
G_prot.add_edges_from(prot)
#=============================================================
plt.figure(1)
plt.title("Comparativa de los complejos proteicos")
nx.draw(G_bin, with_labels=False, node_color='red', node_size=5, font_weight='bold')
plt.legend("Binario")
nx.draw(G_lit, with_labels=False,node_color='blue', node_size=5, font_weight='bold')
plt.legend("Literature")
nx.draw(G_prot, with_labels=False,node_color='green', node_size=5, font_weight='bold')
plt.legend("Proteico")
plt.show()
#=============================================================
B = G_bin
P = G_prot
L = G_lit
G = [B,P, L]
N = np.empty_like(G) #i
L = np.empty_like(G) #ii
D = np.empty_like(G) #iv
G_mean = np.empty_like(G) #Enlaces que llegan a cada nodo
G_max = np.empty_like(G)
G_min  = np.empty_like(G)
dens = np.empty_like(G)
clu = np.empty_like(G)
clu_d = np.empty_like(G)
diam = np.empty_like(G)



def grados_BPL(r):
    L = len(G[r])
    degrees = np.zeros(L)#argumento = elemento de G (indice)
    for j in range(0,L): #G[r], un grafo particular de G
        degrees[j] = list(G[r].degree())[j][1] #este for #sirve para ir armando una lista de únicamente los grados por #nodo de cada grafo de G. El primer list convierte el degree
#view a una lista, conformada por pares (nombre de proteina,
#,cantidad de enlaces), el [j][1] barre toda la lista seleccionan
#do sólo la cantidad de links. Esa lista final es "degrees"
#conformada por la cantidad de nodos del grafo G[r].
    return degrees
    
for i in range(0,len(G)):
    N[i] = G[i].number_of_nodes()
    L[i] = G[i].number_of_edges()
    G_mean[i] = np.mean(grados_BPL(i)) #opero con la lista de #la función que cree
    G_max[i] = np.max(grados_BPL(i))
    G_min[i] = np.min(grados_BPL(i))
    dens[i] = nx.density(G[i])
    clu[i] = nx.average_clustering(G[i])
    clu_d[i] = nx.transitivity(G[i])
    diam[i] = nx.diameter(max(nx.connected_component_subgraphs(G[i]), key=len))

tabla = pd.DataFrame({"Red":["binarias","proteicas","Literatura"],"# de nodos":N,"# total de enlaces":L,"Grado medio":G_mean,"Grado máximo":G_max,"Grado mínimo":G_min,"Densidad de la red":dens,"Coef. de Clust. red": clu,"Sqr. Coef. de Clust. red":clu_d,"Diámetro de la red":diam})
#%%




