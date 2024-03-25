

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
    self.hashValue = str(p1_score) + str(number) + str(p2_score)
    self.eval = 2


class setNode:
  def __init__(self, id, hashValue):
    self.id = id
    self.hashValue = hashValue


class Graph:
  # Graph constructor
  def __init__(self):
    self.nodeID = 0
    self.nodes = {}  # Dictionary to store nodes
    self.levelSet = {
      0: set()
    }

  def generateSetValue(self, Graphnode):
    result = str(Graphnode.p1_score) + str(Graphnode.number) + str(Graphnode.p2_score)
    return result

  # Method to delete all nodes from the graph
  def deleteGraph(self):
    for key, value in self.nodes.items():
      del self.nodes[key]

  # Method to add a node to the graph

  def addNode(self, number, level, p1_score, p2_score, parentID):
    found_existing_node = False
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
    hashValue = str(p1_score) + str(number) + str(p2_score)

    if level not in self.levelSet:
      self.levelSet[level] = set()
    else:
      for node in self.levelSet[level]:
        if hashValue == node.hashValue:
          exNodeID = node.id
          found_existing_node = True
          self.addEdge(parentID, exNodeID)
          return False

    if not found_existing_node:
      self.nodeID += 1
      self.nodes[self.nodeID] = GraphNode(self.nodeID, number, level, p1_score, p2_score)
      self.addEdge(parentID, self.nodeID)
      self.levelSet[level].add(setNode(self.nodeID, self.generateSetValue(self.nodes[self.nodeID])))

      return True

  # Method to add an edge between two nodes in the graph
  def addEdge(self, srcID, endID):
    # Add endID node to the ChildNodes list of srcID node
    self.nodes[srcID].ChildNodes.append(self.nodes[endID])

  # Method to print all nodes in the graph
  def printNodes(self):
    print("root")
    # Iterate over nodes and print their properties and child nodes
    for key, value in self.nodes.items():
      print("(", value.id, " ", value.p1_score, value.number, value.p2_score, value.eval, ")")
      for nodes in value.ChildNodes:
        print("(", nodes.id, " ", nodes.p1_score, nodes.number, nodes.p2_score, nodes.eval, ")", end=" ")
      print("")
      print("")

  # Method to generate the graph starting from a given number
  def generateGraph(self, startNum):
    maxNum = 1000
    # Create the root node and add it to the queue
    self.nodes[self.nodeID] = GraphNode(self.nodeID, startNum, 0, 0, 0)
    self.levelSet[0].add(setNode(self.nodes[0].id, self.generateSetValue(self.nodes[0])))

    nQueue = Queue()
    nQueue.put(self.nodes[self.nodeID])

    # Iterate until the queue is empty
    while not nQueue.empty():
      currNode = nQueue.get()
      # If the current node's number is less than maxNum, generate child nodes
      if currNode.number < maxNum:
        # Generate child nodes with different properties

        if self.addNode(currNode.number * 2, currNode.level + 1, currNode.p1_score, currNode.p2_score, currNode.id):
          nQueue.put(self.nodes[self.nodeID])

        if self.addNode(currNode.number * 3, currNode.level + 1, currNode.p1_score, currNode.p2_score, currNode.id):
          nQueue.put(self.nodes[self.nodeID])

  def printLevels(self):
    for key, value in self.levelSet.items():
      for node in value:
        print("(", node.hashValue, ")", end="")
      print("////////////////////////////////")

  def startEval(self):
    for key, value in self.nodes.items():
      if not value.ChildNodes:
        if value.p1_score > value.p2_score:
          value.eval = -1
        elif value.p1_score == value.p2_score:
          value.eval = 0
        else:
          value.eval = 1

  def minimaxEval(self, node):
    if not node.ChildNodes:
      return node.eval

    if node.level % 2 == 1:
      maxEval = float('-inf')
      for child_node in node.ChildNodes:
        child_node.eval = self.minimaxEval(child_node)
        maxEval = max(maxEval, child_node.eval)
      node.eval = maxEval
      return maxEval
    else:
      minEval = float('inf')
      for child_node in node.ChildNodes:
        child_node.eval = self.minimaxEval(child_node)
        minEval = min(minEval, child_node.eval)
      node.eval = minEval
      return minEval



graph = Graph()
graph.generateGraph(15)
graph.startEval()
graph.minimaxEval(graph.nodes[0])
graph.printNodes()
# graph.printLevels()
