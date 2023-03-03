def smallest_dominating_set(adj_list):
   
    dominating_set = set()
  
    uncovered = set(adj_list.keys())
    while uncovered:
        
        best_vertex = None
        best_cover = set()
        for vertex in adj_list.keys():
            if vertex not in dominating_set:
                cover = set(adj_list[vertex]) & uncovered
                if len(cover) > len(best_cover):
                    best_vertex = vertex
                    best_cover = cover
       
        dominating_set.add(best_vertex)
        uncovered -= best_cover | {best_vertex}
    return dominating_set
adj_list = {
  0: [1, 2],
  1: [0, 2, 3],
  2: [0, 1, 3],
  3: [1, 2]
}
dominating_set = smallest_dominating_set(adj_list)
print(dominating_set)
