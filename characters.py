#!/usr/bin/env python3

class Knight:
    
    def __init__(self, qualities):
        """ Construct knight from the dictionary of qualities """
        self.qualities = qualities

    def name(self):
        """ Get knight's name """
        return self.qualities['name']

    def attack(self):
        """ Get knight's attack """
        return self.qualities['attack']

    def armor(self):
        """ Get knight's armor """
        return self.qualities['armor']

    def agility(self):
        """ Get knight's agility """
        return self.qualities['agility']

    def endurance(self):
        """ Get knight's endurance """
        return self.qualities['endurance']
    
    def to_list(self):
        """ Get list of knight's qualities """
        return [self.attack(), self.armor(), self.agility(), \
                self.endurance()]

class Dragon:

    def __init__(self, scale_thickness, claw_sharpness, \
                 wing_strength, fire_breath):
        """ Construct dragon from list  of qualities """
        self.qualities = dict()
        self.qualities['fireBreath']     = fire_breath
        self.qualities['wingStrength']   = wing_strength
        self.qualities['clawSharpness']  = claw_sharpness
        self.qualities['scaleThickness'] = scale_thickness
        if sum(self.qualities.values()) != 20:
            raise AssertionError(self.qualities)

    def scale_thickness(self):
        """ Get dragon's scale thickness """
        return self.qualities['scaleThickness']

    def claw_sharpness(self):
        """ Get dragon's claw sharpness """
        return self.qualities['clawSharpness']

    def wing_strength(self):
        """ Get dragon's wing strength """
        return self.qualities['wingStrength']

    def fire_breath(self):
        """ Get dragon's fire breath """
        return self.qualities['fireBreath']

    def to_list(self):
        """ Get list of dragon's qualities """
        return [self.scale_thickness(), self.claw_sharpness(), \
                self.wing_strength(), self.fire_breath()]

if __name__ == '__main__':
    pass
            
    
