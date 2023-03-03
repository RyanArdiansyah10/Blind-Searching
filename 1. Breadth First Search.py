def bfs (graph, source):
    visited = set() # trak node yang sudah dikunjungi
    bfs_traversal = list() # hasil dari bfs
    queue = list()
    
    # masukan root node ke antrian dan tandai node tersebut sudah dikunjungi
    queue.append(source)
    visited.add(source)
    
    # lakukan perulangan hingga antrian kosong
    while queue:
        # keluarkan node dari depan antrian dan masukan kedalam bfs_traversal
        current_node = queue.pop(0)
        bfs_traversal.append(current_node)
        
        # lakukan pengecekan semua node terdekat dari current_node
        for neightbourd_node in graph[current_node]:
            # jika node tetangga belum dikunjungi, masukan kedalam antrian dan tandai sudah dikunjungi
            if neightbourd_node not in visited:
                queue.append(neightbourd_node)
                visited.add(neightbourd_node)
                
    return bfs_traversal
def main():
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C'],
        'G': ['C']
    }
    
    bfs_traversal = bfs(graph, 'A')
    print(f"BFS: {bfs_traversal}")
    
if __name__=='__main__':
    main()
                