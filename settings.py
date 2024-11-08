class Settings:
    def __init__(self):
        # Game
        self.screen_width = 0  # will be overriden
        self.screen_height = 0  # will be overriden
        self.bg_color = (230, 230, 230)
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        # Ship
        self.ship_speed = 1.5

        # Bullets
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliens
        self.alien_speed = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.ship_limit = 3

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 0.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increate_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
