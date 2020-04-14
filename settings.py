class Settings:
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0, 0, 0)
		
		#Alien settings
		self.alien_speed = 1.5
		self.fleet_drop_speed = 20
		
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Ship settings
		self.ship_speed = 2.0
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 5.0
		self.bullet_width = 3
		self.bullet_height = 20
		self.bullet_color = (0, 230, 230)
		self.bullets_allowed = 3