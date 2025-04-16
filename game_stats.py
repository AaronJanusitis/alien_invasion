import os

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

        # High score should never be reset, retrived from highscore.txt
        self.high_score = self._get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score(self):
        current_dir = f'{os.path.dirname(os.path.realpath(__file__))}'
        path = f'{current_dir}\\highscore.txt'
        if not os.path.isfile(path):
            score_file = open(f'{os.path.dirname(os.path.realpath(__file__))}\\highscore.txt', 'w')
            score_file.write('0')
            score_file.close()
        score_file = open(f'{os.path.dirname(os.path.realpath(__file__))}\\highscore.txt', 'r')
        retrieved_score = int(score_file.read())
        return retrieved_score