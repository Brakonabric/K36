from queue import Queue


class GraphNode:
    # GraphNode constructor
    def __init__(self, node_id, number, level, p1_score, p2_score):
        self.id = node_id # identifikators katrai virsotnei
        self.number = number # skaitli virsotnei
        self.level = level # līmenis katrai virsotnei
        self.p1_score = p1_score # pirmā spēlētāja punkti
        self.p2_score = p2_score # otrā spēlētāja punkti
        self.ChildNodes = []  # Saraksts virsotnes glabāšanai (bērni)
        self.hashValue = str(p1_score) + str(number) + str(p2_score)
        self.eval = None
        self.visited_nodes = 0


class SetNode:
    def __init__(self, node_id, hashValue):
        self.id = node_id # identifikacijas numuru pievienošana
        self.hashValue = hashValue # hešvērtības pievienošana


class Graph:
    # Graph constructor
    def __init__(self):
        self.nodeID = 0 
        self.nodes = {}  # Virsotnes vārdnīca 
        self.levelSet = {
            0: set() #glāba virsotnes un virsotņu kopas
        }
        self.visited_nodes_count = 0
        self.found_existing_node = False

    @staticmethod
    def generate_set_value(graph_node):
        result = str(graph_node.p1_score) + str(graph_node.number) + str(graph_node.p2_score)
        return result

    # Metode visu mezglu dzēšanai
    def delete_graph(self):
        for key, value in self.nodes.items():
            del self.nodes[key]

    # Metode, lai pievienotu jaunu virsotni
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

    # Metode, lai pievienotu saiti starp diviem virsotnem
    def add_edge(self, srcID, endID):
        # Pievienojiet endID virsotni srcID virsotnes ChildNodes sarakstam

        self.nodes[srcID].ChildNodes.append(self.nodes[endID])

    # metode, kas printē visas virsotnes ekrānā
    def print_nodes(self):
        print("root")
        # Printēt virsotnes ar vērtībām 
        for key, value in self.nodes.items():
            print("(", value.id, " ", value.p1_score, value.number, value.p2_score, value.eval, ")")
            for nodes in value.ChildNodes:
                print("(", nodes.id, " ", nodes.p1_score, nodes.number, nodes.p2_score, nodes.eval, ")", end=" ")
            print("")
            print("")

    # Metode, lai ģenerētu grafu
    def generate_graph(self, startNum, p1_score, p2_score):
        max_level = 4 
        max_num = 1000 # skaitlis, kur beidzas spēle
        # Izveidojiet virostni un pievienojiet to rindai
        self.nodes[self.nodeID] = GraphNode(self.nodeID, startNum, 0, p1_score, p2_score)
        self.levelSet[0].add(SetNode(self.nodes[0].id, self.generate_set_value(self.nodes[0])))

        n_queue = Queue()
        n_queue.put(self.nodes[self.nodeID])

        # Atkārtojiet, kamēr rinda nav tukša
        while not n_queue.empty():
            curr_node = n_queue.get()

            # Ja virsotnes numurs ir mazāks par max_num, ģenerējiet bērnu virsotni
            if curr_node.level < max_level and curr_node.number < max_num:
                
                # Ģenerējiet bērnu visrsotni
                if self.add_node(curr_node.number * 2, curr_node.level + 1, curr_node.p1_score, curr_node.p2_score,
                                 curr_node.id):
                    n_queue.put(self.nodes[self.nodeID])

                if self.add_node(curr_node.number * 3, curr_node.level + 1, curr_node.p1_score, curr_node.p2_score,
                                 curr_node.id):
                    n_queue.put(self.nodes[self.nodeID])

    def minimax_eval(self, node, maximizingPlayer): #rekursīva funkcija, kas pēc minimaksa algoritma katrai virsotnei piešķir heiristisko vertējumu
        self.visited_nodes_count += 1 #izseko cik virsotnes bija apmeklētas
        if not node.ChildNodes: #ja virsotnei nav bērnu(strupceļa virsotne), tad funkcija atgriež šīs virsotnes heiristisko vērtējumu
            return node.eval

        if maximizingPlayer: #ja spēlētājs, kuram jāizdara gājiens, ir maksimizējošais spēlētājs(virsotne atrodas Max līmenī)
            max_eval = float('-inf') #minimāli iespējamā vērtība
            #funkcija izvēlas maksimālo vērtību no pieejamajiem bērnu virsotnēm un atgriež šo vērtību
            for child_node in node.ChildNodes:
                child_node.eval = self.minimax_eval(child_node, False) #ja virsone nav strupceļa virsotne, uz to bērniem tiek pielietots minimaks, pieņēmot, ka tie atrodas Min līmenī
                max_eval = max(max_eval, child_node.eval)
            node.eval = max_eval
            return max_eval
        else: #ja spēlētājs, kuram jāizdara gājiens, ir minimizējošais spēlētājs(virsotne atrodas Min līmenī)
            min_eval = float('inf') #maksimāli iespējamā vērtība
            # funkcija izvēlas minimālo vērtību no pieejamajiem bērnu virsotnēm un atgriež šo vērtību
            for child_node in node.ChildNodes:
                child_node.eval = self.minimax_eval(child_node, True) #ja virsone nav strupceļa virsotne, uz to bērniem tiek pielietots minimaks, pieņēmot, ka tie atrodas Max līmenī
                min_eval = min(min_eval, child_node.eval)
            node.eval = min_eval
            return min_eval

    def heuristic(self): # visiem strupceļa virsotnēm piešķir heiristisko vērtējumu, kas ir vienāda ar 2. un 1. spēlētāja punktu starpību
        for key, value in self.nodes.items():
            if not value.ChildNodes:
                value.eval = value.p2_score - value.p1_score

    def alfa_beta_eval(self, node, alpha, beta, maximizingPlayer): #rekursīva funkcija, kas pēc alfa-beta algoritma katrai virsotnei piešķir heiristisko vertējumu
        self.visited_nodes_count += 1 #izseko cik virsotnes bija apmeklētas
        if not node.ChildNodes: #ja ir sasniegta strupceļa virsotne, funkcija atgriež tās heiristisko vertējumu
            return node.eval

        if maximizingPlayer: #ja spēlētājs, kuram jāizdara gājiens, ir maksimizējošais spēlētājs(virsotne atrodas Max līmenī)
            max_eval = float('-inf')#minimāli iespējamā vērtība
            # funkcija izvēlas maksimālo vērtību no pieejamajiem bērnu virsotnēm un atgriež šo vērtību
            for child_node in node.ChildNodes:
                child_eval = self.alfa_beta_eval(child_node, alpha, beta, False) #ja virsone nav strupceļa virsotne, uz to bērniem tiek pielietota alfa-beta, pieņēmot, ka tie atrodas Min līmenī
                max_eval = max(max_eval, child_eval)
                alpha = max(alpha, max_eval) # labākā (lielākā) vērtība, ko maksimizējošais spēlētājs varētu sasniegt šajā līmenī
                #ja kāda bērnu virsotne sasniedz vērtību, kas lielāka par alfa vērtību, tad alfa vērtība tiek atjaunināta uz šo lielāko vērtību

                #  ja kāda bērnu virsotne sasniedz vērtību, kas ir lielāka par beta vērtību, tad zemākās līmeņa virsotnes, kas nav jau pārbaudītas, netiek izpētītas, jo tie neietekmēs gājiena izvēli, tāpēc tiek pārtraukta turpmāka izpēte šajā virzienā
                if beta <= alpha:
                    break
            node.eval = max_eval
            return max_eval
        else: #ja spēlētājs, kuram jāizdara gājiens, ir minimizējošais spēlētājs(virsotne atrodas Min līmenī)
            min_eval = float('inf') #maksimāli iespējamā vērtība
            #funkcija izvēlas minimālo vērtību no pieejamajiem bērnu virsotnēm un atgriež šo vērtību
            for child_node in node.ChildNodes: 
                child_eval = self.alfa_beta_eval(child_node, alpha, beta, True) #ja virsone nav strupceļa virsotne, uz to bērniem tiek pielietota alfa-beta, pieņēmot, ka tie atrodas Max līmenī
                min_eval = min(min_eval, child_eval)
                beta = min(beta, min_eval) #labākā (mazākā) vērtība, ko minimizējošais spēlētājs varētu sasniegt šajā līmenī
                #ja kāda bērnu virsotne sasniedz vērtību, kas mazāka par beta vērtību, tad beta vērtība tiek atjaunināta uz šo mazāko vērtību
                
                #ja kāda bērnu virsotne sasniedz vērtību, kas ir lielāka par beta vērtību, tad zemākās līmeņa virsotnes, kas nav jau pārbaudītas, netiek izpētītas, jo tie neietekmēs gājiena izvēli, tāpēc tiek pārtraukta turpmāka izpēte šajā virzienā
                if beta <= alpha:
                    break
            node.eval = min_eval
            return min_eval

    def choose_best_child(self): # funkcija kas izvēlas nākamo gajiēnu kā virsotni ar lielāko heiristisko vērtējumu
        valid_children = [child for child in self.nodes[0].ChildNodes if child.eval is not None]
        if not valid_children: #ja nevienai virsotnei nav heiristisko vertējumu, funkcija atgriež None
            return None
        best_child = max(valid_children, key=lambda x: x.eval)
        return best_child


def minimax(startNum, p1_score, p2_score): #funkciija, kas izpilda alfa-beta algoritmu un izpilda gājienu
    graph = Graph()
    graph.generate_graph(startNum, p1_score, p2_score) #funkcija ģenerē grāfa daļu no uzdotas virsotnes
    graph.heuristic() #funkcija piešķir strupceļa virsotnem heiristiskus vertējumus
    graph.minimax_eval(graph.nodes[0], True) #funkcija pēc minimaksa algoritma katrai virsotnei piešķir heiristiskus vertējumus
    graph.print_nodes() #izvada virsotnes konsolī
    best_child = graph.choose_best_child() #funkcija izvēlas nākamo gajiēnu kā virsotni ar lielāko heiristisko vērtējumu
    best_child.visited_nodes = graph.visited_nodes_count #funkcija piešķir šai virsotnei apmēklēto virsotņu skaitu, lai pēc tām to varētu izvadīt
    return best_child


def alphabeta(startNum, p1_score, p2_score): #funkciija, kas izpilda alfa-beta algoritmu un izpilda gājienu
    graph = Graph()
    graph.generate_graph(startNum, p1_score, p2_score) #funkcija ģenerē grāfa daļu no uzdotas virsotnes
    graph.heuristic() #funkcija piešķir strupceļa virsotnem heiristiskus vertējumus
    graph.alfa_beta_eval(graph.nodes[0], float('-inf'), float('inf'), True) #funkcija pēc alfa-beta algoritma katrai virsotnei piešķir heiristiskus vertējumus
    graph.print_nodes() #izvada virsotnes konsolī
    best_child = graph.choose_best_child() #funkcija izvēlas nākamo gajiēnu kā virsotni ar lielāko heiristisko vērtējumu
    best_child.visited_nodes = graph.visited_nodes_count #funkcija piešķir šai virsotnei apmēklēto virsotņu skaitu, lai pēc tām to varētu izvadīt
    return best_child
