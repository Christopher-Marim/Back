from src.Domain.Exceptions import EmptyBorder
from src.Domain.Node import Node
from src.Domain.Search import Search


class DFS(Search):
    def search(self) -> list[Node]:  # busca padrao em grafo
        while True:
            if not self.border:
                raise EmptyBorder
            current = self.border.pop()
            self.explored[(current.x, current.y)] = current
            self.path.append(current)
            if current in self.destiny:
                return self.path
            for adj in self.graph.adj[current]:
                if (adj.x, adj.y) not in self.explored and adj not in self.border:
                    self.border.append(adj)
