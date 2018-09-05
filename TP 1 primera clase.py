# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 18:29:49 2018

@author: Admin
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
prot = ldata('C:/Users/Admin/Documents/GitHub/Redes/tc01_data/yeast_AP-MS.txt')
bina = ldata('C:/Users/Admin/Documents/GitHub/Redes/tc01_data/yeast_Y2H.txt')
lit = ldata('C:/Users/Admin/Documents/GitHub/Redes/tc01_data/yeast_LIT.txt')
#%%
P = nx.Graph()
P.add_edges_from(prot)

B = nx.Graph()
B.add_edges_from(bina)

L = nx.Graph()
L.add_edges_from(lit)
#%%

plt.figure(1)

plt.subplot(311)  #fila columna posicion, el tercero numera los espacios
plt.title('Co-pertenencia a complejos proteícos')
nx.draw(P, with_labels= False,node_color = 'b', node_size = 5)

plt.subplot(312)
plt.title('Interacciones binarias')
nx.draw(B, with_labels= False,node_color = 'r', node_size = 5)

plt.subplot(313)
plt.title('Literaria')
nx.draw(L, with_labels= False,node_color = 'y', node_size = 5)
#%%

G = [B,P, L]
N = np.empty_like(G) #i
L = np.empty_like(G) #ii
D_mean = np.empty_like(G) #iv
D_min = np.empty_like(G) 
D_max = np.empty_like(G)
dens = np.empty_like(G)
clu = np.empty_like(G)
clu_d = np.empty_like(G)
diam = np.empty_like(G) 
for i in range(0,len(G)):
    N[i] = G[i].number_of_nodes()
    L[i] = G[i].number_of_edges()
    D_mean[i] = np.mean(G[i].degree.values())  #toma los valores del diccionario
    D_min[i] = np.min(G[i].degree.values())
    D_max[i] = np.max(G[i].degree.values())
    dens[i] = 
    clu[i] = 
    clu_d[i] = 
    diam[i] = 
#%%
dolphins = nx.read_gml('C:/Users/Admin/Documents/GitHub/Redes/tc01_data/dolphins.gml')
dgen = ldata('C:/Users/Admin/Documents/GitHub/Redes/tc01_data/dolphinsGender.txt')

#%%
#Genero el vector de colores para asignarle a la red

color_map = []
for i in range(0,nx.number_of_nodes(dolphins)):
    if [a[1] for a in dgen][i]=='f':
        color_map.append('r')
    elif [a[1] for a in dgen][i]=='m':
        color_map.append('b')
    else:
        color_map.append('k')
#%%      GENERO DE DELFINES
ng= pd.DataFrame(dgender, columns=['name', 'gender'])
ng = ng.set_index('name')
nx.set_node_attributes(dolphins, ng.to_dict(), 'gender')
nx.draw(dolphins, node_color = color_map )
#%%
plt.figure(2)

plt.subplot(321)
plt.title('Random')
nx.draw_random(dolphins, node_size = 5, node_color = color_map )

plt.subplot(322)
plt.title('Spectral')
nx.draw_spectral(dolphins, node_size = 5, node_color = color_map)

plt.subplot(323)
plt.title('Circular')
nx.draw_circular(dolphins, node_size = 5, node_color = color_map)

plt.subplot(324)
plt.title('Spring')
nx.draw_spring(dolphins, node_size = 5, node_color = color_map)

plt.subplot(325)
plt.title('Shell')
nx.draw_shell(dolphins, node_size = 5, node_color = color_map)

plt.subplot(326)
plt.title('Default')
nx.draw(dolphins, node_size = 5, node_color = color_map)

