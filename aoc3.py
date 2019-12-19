import os

from configs import INPUTS_DIR

class Grid():
    def __init__(self):
        with open(os.path.join(INPUTS_DIR, '3.txt')) as f:
            first_input = f.readline().split(',')
            self.first_snake = Snake(first_input)
            second_input = f.readline().split(',')
            self.second_snake = Snake(second_input)

    def get_intersections(self):
        return set(self.first_snake.nodes_visited) & set(self.second_snake.nodes_visited)

    def get_closest_intersection(self):
        intersections = self.get_intersections()
        distances = [abs(node[0]) + abs(node[1]) for node in intersections]
        distances.remove(0)
        return min(distances)


class Snake():
    direction = ''
    shift = 0

    def __init__(self, instructions):
        self.instructions = instructions
        self.cursors = {'x': 0, 'y': 0}
        self.nodes_visited = []

    def set_next_command(self, command):
        self.direction = command[:1]
        self.shift = int(command[1:])

    def move(self):
        if self.direction == 'R':
            self.nodes_visited += [(x, self.cursors['y']) for x in range(self.cursors['x'], self.cursors['x'] + self.shift)]
            self.cursors['x'] += self.shift
        elif self.direction == 'L':
            self.nodes_visited += [(x, self.cursors['y']) for x in range(self.cursors['x'], self.cursors['x'] - self.shift, -1)]
            self.cursors['x'] -= self.shift
        elif self.direction == 'U':
            self.nodes_visited += [(self.cursors['x'], y) for y in range(self.cursors['y'], self.cursors['y'] + self.shift, 1)]
            self.cursors['y'] += self.shift
        elif self.direction == 'D':
            self.nodes_visited += [(self.cursors['x'], y) for y in range(self.cursors['y'], self.cursors['y'] - self.shift, -1)]
            self.cursors['y'] -= self.shift

    def process_snake(self):
        for i in range(0, len(self.instructions)):
            self.set_next_command(self.instructions[i])
            self.move()


if __name__ == '__main__':
    g = Grid()
    for s in [g.first_snake, g.second_snake]:
        s.process_snake()
    print(g.get_intersections())
    print(g.get_closest_intersection())
