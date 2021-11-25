import os
from asteroids_game.score import Score

try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"


def test_IncreaseScore():
    score = Score()
    score.update_score('small')
    assert score.current_score == 100
    score.update_score('medium')
    assert score.current_score == 150
    score.update_score('big')
    assert score.current_score == 170


def test_ResetScore():
    score = Score()
    score.update_score('small')
    score.update_score('small')
    score.update_score('small')
    assert score.current_score == 300
    score.reset_score()
    assert score.current_score == 0
