"""
Skeleton code for Project 1 of Columbia University's AI EdX course (8-puzzle).
Python 3
"""

import queue as Q

import resource

import sys

import math

import time

start_time, end_time = 0.0, 0.0


#### SKELETON CODE ####

## The Class that Represents the Puzzle


class PuzzleState(object):
    """docstring for PuzzleState"""

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


# Function that Writes to output.txt

### Students need to change the method to have the corresponding parameters

# noinspection PyPep8Naming
def writeOutput(goal, nodes_expanded, max_depth):
    ### Student Code Goes here
    ans = []
    while (goal.parent is not None):
        ans.append(goal.action)
        goal = goal.parent
    end_time = time.time()
    f = open("output.txt", "w+")
    f.write("path_to_goal: " + str(list(reversed(ans))) + \
            "\ncost_of_path: " + str(len(ans)) + \
            "\nnodes_expanded: " + str(nodes_expanded) + \
            "\nsearch_depth: " + str(len(ans)) + \
            "\nmax_search_depth: " + str(max_depth) + \
            "\nrunning_time: " + str(end_time - start_time) + \
            "\nmax_ram_usage: " + str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
    f.close()


def bfs_search(initial_state):
    """BFS search"""
    ### STUDENT CODE GOES HERE ###
    frontier = [initial_state]
    nodes_expanded = -1
    frontier_configs = [initial_state.config]
    explored = []
    max_depth = 0
    while (len(frontier) != 0):
        state = frontier.pop(0)
        explored.append(state.config)
        # print(state.display())
        nodes_expanded += 1
        # print(nodes_expanded)
        if (test_goal(state)):
            writeOutput(state, nodes_expanded, max_depth)
            break
        for neighbor in state.expand():
            if not (neighbor.config in frontier_configs or neighbor.config in explored):
                frontier.append(neighbor)
                frontier_configs.append(neighbor.config)
                max_depth = max(max_depth, neighbor.cost)


def dfs_search(initial_state):
    """DFS search"""

    ### STUDENT CODE GOES HERE ###
    frontier = [initial_state]
    nodes_expanded = -1
    frontier_configs = set(initial_state.config)
    explored = set()
    max_depth = 0
    while (len(frontier) != 0):
        state = frontier.pop(frontier.__len__() - 1)
        explored.add(state.config)
        # print(state.display())
        nodes_expanded += 1
        print(nodes_expanded)
        if (test_goal(state)):
            writeOutput(state, nodes_expanded, max_depth)
            break
        for neighbor in reversed(state.expand()):
            if not (neighbor.config in frontier_configs or neighbor.config in explored):
                frontier.append(neighbor)
                frontier_configs.add(neighbor.config)
                max_depth = max(max_depth, neighbor.cost)


def A_star_search(initial_state):
    """A * search"""

    ### STUDENT CODE GOES HERE ###


def calculate_total_cost(state):
    """calculate the total estimated cost of a state"""

    ### STUDENT CODE GOES HERE ###


def calculate_manhattan_dist(idx, value, n):
    """calculate the manhattan distance of a tile"""

    ### STUDENT CODE GOES HERE ###


def test_goal(puzzle_state):
    """test the state is the goal state or not"""

    ### STUDENT CODE GOES HERE ###
    return puzzle_state.config == tuple([0]).__add__(tuple(range(1, puzzle_state.n * puzzle_state.n)))


# Main Function that reads in Input and Runs corresponding Algorithm

def main():
    start_time = time.time()
    sm = sys.argv[1].lower()

    begin_state = sys.argv[2].split(",")

    begin_state = tuple(map(int, begin_state))

    size = int(math.sqrt(len(begin_state)))

    hard_state = PuzzleState(begin_state, size)

    if sm == "bfs":

        bfs_search(hard_state)

    elif sm == "dfs":

        dfs_search(hard_state)

    elif sm == "ast":

        A_star_search(hard_state)

    else:

        print("Enter valid command arguments !")


if __name__ == '__main__':
    main()