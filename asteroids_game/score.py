class Score:
    def __init__(self):
        self.current_score = 0
        self.destruction_points = 100

    def reset_score(self):
        self.current_score = 0

    def update_score(self):
        self.current_score += self.destruction_points
