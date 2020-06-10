import random
import copy


class Node:
    def __init__(self, node_id):
        self.__id = node_id
        self.__color = "uncolored"
        self.__domain = ["red", "blue", "green"]
        self.__neighbors_id = []
        self.__conflicts_id = []
        self.__neighbors_number = 0

    def __del__(self):
        del self.__id
        del self.__color
        del self.__domain
        del self.__neighbors_id
        del self.__conflicts_id
        del self.__neighbors_number

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def get_domain_color(self, pos):
        return self.__domain[pos]

    def get_neighbors_number(self):
        return self.__neighbors_number

    def get_conflicts_number(self):
        return len(self.__conflicts_id)

    def get_neighbor_id(self, pos):
        if 0 <= pos < len(self.__neighbors_id):
            return self.__neighbors_id[pos]
        else:
            print("Ooops!!! Something' s wrong!")

    def get_id(self):
        return self.__id

    def get_domain_length(self):
        return len(self.__domain)

    def clean_neighbors(self):
        while len(self.__neighbors_id) > 0:
            self.__neighbors_id.pop()
        self.__neighbors_number = 0

    def clean_conflicts(self):
        while len(self.__conflicts_id) > 0:
            self.__conflicts_id.pop()

    def add_conflict(self, node_id):
        if len(self.__conflicts_id) == 0:
            self.__conflicts_id.append(node_id)
        else:
            check_presence = False
            i = 0
            while i < len(self.__conflicts_id) and not check_presence:
                if node_id == self.__conflicts_id[i]:
                    check_presence = True
                i += 1
            if not check_presence:
                self.__conflicts_id.append(node_id)

    def remove_conflict(self, node_id):
        if len(self.__conflicts_id) != 0:
            removed = False
            i = 0
            while i < len(self.__conflicts_id) and not removed:
                if self.__conflicts_id[i] == node_id:
                    self.__conflicts_id.remove(node_id)
                    removed = True
                i += 1

    def remove_domain_color(self, color):
        if len(self.__domain) != 0:
            i = 0
            removed = False
            while i < len(self.__domain) and not removed:
                if self.__domain[i] == color:
                    self.__domain.remove(color)
                    removed = True
                i += 1

    def add_domain_color(self, color):
        if len(self.__domain) != 0:
            i = 0
            color_presence = False
            while i < len(self.__domain) and not color_presence:
                if self.__domain[i] == color:
                    color_presence = True
                i += 1
            if not color_presence:
                self.__domain.append(color)
        else:
            self.__domain.append(color)

    def add_neighbor(self, node_id):
        self.__neighbors_id.append(node_id)
        self.__neighbors_number += 1

    def check_adjacency(self, node_id):
        if len(self.__neighbors_id) == 0:
            return False
        else:
            neighbor = False
            i = 0
            while i < len(self.__neighbors_id) and not neighbor:
                if node_id == self.__neighbors_id[i]:
                    neighbor = True
                i += 1
            return neighbor


class Map:
    def __init__(self, nodes_number, arcs_number_choice):
        self.__nodes = []
        self.__conflict_nodes_id = []
        for i in range(0, nodes_number):
            node = Node(i)
            self.__nodes.append(node)
            self.__conflict_nodes_id.append(node.get_id())
        if (nodes_number % 3) == 0:
            while self.unconnected_components():
                for i in range(0, nodes_number):
                    self.__nodes[i].clean_conflicts()
                    self.__nodes[i].clean_neighbors()
                arcs_number = 0
                if arcs_number_choice == 0:
                    arcs_number = 2 * nodes_number
                elif arcs_number_choice == 1:
                    arcs_number = nodes_number * (nodes_number - 1) // 4
                for j in range(0, arcs_number):
                    first_pos = 0
                    second_pos = 0
                    check_arc_validity = False
                    while not check_arc_validity:
                        first_pos = random.randint(0, nodes_number - 1)
                        if 0 <= first_pos < nodes_number // 3:
                            second_pos = random.randint(nodes_number // 3, nodes_number - 1)
                        elif nodes_number // 3 <= first_pos < 2 * (nodes_number // 3):
                            group_choice = random.randint(0, 1)
                            if group_choice == 0:
                                second_pos = random.randint(0, (nodes_number // 3) - 1)
                            else:
                                second_pos = random.randint(2 * (nodes_number // 3), nodes_number - 1)
                        else:
                            second_pos = random.randint(0, 2 * (nodes_number // 3) - 1)
                        if not self.__nodes[first_pos].check_adjacency(self.__nodes[second_pos].get_id()):
                            check_arc_validity = True
                    self.add_nodes_adjacency(first_pos, second_pos)
        elif (nodes_number % 3) == 1:
            while self.unconnected_components():
                for i in range(0, nodes_number):
                    self.__nodes[i].clean_conflicts()
                    self.__nodes[i].clean_neighbors()
                arcs_number = 0
                if arcs_number_choice == 0:
                    arcs_number = 2 * nodes_number
                elif arcs_number_choice == 1:
                    arcs_number = nodes_number * (nodes_number - 1) // 4
                for j in range(0, arcs_number):
                    first_pos = 0
                    second_pos = 0
                    check_arc_validity = False
                    while not check_arc_validity:
                        first_pos = random.randint(0, nodes_number - 1)
                        if 0 <= first_pos <= nodes_number // 3:
                            second_pos = random.randint((nodes_number // 3) + 1, nodes_number - 1)
                        elif (nodes_number // 3) + 1 <= first_pos <= 2 * (nodes_number // 3):
                            group_choice = random.randint(0, 1)
                            if group_choice == 0:
                                second_pos = random.randint(0, nodes_number // 3)
                            else:
                                second_pos = random.randint(2 * (nodes_number // 3) + 1, nodes_number - 1)
                        else:
                            second_pos = random.randint(0, 2 * (nodes_number // 3))
                        if not self.__nodes[first_pos].check_adjacency(self.__nodes[second_pos].get_id()):
                            check_arc_validity = True
                    self.add_nodes_adjacency(first_pos, second_pos)
        else:
            while self.unconnected_components():
                for i in range(0, nodes_number):
                    self.__nodes[i].clean_conflicts()
                    self.__nodes[i].clean_neighbors()
                arcs_number = 0
                if arcs_number_choice == 0:
                    arcs_number = 2 * nodes_number
                elif arcs_number_choice == 1:
                    arcs_number = nodes_number * (nodes_number - 1) // 4
                for j in range(0, arcs_number):
                    first_pos = 0
                    second_pos = 0
                    check_arc_validity = False
                    while not check_arc_validity:
                        first_pos = random.randint(0, nodes_number - 1)
                        if 0 <= first_pos <= nodes_number // 3:
                            second_pos = random.randint((nodes_number // 3) + 1, nodes_number - 1)
                        elif (nodes_number // 3) + 1 <= first_pos <= 2 * (nodes_number // 3) + 1:
                            group_choice = random.randint(0, 1)
                            if group_choice == 0:
                                second_pos = random.randint(0, nodes_number // 3)
                            else:
                                second_pos = random.randint(2 * (nodes_number // 3) + 2, nodes_number - 1)
                        else:
                            second_pos = random.randint(0, 2 * (nodes_number // 3) + 1)
                        if not self.__nodes[first_pos].check_adjacency(self.__nodes[second_pos].get_id()):
                            check_arc_validity = True
                    self.add_nodes_adjacency(first_pos, second_pos)

    def __del__(self):
        while len(self.__nodes) != 0:
            del self.__nodes[0]
        del self.__nodes
        del self.__conflict_nodes_id

    def unconnected_components(self):
        unconnected_component = False
        i = 0
        while not unconnected_component and i < len(self.__nodes):
            if self.__nodes[i].get_neighbors_number() == 0:
                unconnected_component = True
            i += 1
        return unconnected_component

    def add_nodes_adjacency(self, first_node_pos, second_node_pos):
        self.__nodes[first_node_pos].add_neighbor(self.__nodes[second_node_pos].get_id())
        self.__nodes[second_node_pos].add_neighbor(self.__nodes[first_node_pos].get_id())
        self.check_nodes_conflicts(first_node_pos, second_node_pos)

    def check_nodes_conflicts(self, first_node_pos, second_node_pos):
        if self.__nodes[first_node_pos].get_color() == self.__nodes[second_node_pos].get_color():
            self.__nodes[first_node_pos].add_conflict(self.__nodes[second_node_pos].get_id())
            self.__nodes[second_node_pos].add_conflict(self.__nodes[first_node_pos].get_id())

    def brelaz_initialization(self):
        uncolored_nodes_pos = []
        for i in range(0, len(self.__nodes)):
            uncolored_nodes_pos.append(i)
        while len(uncolored_nodes_pos) > 0:
            if len(uncolored_nodes_pos) == 1:
                self.color_node(uncolored_nodes_pos[0])
                uncolored_nodes_pos.pop()
            else:
                node_choices = []
                min_domain = self.__nodes[uncolored_nodes_pos[0]].get_domain_length()
                node_choices.append(uncolored_nodes_pos[0])
                for i in range(1, len(uncolored_nodes_pos)):
                    actual_node_domain_length = self.__nodes[uncolored_nodes_pos[i]].get_domain_length()
                    if actual_node_domain_length == min_domain:
                        node_choices.append(uncolored_nodes_pos[i])
                    elif actual_node_domain_length < min_domain:
                        while len(node_choices) > 0:
                            node_choices.pop()
                        node_choices.append(uncolored_nodes_pos[i])
                        min_domain = actual_node_domain_length
                if len(node_choices) > 1:
                    actual_choices = []
                    max_degree = self.get_node_submap_degree(node_choices[0])
                    actual_choices.append(node_choices[0])
                    for i in range(1, len(node_choices)):
                        node_submap_degree = self.get_node_submap_degree(node_choices[i])
                        if node_submap_degree == max_degree:
                            actual_choices.append(node_choices[i])
                        elif node_submap_degree > max_degree:
                            while len(actual_choices) > 0:
                                actual_choices.pop()
                            actual_choices.append(node_choices[i])
                            max_degree = node_submap_degree
                    if len(actual_choices) > 1:
                        random_actual_choice_pos = random.randint(0, len(actual_choices) - 1)
                        self.color_node(actual_choices[random_actual_choice_pos])
                        uncolored_nodes_pos.remove(actual_choices[random_actual_choice_pos])
                    else:
                        self.color_node(actual_choices[0])
                        uncolored_nodes_pos.remove(actual_choices[0])
                else:
                    self.color_node(node_choices[0])
                    uncolored_nodes_pos.remove(node_choices[0])

    def color_node(self, node_pos):
        old_color = self.__nodes[node_pos].get_color()
        if self.__nodes[node_pos].get_domain_length() == 0:
            self.__nodes[node_pos].set_color(self.minimizing_conflicts_color(node_pos))
        elif self.__nodes[node_pos].get_domain_length() == 1:
            self.__nodes[node_pos].set_color(self.__nodes[node_pos].get_domain_color(0))
        else:
            color_pos = random.randint(0, self.__nodes[node_pos].get_domain_length() - 1)
            color = self.__nodes[node_pos].get_domain_color(color_pos)
            self.__nodes[node_pos].set_color(color)
        self.update_conflicts(node_pos)
        self.update_neighbors_domains(node_pos, old_color)

    def minimizing_conflicts_color(self, node_pos):
        color_conflicts = [0, 0, 0]
        for i in range(0, self.__nodes[node_pos].get_neighbors_number()):
            neighbor_color = self.__nodes[self.get_node_pos(self.__nodes[node_pos].get_neighbor_id(i))].get_color()
            if neighbor_color == "red":
                color_conflicts[0] += 1
            elif neighbor_color == "blue":
                color_conflicts[1] += 1
            elif neighbor_color == "green":
                color_conflicts[2] += 1
        min_conflicts_number = color_conflicts[0]
        min_conflicts_pos = [0]
        for i in range(1, len(color_conflicts)):
            if color_conflicts[i] == min_conflicts_number:
                min_conflicts_pos.append(i)
            elif color_conflicts[i] < min_conflicts_number:
                min_conflicts_number = color_conflicts[i]
                while len(min_conflicts_pos) != 0:
                    min_conflicts_pos.pop()
                min_conflicts_pos.append(i)
        if len(min_conflicts_pos) > 1:
            color_choice = min_conflicts_pos[random.randint(0, len(min_conflicts_pos) - 1)]
        else:
            color_choice = min_conflicts_pos[0]
        if color_choice == 0:
            return "red"
        elif color_choice == 1:
            return "blue"
        else:
            return "green"

    def get_node_pos(self, node_id):
        i = 0
        node_pos = len(self.__nodes)
        while i < len(self.__nodes) and node_pos == len(self.__nodes):
            if self.__nodes[i].get_id() == node_id:
                node_pos = i
            i += 1
        return node_pos

    def update_conflicts(self, node_pos):
        self.__nodes[node_pos].clean_conflicts()
        node_color = self.__nodes[node_pos].get_color()
        neighbors_not_conflicts = []
        for i in range(0, self.__nodes[node_pos].get_neighbors_number()):
            neighbor_id = self.__nodes[node_pos].get_neighbor_id(i)
            if node_color == self.__nodes[self.get_node_pos(neighbor_id)].get_color():
                self.__nodes[node_pos].add_conflict(neighbor_id)
                self.__nodes[self.get_node_pos(neighbor_id)].add_conflict(self.__nodes[node_pos].get_id())
                self.add_conflict_node(neighbor_id)
            else:
                neighbors_not_conflicts.append(neighbor_id)
        for j in range(0, len(neighbors_not_conflicts)):
            self.__nodes[self.get_node_pos(neighbors_not_conflicts[j])].remove_conflict(self.__nodes[node_pos].get_id())
            if self.__nodes[self.get_node_pos(neighbors_not_conflicts[j])].get_conflicts_number() == 0:
                self.remove_conflict_node(neighbors_not_conflicts[j])
        if self.__nodes[node_pos].get_conflicts_number() == 0:
            self.remove_conflict_node(self.__nodes[node_pos].get_id())
        else:
            self.add_conflict_node(self.__nodes[node_pos].get_id())

    def update_neighbors_domains(self, node_pos, old_color):
        node_color = self.__nodes[node_pos].get_color()
        for i in range(0, self.__nodes[node_pos].get_neighbors_number()):
            neighbor_pos = self.get_node_pos(self.__nodes[node_pos].get_neighbor_id(i))
            self.__nodes[neighbor_pos].remove_domain_color(node_color)
            if old_color != "uncolored":
                j = 0
                old_color_conflict = False
                while j < self.__nodes[neighbor_pos].get_neighbors_number() and not old_color_conflict:
                    if self.__nodes[self.get_node_pos(self.__nodes[neighbor_pos].get_neighbor_id(j))].get_color() == old_color:
                        old_color_conflict = True
                    j += 1
                if not old_color_conflict:
                    self.__nodes[neighbor_pos].add_domain_color(old_color)

    def get_node_submap_degree(self, node_pos):
        colored_neighbors_number = 0
        for i in range(0, self.__nodes[node_pos].get_neighbors_number()):
            if self.__nodes[self.get_node_pos(self.__nodes[node_pos].get_neighbor_id(i))].get_color() != "uncolored":
                colored_neighbors_number = colored_neighbors_number + 1
        return self.__nodes[node_pos].get_neighbors_number() - colored_neighbors_number

    def get_map_conflicts(self):
        return len(self.__conflict_nodes_id)

    def remove_conflict_node(self, node_id):
        if len(self.__conflict_nodes_id) != 0:
            i = 0
            conflict_presence = False
            while i < len(self.__conflict_nodes_id) and not conflict_presence:
                if node_id == self.__conflict_nodes_id[i]:
                    conflict_presence = True
                i += 1
            if conflict_presence:
                self.__conflict_nodes_id.remove(node_id)

    def add_conflict_node(self, node_id):
        if len(self.__conflict_nodes_id) != 0:
            i = 0
            conflict_presence = False
            while i < len(self.__conflict_nodes_id) and not conflict_presence:
                if node_id == self.__conflict_nodes_id[i]:
                    conflict_presence = True
                i += 1
            if not conflict_presence:
                self.__conflict_nodes_id.append(node_id)
        else:
            self.__conflict_nodes_id.append(node_id)

    def get_random_conflict_id(self):
        if len(self.__conflict_nodes_id) != 1:
            return self.__conflict_nodes_id[random.randint(0, len(self.__conflict_nodes_id) - 1)]
        else:
            return self.__conflict_nodes_id[0]

    def check_all_nodes_colored(self):
        valid = True
        i = 0
        while i < len(self.__nodes) and valid:
            if self.__nodes[i].get_color() == "uncolored":
                valid = False
            i += 1
        return valid

    def get_uncolored_node_pos(self):
        uncolored_nodes_pos = []
        for i in range(0, len(self.__nodes)):
            if self.__nodes[i].get_color() == "uncolored":
                uncolored_nodes_pos.append(i)
        return uncolored_nodes_pos[random.randint(0, len(uncolored_nodes_pos) - 1)]


def min_conflicts(csp, max_steps):
    current_conflicts = csp.get_map_conflicts()
    current_csp_state = False
    i = 0
    while i < max_steps and not current_csp_state:
        if current_conflicts != 0:
            conflict_node_id = csp.get_random_conflict_id()
            csp.color_node(csp.get_node_pos(conflict_node_id))
            current_conflicts = csp.get_map_conflicts()
        elif not csp.check_all_nodes_colored():
            csp.color_node(csp.get_uncolored_node_pos())
            current_conflicts = csp.get_map_conflicts()
        if current_conflicts == 0 and csp.check_all_nodes_colored():
            current_csp_state = True
        i += 1
    return i


min_conflicts_choice = int(input("Digit 0 if you want min_conflicts without initialization or 1 if you want min_conflicts with Brelaz initialization:"))
while min_conflicts_choice != 0 and min_conflicts_choice != 1:
    min_conflicts_choice = int(input("Input must be 0 or 1!!! Digit your choice:"))
n = int(input('Insert number of nodes:'))
graph_choice = int(input('Insert 0 for a sparsely-connected graph or 1 for a densely-connected graph:'))
while graph_choice != 0 and graph_choice != 1:
    min_conflicts_choice = int(input("Input must be 0 or 1!!! Digit your choice:"))
n_map = Map(n, graph_choice)
total_iterations = 0
if min_conflicts_choice == 0:
    successes = 0
    for i in range(0, 1000):
        actual_map = copy.deepcopy(n_map)
        actual_iterations = min_conflicts(actual_map, 9 * n)
        if actual_iterations < 9 * n:
            successes += 1
            total_iterations += actual_iterations
        elif actual_iterations == 9 * n and actual_map.get_map_conflicts() == 0 and actual_map.check_all_nodes_colored():
            successes += 1
            total_iterations += actual_iterations
        if i % 100 == 0 and i != 0:
            print("---")
        del actual_map
    if successes != 0 and graph_choice == 0:
        print("Min-conflicts resolves a sparsely-connected map with " + str(n) + " nodes in approximately " + str(total_iterations // successes) + " iterations with resolution probability  " + str(round(successes / 10, 2)) + "%")
    elif successes != 0 and graph_choice == 1:
        print("Min-conflicts resolves a densely-connected map with " + str(n) + " nodes in approximately " + str(total_iterations // successes) + " iterations with resolution probability  " + str(round(successes / 10, 2)) + "%")
    else:
        print("Min-conflicts has never resolved a map with " + str(n) + " nodes")
else:
    successful_initialization = 0
    successful_min_conflicts = 0
    if graph_choice == 0:
        tests_number = 100
    else:
        tests_number = 10
    for i in range(0, tests_number):
        actual_map = copy.deepcopy(n_map)
        actual_map.brelaz_initialization()
        if actual_map.get_map_conflicts() == 0:
            successful_initialization += 1
        else:
            actual_iterations = min_conflicts(actual_map, 9 * n)
            if actual_iterations < 9 * n:
                successful_min_conflicts += 1
                total_iterations += actual_iterations
            elif actual_iterations == 9 * n and actual_map.get_map_conflicts() == 0 and actual_map.check_all_nodes_colored():
                successful_min_conflicts += 1
                total_iterations += actual_iterations
        if graph_choice == 0 and i == 50:
            print("---")
        elif graph_choice == 1 and i == 5:
            print("---")
        del actual_map
    if graph_choice == 0 and successful_initialization != 100:
        if successful_min_conflicts != 0:
            print("Min_conflicts with Brelaz initialization resolves a sparsely-connected map with " + str(n) + " nodes in initialization for " + str(successful_initialization) + "% of cases. In the other cases the resolution probability, after the min_conflicts executions, is " + str(round(successful_min_conflicts / (100 - successful_initialization) * 100, 2)) + "% in approximately " + str(total_iterations // successful_min_conflicts) + " iterations")
        else:
            print("Min_conflicts with Brelaz initialization resolves a sparsely-connected map with " + str(n) + " nodes in initialization for " + str(successful_initialization) + "% of cases. In the other cases the resolution probability, after the min_conflicts executions, is " + str(round(successful_min_conflicts / (100 - successful_initialization) * 100,2)) + "%")
    elif graph_choice == 0 and successful_initialization == 100:
        print("Min_conflicts with Brelaz initialization resolves a sparsely-connected map with " + str(n) + " nodes in initialization for " + str(successful_initialization) + "% of cases")
    elif graph_choice == 1 and successful_initialization != 10:
        if successful_min_conflicts != 0:
            print("Min_conflicts with Brelaz initialization resolves a densely-connected map with " + str(n) + " nodes in initialization for " + str(successful_initialization * 10) + "% of cases. In the other cases the resolution probability, after the min_conflicts executions, is " + str(round(successful_min_conflicts / (10 - successful_initialization) * 100, 2)) + "% in approximately " + str(total_iterations // successful_min_conflicts) + " iterations")
        else:
            print("Min_conflicts with Brelaz initialization resolves a densely-connected map with " + str(n) + " nodes in initialization for " + str(successful_initialization * 10) + "% of cases. In the other cases the resolution probability, after the min_conflicts executions, is " + str(round(successful_min_conflicts / (10 - successful_initialization) * 100,2)) + "%")
    elif graph_choice == 1 and successful_initialization == 10:
        print("Min_conflicts with Brelaz initialization resolves a densely-connected map with " + str(n) + " nodes in initialization for " + str(successful_initialization * 10) + "% of cases")
