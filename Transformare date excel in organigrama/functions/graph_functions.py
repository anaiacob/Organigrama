from collections import deque
from .strings_functions import numarare
class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []
        self.left = None
        self.right = None
    def add_neighbor(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)
    def __getitem__(self, node):
        return self.nodes.get(node, [])
    def __repr__(self):
        return f"Node({self.value})"
    

class Graph:
    def __init__(self):
        self.nodes = []
    def add_node(self, node):
        self.nodes.append(node)
    def add_edge(self, node1, node2):
        # Adăugăm muchia doar într-o direcție, deoarece graful este neorientat
        node1.add_neighbor(node2)
        node2.add_neighbor(node1)
    def __repr__(self):
        return f"Graph({self.nodes})"
    

def build_graph(parents, children):
    graph = {}
    
    # Adaugă relația de la părinte la copil
    for parent, child in zip(parents, children):
        if parent not in graph:
            graph[parent] = []
        graph[parent].append(child)
        
        # Adaugă relația inversă de la copil la părinte
        if child not in graph:
            graph[child] = []
        graph[child].append(parent)
    
    return graph

def dfs(node, visited, graph, level, h,first, prev_node=None):
    visited.add(node)
    for neighbor in graph.get(node, []):
        if neighbor != prev_node:
            if neighbor not in visited and neighbor!=first:
                # Continuăm traversarea DFS și creștem nivelul cu 1
                level[neighbor] = level[node] + 1
                # Actualizăm înălțimea maximă (h) dacă este necesar
                if h < level[neighbor]:
                    h = level[neighbor]
                h=dfs(neighbor, visited, graph, level, h, first, node)
    return h

def print_graph_dfs(graph, start_node,first):
    visited = set()
    visited.add(start_node)
    level = {start_node: 1}# Inițializăm nivelul nodului de start cu 0
    h = 1  # Inițializăm înălțimea maximă cu 0
    h = dfs(start_node, visited, graph, level, h,first,)
    return h

def count_children_except(graph, node, excluded_child):
    children_count = 0
    
    # Parcurgem lista de vecini a nodului
    for child in graph.get(node, []):
        # Verificăm dacă vecinul nu este copilul exclus și îl numărăm ca fiind copil
        if child != excluded_child:
            children_count += 1
    
    return children_count

def level_order_traversal(graph, root, first, node_levels, h):
    if root is None:
        return
    
    queue = deque([(root, 1, None, -1)]) 
    visited = set()
    visited.add(root)
    
    while queue:
        current_node, level, parent, granny = queue.popleft()
        node_levels.append((current_node, level, parent, granny))
        
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited and neighbor != first:
                if level <= h:  
                    new_granny = -1  
                else:
                    new_granny = parent if level == h + 1 else granny  # Modificăm valoarea pentru niveluri mai mari decât h
                    
                queue.append((neighbor, level + 1, current_node, new_granny))  
                visited.add(neighbor)
                
def centralizare(data1,graph, node, first, node_levels, h, level=1, parent=None, granny=-1, visited=None,prev_node=None):
    
    print("centralizare",end="\n")
    if visited is None:
        visited = set()
    print(node, end="\n")
    print(type(node),end="\n")
    node=int(node)
    visited.add(node)
    
    # conds1=numarare(data1,node,'Conducere1','Standard')
    # print("done",end="\n")
    # conds2=numarare(data1,node,'Conducere2','Standard')
    # print("done",end="\n")
    # maistris=numarare(data1,node,'Maistri','Standard')
    # print("done",end="\n")
    # tesas=numarare(data1,node,'Tesa','Standard')
    # print("done",end="\n")
    # muncitors=numarare(data1,node,'Muncitori','Standard')
    # print("done",end="\n")
    # condpt1=numarare(data1,node,'Conducere1','Timp partial')
    # print("done",end="\n")
    # condpt2=numarare(data1,node,'Conducere2','Timp partial')
    # print("done",end="\n")
    # tesapt=numarare(data1,node,'Tesa','Timp partial')
    # print("done",end="\n")
    # muncitorpt=numarare(data1,node,'Muncitori','Timp partial')
    # print("done",end="\n")
    # maistript=numarare(data1,node,'Maistri','Timp partial')
    # print("done",end="\n")
    # totals=conds1+conds2+tesas+maistris+muncitors
    # totalpt=condpt1+condpt2+tesapt+maistript+muncitorpt
    # node_levels.append((node, level, parent, granny,conds1,conds2,tesas,maistris,muncitors,totals,condpt1,condpt2,tesapt,maistript,muncitorpt,totalpt))
    # print("take",end="\n")
    for neighbor in graph.get(node, []):
        neighbor=int(neighbor)
        if neighbor != prev_node:
            if neighbor not in visited and neighbor != first:
                conds1=numarare(data1,node,'Conducere1','Standard')
                print("done",end="\n")
                conds2=numarare(data1,node,'Conducere2','Standard')
                print("done",end="\n")
                maistris=numarare(data1,node,'Maistri','Standard')
                print("done",end="\n")
                tesas=numarare(data1,node,'Tesa','Standard')
                print("done",end="\n")
                muncitors=numarare(data1,node,'Muncitori','Standard')
                print("done",end="\n")
                condpt1=numarare(data1,node,'Conducere1','Timp partial')
                print("done",end="\n")
                condpt2=numarare(data1,node,'Conducere2','Timp partial')
                print("done",end="\n")
                tesapt=numarare(data1,node,'Tesa','Timp partial')
                print("done",end="\n")
                muncitorpt=numarare(data1,node,'Muncitori','Timp partial')
                print("done",end="\n")
                maistript=numarare(data1,node,'Maistri','Timp partial')
                print("done",end="\n")
                totals=conds1+conds2+tesas+maistris+muncitors
                totalpt=condpt1+condpt2+tesapt+maistript+muncitorpt
                node_levels.append((node, level, parent, granny,conds1,conds2,tesas,maistris,muncitors,totals,condpt1,condpt2,tesapt,maistript,muncitorpt,totalpt))
                print("take",end="\n")
                if level <= h:
                    new_granny = -1
                else:
                    new_granny = parent if level == h + 1 else granny
                print("continua centralizare",end="\n")
                centralizare(graph, int(neighbor), first, node_levels, h, level + 1, node, new_granny, visited,node)
    
def sum(node_levels,s_conds1,s_conds2,s_tesas,s_maistris,s_muncitors,s_totals,s_condpt1,s_condpt2,s_tesapt,s_maistrips,s_muncitorpt,s_totalpt,graph, node, first, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    gasit=None
    for n in node_levels:
        if n[0]==node:
            gasit=n
            break
    for neighbor in graph.get(node, []):
        if neighbor not in visited and neighbor != first:
            s_conds1=s_conds1+gasit[4]
            s_conds2=s_conds2+gasit[5]
            s_tesas=s_tesas+gasit[6]
            s_maistris=s_maistris+gasit[7]
            s_muncitors=s_muncitors+gasit[8]
            s_totals=s_totals+gasit[9]
            s_condpt1=s_condpt1+gasit[10]
            s_condpt2=s_condpt2+gasit[11]
            s_tesapt=s_tesapt+gasit[12]
            s_maistrips=s_maistrips+gasit[13]
            s_muncitorpt=s_muncitorpt+gasit[14]
            s_totalpt=s_totalpt+gasit[15]
            sum(node_levels,s_conds1,s_conds2,s_tesas,s_maistris,s_muncitors,s_totals,s_condpt1,s_condpt2,s_tesapt,s_maistrips,s_muncitorpt,s_totalpt, neighbor, first, visited)
    return s_conds1,s_conds2,s_tesas,s_maistris,s_muncitors,s_totals,s_condpt1,s_condpt2,s_tesapt,s_maistrips,s_muncitorpt,s_totalpt

