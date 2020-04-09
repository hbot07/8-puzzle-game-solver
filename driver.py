import resource

import sys

import math

import heapq

import time

start_time, end_time = 0.0, 0.0

class PuzzleState(object):

    def __init__(self, config, n, parent=None, action="Initial", cost=0):

        if n * n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")

        self.n = n

        self.cost = cost

        self.parent = parent

        self.action = action

        self.dimension = n

        self.config = config

        self.children = []

        for i, item in enumerate(self.config):

            if item == 0:
                self.blank_row = i // self.n

                self.blank_col = i % self.n

                break

    def display(self):

        for i in range(self.n):

            line = []

            offset = i * self.n

            for j in range(self.n):
                line.append(self.config[offset + j])

            print(line)

    def move_left(self):

        if self.blank_col == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):

        if self.blank_col == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + 1

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):

        if self.blank_row == 0:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index - self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):

        if self.blank_row == self.n - 1:

            return None

        else:

            blank_index = self.blank_row * self.n + self.blank_col

            target = blank_index + self.n

            new_config = list(self.config)

            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]

            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):

        """expand the node"""

        # add child nodes in order of UDLR

        if len(self.children) == 0:

            up_child = self.move_up()

            if up_child is not None:
                self.children.append(up_child)

            down_child = self.move_down()

            if down_child is not None:
                self.children.append(down_child)

            left_child = self.move_left()

            if left_child is not None:
                self.children.append(left_child)

            right_child = self.move_right()

            if right_child is not None:
                self.children.append(right_child)

        return self.children
    
    def __lt__(self, other):
        return calculate_total_cost(self) < calculate_total_cost(other)

def writeOutput(goal, nodes_expanded, max_depth):
    ans = []
    while (goal.parent is not None):
        ans.append(goal.action)
        goal = goal.parent
    end_time = time.time()
    print("Moves: " + str(list(reversed(ans))) + \
            "\nNumber of Moves: " + str(len(ans)))

                
def A_star_search(initial_state):
    frontier = [initial_state]
    heapq.heapify(frontier)
    nodes_expanded = -1
    frontier_configs = set(initial_state.config)
    explored = set()
    max_depth = 0
    while (len(frontier) != 0):
        state = heapq.heappop(frontier)
        explored.add(state.config)
        # state.display()
        nodes_expanded += 1
        print(nodes_expanded)
        if (test_goal(state)):
            writeOutput(state, nodes_expanded, max_depth)
            break
        for neighbor in reversed(state.expand()):
            if not (neighbor.config in frontier_configs or neighbor.config in explored):
                heapq.heappush(frontier, neighbor)
                frontier_configs.add(neighbor.config)
                max_depth = max(max_depth, neighbor.cost)


def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""

    sum = 0
    for i in range(0, len(state.config)):
        sum += calculate_manhattan_dist(i, state.config[i], math.sqrt(len(state.config)))
    return sum + state.cost


def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""

    return math.fabs(value // n - idx // n) + math.fabs(value % n - idx % n)
                
def test_goal(puzzle_state):
    """test the state is the goal state or not"""
    return puzzle_state.config == tuple(range(1, puzzle_state.n * puzzle_state.n)).__add__(tuple([0]))


# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    begin_state = input("Enter board state \n").split(",")
    start_time = time.time()

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)
    
    A_star_search(hard_state)

if __name__ == '__main__':
    main()
