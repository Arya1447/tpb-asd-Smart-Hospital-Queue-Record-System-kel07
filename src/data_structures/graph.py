class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, asal, tujuan):

        if asal not in self.graph:
            self.graph[asal] = []

        self.graph[asal].append(tujuan)

    def tampilkan_graph(self):

        print('\n=== GRAPH RUJUKAN POLI ===')

        for poli in self.graph:

            print(
                poli,
                '->',
                self.graph[poli]
            )

    def bfs(self, start):

        visited = []
        queue = []

        visited.append(start)
        queue.append(start)

        print('\nBFS Traversal:')

        while queue:

            node = queue.pop(0)

            print(node)

            for tetangga in self.graph.get(node, []):

                if tetangga not in visited:

                    visited.append(tetangga)
                    queue.append(tetangga)