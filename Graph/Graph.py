from queue import Queue

# Определение класса GraphNode
class GraphNode:
  # Конструктор класса GraphNode
  def __init__(self, id, number, level, p1_score, p2_score):
    # Инициализация свойств узла
    self.id = id
    self.number = number
    self.level = level
    self.p1_score = p1_score
    self.p2_score = p2_score
    self.ChildNodes = []  # Список для хранения дочерних узлов
    self.hashValue = str(p1_score) + str(number) + str(p2_score)

# Определение класса setNode
class setNode:
  def __init__(self, id, hashValue):
    self.id = id
    self.hashValue = hashValue   

# Определение класса Graph
class Graph:
  # Конструктор класса Graph
  def __init__(self):
    self.nodeID = 0
    self.nodes = {}  # Словарь для хранения узлов
    self.levelSet = {
      0:set()
    }

  # Метод для генерации значения узла
  def generateSetValue(self, Graphnode):
    result = str(Graphnode.p1_score) + str(Graphnode.number) + str(Graphnode.p2_score)
    return result

  # Метод для удаления всех узлов из графа
  def deleteGraph(self):
    for key, value in self.nodes.items():
      del self.nodes[key]

  # Метод для добавления узла в граф
  def addNode(self, number, level, p1_score, p2_score, parentID):
    found_existing_node = False
    # Вычисление хэша узла
    hashValue = str(p1_score) + str(number) + str(p2_score)

    # Проверка наличия уровня в графе
    if level not in self.levelSet:
      self.levelSet[level] = set()
    else:
      # Проверка существующих узлов на совпадение хэша
      for node in self.levelSet[level]:
        if hashValue == node.hashValue:
          exNodeID = node.id
          found_existing_node = True
          # Добавление ребра между узлами, если узел уже существует
          self.addEdge(parentID, exNodeID)
          return False
          
    # Если узел не найден, создаем новый
    if not found_existing_node:  
      # Вычисление очков игроков
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

      # Создание нового узла
      self.nodeID += 1    
      self.nodes[self.nodeID] = GraphNode(self.nodeID, number, level, p1_score, p2_score)
      self.addEdge(parentID, self.nodeID)
      # Добавление узла в множество уровня
      self.levelSet[level].add(setNode(self.nodeID, self.generateSetValue(self.nodes[self.nodeID])))

      return True

  # Метод для добавления ребра между узлами в графе
  def addEdge(self, srcID, endID):
    # Добавление узла endID в список дочерних узлов узла srcID
    self.nodes[srcID].ChildNodes.append(self.nodes[endID])

  # Метод для печати всех узлов в графе
  def printNodes(self):
    print("root")
    # Перебор узлов и печать их свойств и дочерних узлов
    for key, value in self.nodes.items():
      print("(", value.p1_score, value.number, value.p2_score, ")")
      for nodes in value.ChildNodes:
        print("(", nodes.p1_score, nodes.number, nodes.p2_score, ")", end=" ")
      print("")

  # Метод для печати уровней графа
  def printLevels(self):
    for key, value in self.levelSet.items():
      for node in value:
        print("(", node.hashValue, ")", end = "")
      print(" ")

  # Метод для генерации графа, начиная с заданного числа
  def generateGraph(self, startNum):
    maxNum = 1000
    # Создание корневого узла и добавление его в очередь
    self.nodes[self.nodeID] = GraphNode(self.nodeID, startNum, 0, 0, 0)
    self.levelSet[0].add(setNode(self.nodes[0].id, self.generateSetValue(self.nodes[0])))

    nQueue = Queue()
    nQueue.put(self.nodes[self.nodeID])

    # Итерация, пока очередь не пуста
    while not nQueue.empty():
      currNode = nQueue.get()
      # Если число текущего узла меньше максимального числа, генерируем дочерние узлы
      if currNode.number < maxNum:
        # Генерация дочерних узлов с разными свойствами
        if self.addNode(currNode.number * 2, currNode.level + 1, currNode.p1_score, currNode.p2_score, currNode.id):
          nQueue.put(self.nodes[self.nodeID])

        if self.addNode(currNode.number * 3, currNode.level + 1, currNode.p1_score, currNode.p2_score, currNode.id):
          nQueue.put(self.nodes[self.nodeID])

