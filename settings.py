class Settings:
    def __init__(self):
        # Game
        self.screen_width = 0  # will be overriden
        self.screen_height = 0  # will be overriden
        self.bg_color = (230, 230, 230)

        # Ship
        self.speed = 1.5

        # Bullets
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Aliens
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
