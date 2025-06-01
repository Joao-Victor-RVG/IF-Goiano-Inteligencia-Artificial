class Node:
    def __init__(self, node_id):
        self.node_id = node_id

class CentralizedController:
    def __init__(self):
        self.nodes = []

    def register_node(self, node):
        self.nodes.append(node)
        print(f"Nó {node.node_id} registrado.")

    def elect_leader(self):
        if not self.nodes:
            print("Nenhum nó registrado.")
            return None
        leader = max(self.nodes, key=lambda n: n.node_id)
        print(f"Nó eleito como líder: {leader.node_id}")
        return leader

# Simulação
controller = CentralizedController()
controller.register_node(Node(1))
controller.register_node(Node(3))
controller.register_node(Node(2))

leader = controller.elect_leader()


