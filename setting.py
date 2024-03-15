class Settings():
    '''A class to store all settings for Alien Invasion.'''
    def __init__(self):
        '''Initialize game's settings.'''
        #Screen Settings.
        self.screen_width=1200
        self.screen_height=800
        self.screen_bg_color=(230,230,230)
        self.ship_speed_factor = 0.75
        #Bullet Settings.
        self.bullet_speed_factor = 3
        self.bullet_width =3
        self.bullet_height =15
        self.bullet_color =(0,0,0)
        self.bullets_allowed = 5
        #Alien settings
        self.alien_speed_factor=1
        self.fleet_drop_speed =10
        #fleet_direction of 1 represents right; -1 represents left. 
        self.fleet_direction =1 
        #Ship settings
        self.ship_speed_factor =1.5
        self.ship_limit= 3

