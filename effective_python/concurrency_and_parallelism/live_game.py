from collections import namedtuple

ALIVE = '*'
EMPTY = '_'
TICK = object()
Query = namedtuple('Query', ('y', 'x'))
Transition = namedtuple('Transition', ('y', 'x', 'state'))

class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    # def __str__(self):
        # ...

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

class ColumnPrinter(object):
    def __init__(self):
        print("init")

    def append(self, grid):
        print("add grid")

def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # Northeast

    e_ = yield Query(y + 0, x + 1)  # East
    se = yield Query(y - 1, x + 1)  # Southeast

    s_ = yield Query(y - 1, x + 0)  # South
    sw = yield Query(y - 1, x - 1)  # Southwest

    w_ = yield Query(y + 0, x - 1)  # West
    nw = yield Query(y + 1, x - 1)  # Northwest

    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count

def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY
        elif neighbors > 3:
            return EMPTY
    else:
        if neighbors == 3:
            return ALIVE
    return state

def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)

def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK

def live_a_generation(grid, sim):
    progeny = Grid(grid.height, grid.width)
    item = next(sim)
    while item is not TICK:
        if isinstance(item, Query):
            state = grid.query(item.y, item.x)
            item = sim.send(state)
        else:
            progeny.assign(item.y, item.x, item.state)
            item = next(sim)
    return progeny

def test():
    it = count_neighbors(10, 5)
    q1 = next(it)
    print('First yield: ', q1)
    q2 = it.send(ALIVE)
    print('Second yield: ', q2)
    q3 = it.send(ALIVE)
    print('Third yield: ', q3)

    for i in range(4, 9):
        print('The', '%sth yield: ' % i, it.send(ALIVE))
    # ...
    try:
        count = it.send(EMPTY)
    except StopIteration as e:
        print('Count: ', e.value)

def test1():
    it = step_cell(10, 5)
    q0 = next(it)
    print('Me:     ', q0)
    q1 = it.send(ALIVE)
    print('Q1:     ', q1)

    t1 = it.send(EMPTY)
    print('Outcome: ', t1)

def test2():
    grid = Grid(5, 9)
    grid.assign(0, 3, ALIVE)
    print(grid)

    columns = ColumnPrinter()
    sim = simulate(grid.height, grid.width)
    for i in range(5):
        columns.append(str(grid))
        grid = live_a_generation(grid, sim)
    print(columns)

if __name__ == '__main__':
    # test()
    # test1()
    test2()
