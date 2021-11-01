class Score:
    def __init__(self):
        self.current_score = 0
        self.point = {
            'small': 100,
            'medium': 50,
            'big': 20
        }

    def reset_score(self):
        self.current_score = 0

    def update_score(self, size):
        self.current_score += self.point[size]
