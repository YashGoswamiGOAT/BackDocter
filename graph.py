import copy
import numpy as np
from support import *
class Node:
    def __init__(self,name,data=None):
        self.name = name
        self.data = data
        self.index = None
        self.id = None
    def setID(self,index):
        self.index = index
        self.id = self.name+"("+str(self.index)+")"
    def __repr__(self):
        if self.id==None:
            return self.name
        return self.id

class Edge:
    def __init__(self,fst,snd,id=None,data=None):
        self.fst = fst
        self.snd = snd
        self.id = id
        self.data = data
    def __repr__(self):
        if self.id==None:
            return f"{self.fst, self.snd}"
        else:
            return f"{self.id}{self.fst, self.snd}"

class HashMap:
    def __init__(self):
        self.map = []
    def set(self,key,value):
        if self.get(key)==-1:
            self.map.append([key, value])
        else:
            for i in range(len(self.map)):
                if self.map[i][0]==key:
                    self.map[i][1] = value
        return self
    def get(self,key):
        for i in range(len(self.map)):
            if(self.map[i][0]==key):
                return self.map[i][1]
        return -1
    def keys(self):
        keys_ = []
        for key__ in self.map:
            keys_.append(key__[0])
        return keys_
    def values(self):
        values_ = []
        for value__ in self.map:
            values_.append(value__[1])
        return values_
    def remove(self,key):
        return_ = False
        try:
            for i in range(len(self.map)):
                if (self.map[i][0] == key):
                    self.map.remove(self.map[i])
                    return_ = True
            return self if return_ else return_
        except:
            return return_
    def __repr__(self):
        return str(self.map)

class HashMapList:
    def __init__(self):
        self.map = []
    def set(self,key,value):
        if self.get(key)==-1:
            self.map.append([key, [value]])
        else:
            for i in range(len(self.map)):
                if self.map[i][0]==key:
                    self.map[i][1] = [value]
        return self
    def add(self,key,value):
        if self.get(key)==-1:
            self.map.append([key, [value]])
        else:
            for i in range(len(self.map)):
                if self.map[i][0]==key:
                    self.map[i][1].append(value)
        return self
    def get(self,key):
        for i in range(len(self.map)):
            if(self.map[i][0]==key):
                return self.map[i][1]
        return -1
    def keys(self):
        keys_ = []
        for key__ in self.map:
            keys_.append(key__[0])
        return keys_
    def values(self):
        values_ = []
        for value__ in self.map:
            values_.append(value__[1])
        return values_
    def remove(self,key):
        return_ = False
        try:
            for i in range(len(self.map)):
                if (self.map[i][0] == key):
                    self.map.remove(self.map[i])
                    return_ = True
            return self if return_ else return_
        except:
            return return_
    def removeValue(self,key,value):
        return_ = False
        try:
            for i in range(len(self.map)):
                if (self.map[i][0] == key):
                    self.map[i][1].remove(value)
                    return_ = True
            return return_
        except:
            return self if return_ else return_
    def uniques(self,key):
        new_k = []
        for key_ in range(len(self.map)):
            if self.map[key_][0]==key:
                for elem in self.map[key_][1]:
                    if elem not in new_k:
                        new_k.append(elem)
                self.map[key_][1] = new_k
    def __repr__(self):
        return str(self.map)

class Graph:
    def __init__(self,graph,nodes):
        if graph==[] and nodes==[]:
            self.graph = []
            self.nodes = []
            self.matrix = []
        else:
            self.graph = list(graph)
            self.matrix = list(copy.deepcopy(graph))
            self.nodes = list(nodes)
            for i in range(len(self.nodes)):
                self.nodes[i].setID(i)
            for nodeA in self.nodes:
                for nodeB in self.nodes:
                    indexA = self.nodes.index(nodeA)
                    indexB = self.nodes.index(nodeB)
                    if self.graph[indexA][indexB]!=0:
                        if type(self.graph[indexA][indexB])!=type([]):
                            self.graph[indexA][indexB] = Edge(nodeA, nodeB)
                        else:
                            ways = []
                            for way in range(len(self.graph[indexA][indexB])):
                                ways.append(Edge(nodeA, nodeB, way))
                            self.graph[indexA][indexB] = ways
    def createEdge(self,fst,snd,both=True,data=None):
        indexA = self.nodes.index(fst)
        indexB = self.nodes.index(snd)
        if self.graph[indexA][indexB]==0:
            if both:
                self.graph[indexA][indexB] = Edge(fst, snd,data=data)
                self.matrix[indexA][indexB] = 1
                self.graph[indexB][indexA] = Edge(snd, fst,data=data)
                self.matrix[indexB][indexA] = 1
            else:
                self.graph[indexA][indexB] = Edge(fst, snd)
                self.matrix[indexA][indexB] = 1
        elif type(self.graph[indexA][indexB]) == type(Edge(fst, snd,data=data)):
            if both:
                way = [self.graph[indexA][indexB]]
                self.graph[indexA][indexB].id = 0
                way.append(Edge(fst, snd, 1,data=data))
                self.graph[indexA][indexB] = list(way)
                way = [self.matrix[indexA][indexB]]
                way.append(1)
                self.matrix[indexA][indexB] = list(way)

                way = [self.graph[indexB][indexA]]
                self.graph[indexB][indexA].id = 0
                way.append(Edge(snd, fst, 1))
                self.graph[indexB][indexA] = list(way)
                way = [self.matrix[indexB][indexA]]
                way.append(1)
                self.matrix[indexB][indexA] = list(way)
            else:
                way = [self.graph[indexA][indexB]]
                self.graph[indexA][indexB].id = 0
                way.append(Edge(fst, snd, 1,data=data))
                self.graph[indexA][indexB] = list(way)
                way = [self.matrix[indexA][indexB]]
                way.append(1)
                self.matrix[indexA][indexB] = list(way)
        elif type(self.graph[indexA][indexB]) == type([]):
            if both:
                self.graph[indexA][indexB].append(Edge(fst, snd, len(self.graph[indexA][indexB]),data=data))
                self.matrix[indexA][indexB].append(1)

                self.graph[indexB][indexA].append(Edge(fst, snd, len(self.graph[indexB][indexA]),data=data))
                self.matrix[indexB][indexA].append(1)
            else:
                self.graph[indexA][indexB].append(Edge(fst, snd, len(self.graph[indexA][indexB]),data=data))
                self.matrix[indexA][indexB].append(1)
        return self

    def addNode(self,node):
        i = len(self.nodes)
        self.nodes.append(node)
        node.setID(i)
        if self.graph == []:
            self.graph.append([])
            self.matrix.append([])
            self.graph[0].append(0)
            self.matrix[0].append(0)
        else:
            for vector in self.graph:
                vector.append(0)
            for vector in self.matrix:
                vector.append(0)
            self.graph.append([0]*(i+1))
            self.matrix.append([0]*(i+1))
        return self
    def getEdge(self,nodeA,nodeB):
        return self.graph[self.nodes.index(nodeA)][self.nodes.index(nodeB)]
    def displacement(self,node):
        Disp = self.distance(node)
        for pair in range(len(Disp.map)):
            key = Disp.map[pair][0]
            values = Disp.map[pair][1]
            shortest_len = None
            shortest_dists = []
            for value in values:
                if shortest_len==None:
                    shortest_len = len(value)
                elif shortest_len>len(value):
                    shortest_len = len(value)
            for value in values:
                if shortest_len==len(value):
                    shortest_dists.append(value)
            Disp.map[pair][1] = shortest_dists
        return Disp
    def distance(self,node):
        Disp = HashMapList()
        Rejection = [node]
        Disp.add(node,[node])
        Matrix = list(self.graph)
        def simulation(node_, mat_, rejection_):
            for edge in mat_[self.nodes.index(node_)]:
                r_ = list(rejection_)
                if edge != 0:
                    if type(edge)!=type([]):
                        disp = []
                        if edge.snd not in r_:
                            for distance_ in Disp.get(edge.fst):
                                if edge.snd not in distance_:
                                    tempdist = []
                                    for node__ in distance_:
                                        tempdist.append(node__)
                                    tempdist.append(edge.snd)
                                    disp.append(tempdist)
                            for dist_ in disp:
                                Disp.add(edge.snd, dist_)
                            r_.append(edge.snd)
                            simulation(edge.snd, mat_, r_)
                    else:
                        for edge_ in edge:
                            disp = []
                            if edge_.snd not in r_:
                                for distance_ in Disp.get(edge_.fst):
                                    if edge_.snd not in distance_:
                                        tempdist = []
                                        for node__ in distance_:
                                            tempdist.append(node__)
                                        tempdist.append(edge_.snd)
                                        disp.append(tempdist)
                                for dist_ in disp:
                                    Disp.add(edge_.snd, dist_)
                                r_.append(edge_.snd)
                                simulation(edge_.snd, mat_, r_)
        simulation(node, Matrix, Rejection)
        for pair in range(len(Disp.map)):
            Disp.uniques(Disp.map[pair][0])
        return Disp
    def getNode(self,filter={}):
        nodes = []
        for node in self.nodes:
            if Filter(filter,node.__dict__):
                nodes.append(node)
        return nodes
    def createPath(self,nodeset):
        paths = []
        for i in range(len(nodeset)-1):
            pathUpdated = []
            nodeA = nodeset[i]
            nodeB = nodeset[i+1]
            edgeObj = self.getEdge(nodeA, nodeB)
            if paths==[] and type(edgeObj)==type([]):
                for path_ in edgeObj:
                    paths.append([path_])
            elif paths==[] and type(edgeObj)==type(paths[0][0]):
                paths.append([edgeObj])
            elif paths != [] and type(edgeObj) == type([]):
                for path_ in paths:
                    for path__ in edgeObj:
                        pathUpdated.append(concatinateList(path_,[path__]))
                paths = pathUpdated
            elif paths != [] and type(edgeObj) == type(paths[0][0]):
                for path_ in paths:
                    pathUpdated.append(concatinateList(path_,[edgeObj]))
                paths = pathUpdated
        return paths
    def getCycles(self,path):
        cycles = []
        paths = self.distance(path[0]).get(path[-1])
        for path_ in paths:
            path_ = list(path_)
            for i in range(len(path)):
                node = path[i]
                if node in path_:
                    path_.remove(node)
            cycles.append(path_)
        def Filter():
            rejectionCycle = []
            for cycle in cycles:
                if cycle == []:
                    rejectionCycle.append(cycle)
                for j in range(len(cycle) - 1):
                    if self.getEdge(cycle[j], cycle[j + 1]) == 0:
                        rejectionCycle.append(cycle)
                        break
            for cyc_ in rejectionCycle:
                cycles.remove(cyc_)
        Filter()
        return cycles
    def getDepth(self,node):
        Disp = self.displacement(node)
        depth = HashMap()
        for node in Disp.keys():
            depth.set(node,len(Disp.get(node)[0])-1)
        return depth
    def __repr__(self):
        return str(self.graph)