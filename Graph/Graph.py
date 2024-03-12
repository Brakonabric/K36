from queue import Queue


class GraphNode:
  # GraphNode constructor
  def __init__(self, id, number, level, p1_score, p2_score):
    self.id = id
    self.number = number
    self.level = level
    self.p1_score = p1_score
    self.p2_score = p2_score
    self.ChildNodes = []  # List to store child nodes


class Graph:
  # Graph constructor
  def __init__(self):
    self.nodes = {}  # Dictionary to store nodes

  # Method to delete all nodes from the graph
  def deleteGraph(self):
    for key, value in self.nodes.items():
      del self.nodes[key]

  # Method to add a node to the graph
  def addNode(self, id, number, level, p1_score, p2_score):
    # Adjust player scores based on node properties
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
    # Create a new GraphNode and add it to the dictionary
    self.nodes[id] = GraphNode(id, number, level, p1_score, p2_score)

  # Method to add an edge between two nodes in the graph
  def addEdge(self, srcID, endID):
    # Add endID node to the ChildNodes list of srcID node
    self.nodes[srcID].ChildNodes.append(self.nodes[endID])

  # Method to print all nodes in the graph
  def printNodes(self):
    print("root")
    # Iterate over nodes and print their properties and child nodes
    for key, value in self.nodes.items():
      print("(", value.p1_score, value.number, value.p2_score, ")")
      for nodes in value.ChildNodes:
        print("(", nodes.p1_score, nodes.number, nodes.p2_score, ")", end=" ")
      print("")

  # Method to generate the graph starting from a given number
  def generateGraph(self, startNum):
    maxNum = 1000
    nodeID = 0
    # Create the root node and add it to the queue
    self.nodes[nodeID] = GraphNode(nodeID, startNum, 0, 0, 0)
    nQueue = Queue()
    nQueue.put(self.nodes[nodeID])

    # Iterate until the queue is empty
    while not nQueue.empty():
      currNode = nQueue.get()
      # If the current node's number is less than maxNum, generate child nodes
      if currNode.number < maxNum:
        # Generate child nodes with different properties
        self.addNode(nodeID + 1, currNode.number * 2, currNode.level + 1,
                     currNode.p1_score, currNode.p2_score)
        nQueue.put(self.nodes[nodeID + 1])

        self.addNode(nodeID + 2, currNode.number * 3, currNode.level + 1,
                     currNode.p1_score, currNode.p2_score)
        nQueue.put(self.nodes[nodeID + 2])

        # Add edges between the current node and its child nodes
        self.addEdge(currNode.id, nodeID + 1)
        self.addEdge(currNode.id, nodeID + 2)
        nodeID += 2  # Increment nodeID for the next pair of child nodes
