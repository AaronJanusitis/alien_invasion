class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's static settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        self.game_difficulty = 'easy'

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game based on difficulty level"""
        if self.game_difficulty == 'easy':
            self.ship_speed = 5
            self.bullet_speed = 7.0
            self.alien_speed = 3.0
            self.score_scale = 1.5
        elif self.game_difficulty == 'medium':
            self.ship_speed = 4
            self.bullet_speed = 6.0
            self.alien_speed = 4.0
            self.score_scale = 1.6
        elif self.game_difficulty == 'hard':
            self.ship_speed = 3
            self.bullet_speed = 5.0
            self.alien_speed = 5.0
            self.score_scale = 1.7

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)