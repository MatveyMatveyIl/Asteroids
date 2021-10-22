def save_result(level):
    with open('asteroids_game/user_results.txt', 'w') as f:
        f.write(level)