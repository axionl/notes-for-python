import pickle
import copyreg

class GameState(object):
    def __init__(self, level=0, lives=4, points=0):
        self.level = level
        self.lives = lives
        self.points = points

def unpickle_game_state(kwargs):
    return GameState(**kwargs)

def pickle_game_state(game_state):
    kwargs = game_state.__dict__
    # kwargs['version'] = 2
    return unpickle_game_state, (kwargs, )

def main():
    state = GameState()
    state.level += 1
    state.lives -= 1

    state_path = '/tmp/game_state.bin'
    with open(state_path, 'wb') as f:
        pickle.dump(state, f)

    with open(state_path, 'rb') as f:
        state_after = pickle.load(f)
    print(state_after.__dict__)

    assert isinstance(state_after, GameState)

    copyreg.pickle(GameState, pickle_game_state)
    state.points += 1000
    serialized = pickle.dumps(state)
    state_after = pickle.loads(serialized)
    print(state_after.__dict__)

if __name__ == '__main__':
    main()