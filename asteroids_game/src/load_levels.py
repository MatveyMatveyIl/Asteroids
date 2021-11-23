import os

def load_levels():
    levels = dict()
    path = os.path.abspath(f'asteroids_game/levels.txt')
    with open(path, 'r') as f:
        while True:
            text = f.readline()
            if len(text) == 0:
                break
            level_number = text.split(':')[0]
            count_asteroids = list(map(lambda x: int(x), text.split(':')[1].split(',')))
            levels[level_number] = count_asteroids

    return levels
