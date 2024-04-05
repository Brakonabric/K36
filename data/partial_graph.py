from queue import Queue


class GraphNode:
    # GraphNode constructor
    def __init__(self, node_id, number, level, p1_score, p2_score):
        self.id = node_id
        self.number = number
        self.level = level
        self.p1_score = p1_score
        self.p2_score = p2_score
        self.ChildNodes = []  # List to store child nodes
        self.hashValue = str(p1_score) + str(number) + str(p2_score)
        self.eval = None
        self.visited_nodes = 0


class SetNode:
    def __init__(self, node_id, hashValue):
        self.id = node_id
        self.hashValue = hashValue


class Graph:
    # Graph constructor
    def __init__(self):
        self.nodeID = 0
        self.nodes = {}  # Dictionary to store nodes
        self.levelSet = {
            0: set()
        }
        self.visited_nodes_count = 0
        self.found_existing_node = False

    @staticmethod
    def generate_set_value(graph_node):
        result = str(graph_node.p1_score) + str(graph_node.number) + str(graph_node.p2_score)
        return result

    # Method to delete all nodes from the graph
    def delete_graph(self):
        for key, value in self.nodes.items():
            del self.nodes[key]

    # Method to add a node to the graph

    def add_node(self, number, level, p1_score, p2_score, parentID):
        self.found_existing_node = False
        if level % 2 != 0:
            if number % 2 == 0:
                p1_score += 1
            else:
                p1_score -= 1
        else:
            if number % 2 == 0:
                p2_score += 1
            else:
                p2_score -= 1
        hash_value = str(p1_score) + str(number) + str(p2_score)

        if level not in self.levelSet:
            self.levelSet[level] = set()
        else:
            for node in self.levelSet[level]:
                if hash_value == node.hashValue:
                    ex_node_id = node.id
                    self.found_existing_node = True
                    self.add_edge(parentID, ex_node_id)
                    return False

        if not self.found_existing_node:
            self.nodeID += 1
            self.nodes[self.nodeID] = GraphNode(self.nodeID, number, level, p1_score, p2_score)
            self.add_edge(parentID, self.nodeID)
            self.levelSet[level].add(SetNode(self.nodeID, self.generate_set_value(self.nodes[self.nodeID])))

            return True

    # Method to add an edge between two nodes in the graph
    def add_edge(self, srcID, endID):
        # Add endID node to the ChildNodes list of srcID node
        self.nodes[srcID].ChildNodes.append(self.nodes[endID])

    # Method to print all nodes in the graph
    def print_nodes(self):
        print("root")
        # Iterate over nodes and print their properties and child nodes
        for key, value in self.nodes.items():
            print("(", value.id, " ", value.p1_score, value.number, value.p2_score, value.eval, ")")
            for nodes in value.ChildNodes:
                print("(", nodes.id, " ", nodes.p1_score, nodes.number, nodes.p2_score, nodes.eval, ")", end=" ")
            print("")
            print("")

    # Method to generate the graph starting from a given number
    def generate_graph(self, startNum, p1_score, p2_score):
        max_level = 4
        max_num = 1000
        # Create the root node and add it to the queue
        self.nodes[self.nodeID] = GraphNode(self.nodeID, startNum, 0, p1_score, p2_score)
        self.levelSet[0].add(SetNode(self.nodes[0].id, self.generate_set_value(self.nodes[0])))

        n_queue = Queue()
        n_queue.put(self.nodes[self.nodeID])

        # Iterate until the queue is empty
        while not n_queue.empty():
            curr_node = n_queue.get()
            # If the current node's number is less than max_num, generate child nodes

            if curr_node.level < max_level and curr_node.number < max_num:
                # Generate child nodes with different properties

                if self.add_node(curr_node.number * 2, curr_node.level + 1, curr_node.p1_score, curr_node.p2_score,
                                 curr_node.id):
                    n_queue.put(self.nodes[self.nodeID])

                if self.add_node(curr_node.number * 3, curr_node.level + 1, curr_node.p1_score, curr_node.p2_score,
                                 curr_node.id):
                    n_queue.put(self.nodes[self.nodeID])

    def minimax_eval(self, node, maximizingPlayer):
        self.visited_nodes_count += 1
        if not node.ChildNodes:
            return node.eval

        if maximizingPlayer:
            max_eval = float('-inf')
            for child_node in node.ChildNodes:
                child_node.eval = self.minimax_eval(child_node, False)
                max_eval = max(max_eval, child_node.eval)
            node.eval = max_eval
            return max_eval
        else:
            min_eval = float('inf')
            for child_node in node.ChildNodes:
                child_node.eval = self.minimax_eval(child_node, True)
                min_eval = min(min_eval, child_node.eval)
            node.eval = min_eval
            return min_eval

    def heuristic(self):
        for key, value in self.nodes.items():
            if not value.ChildNodes:
                value.eval = value.p2_score - value.p1_score

    def alfa_beta_eval(self, node, alpha, beta, maximizingPlayer):
        self.visited_nodes_count += 1
        if not node.ChildNodes:
            return node.eval

        if maximizingPlayer:
            max_eval = float('-inf')
            for child_node in node.ChildNodes:
                child_eval = self.alfa_beta_eval(child_node, alpha, beta, False)
                max_eval = max(max_eval, child_eval)
                alpha = max(alpha, max_eval)
                if beta <= alpha:
                    break
            node.eval = max_eval
            return max_eval
        else:
            min_eval = float('inf')
            for child_node in node.ChildNodes:
                child_eval = self.alfa_beta_eval(child_node, alpha, beta, True)
                min_eval = min(min_eval, child_eval)
                beta = min(beta, min_eval)
                if beta <= alpha:
                    break
            node.eval = min_eval
            return min_eval

    def choose_best_child(self):
        valid_children = [child for child in self.nodes[0].ChildNodes if child.eval is not None]
        if not valid_children:
            return None
        best_child = max(valid_children, key=lambda x: x.eval)
        return best_child


def minimax(startNum, p1_score, p2_score):
    graph = Graph()
    graph.generate_graph(startNum, p1_score, p2_score)
    graph.heuristic()
    graph.minimax_eval(graph.nodes[0], True)
    graph.print_nodes()
    best_child = graph.choose_best_child()
    best_child.visited_nodes = graph.visited_nodes_count
    return best_child


def alphabeta(startNum, p1_score, p2_score):
    graph = Graph()
    graph.generate_graph(startNum, p1_score, p2_score)
    graph.heuristic()
    graph.alfa_beta_eval(graph.nodes[0], float('-inf'), float('inf'), True)
    graph.print_nodes()
    best_child = graph.choose_best_child()
    best_child.visited_nodes = graph.visited_nodes_count
    return best_child
