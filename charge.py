import math
from constants import *

class Charge:
    """ Abstraction for a charged particle. Has position, 
        velocity, mass, and charge attributes.
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, mass, charge):
        self._x_pos = float(x_pos) * M_PER_MICROM
        self._y_pos = float(y_pos) * M_PER_MICROM
        self._x_vel = float(x_vel) * M_PER_MICROM
        self._y_vel = float(y_vel) * M_PER_MICROM
        self._mass = mass
        self._charge = charge
        self._x_force = None
        self._y_force = None
        self._x_accel = None
        self._y_accel = None
        self._x_pts = []
        self._y_pts = []

    def __repr__(self):
        return 'Charge(' + \
            'x_pos={0}, y_pos={1}, '.format(self._x_pos, self._y_pos) + \
            'x_vel={2}, y_vel={3} '.format(self._x_vel, self._y_vel) + \
            'mass={0}, charge={1}, '.format(self._mass, self._charge) + \
            'x_force={2}, y_force={3}, '.format(self._x_force, self._y_force) + \
            'x_accel={0}, y_accel={1})'.format(self._x_accel, self._y_accel)

    # Interactions between charges

    def distance_between(self, other):
        """ Takes two Charge objects and returns the distance
            between them in meters.
        """
        x_dist = self._x_pos - other.get_x_pos()
        y_dist = self._y_pos - other.get_y_pos()
        dist = math.sqrt(x_dist ** 2 + y_dist ** 2)

        # Avoid division by zero 
        if dist == 0:
            return 0.000000001
        return dist

    def angle_between(self, other):
        """ Takes two Charge objects and returns the angle 
            between them in radians.
        """
        x_dist = self._x_pos - other.get_x_pos()
        y_dist = self._y_pos - other.get_y_pos()
        
        # Edge cases
        if y_dist == 0:
            return 0
        if x_dist == 0:
            return float(math.pi) / 2

        return math.atan(float(x_dist) / y_dist)

    def _repulsive(self, other):
        """ Boolean function that returns True if the two objects 
            have charges of opposite signs and false otherwise.
        """
        charge_1 = self._charge
        charge_2 = other.get_charge()
        return (charge_1 > 0 and charge_2 < 0) or (charge_1 < 0 and charge_2 > 0)

    def coulomb_force(self, other):
        """ Returns the Coulomb force on this charge object 
            exerted by the second charge object.
        """
        numerator = K * self._charge * other.get_charge()
        denominator = self.distance_between(other)
        f = math.fabs(float(numerator) / denominator)

        angle = self.angle_between(other)
        fx = f * math.cos(angle)
        fy = f * math.sin(angle)

        # Flip signs as necessary
        if self._repulsive(other):
            if self._x_pos < other.get_x_pos():
                fx = fx * -1
            if self._y_pos < other.get_y_pos():
                fy = fy * -1
        else:
            if self._x_pos > other.get_x_pos():
                fx = fx * -1
            if self._y_pos > other.get_y_pos():
                fy = fy * -1

        return [fx, fy]

    # 'Set methods'

    def set_x_pos(self, x_pos):
        self._x_pos = x_pos

    def set_y_pos(self, y_pos):
        self._y_pos = y_pos

    def set_force(self, x_force, y_force):
        self._x_force = x_force
        self._y_force = y_force

    def set_accel(self):
        """ Calculates and sets the acceleration of a charge
            based on Newton's Second Law.
        """
        mass = self._mass
        self._x_accel = float(self._x_force) / mass
        self._y_accel = float(self._y_force) / mass

    def add_x_pt(self, pt):
        self._x_pts.append(pt)

    def add_y_pt(self, pt):
        self._y_pts.append(pt)

    # 'Get' methods

    def get_x_pos(self):
        return self._x_pos
    
    def get_y_pos(self):
        return self._y_pos
    
    def get_x_vel(self):
        return self._x_vel
    
    def get_y_vel(self):
        return self._y_vel
    
    def get_mass(self):
        return self._mass
    
    def get_charge(self):
        return self._charge
        
    def get_x_force(self):
        return self._x_force
 
    def get_y_force(self):
        return self._y_force
    
    def get_x_accel(self):
        return self._x_accel
    
    def get_y_accel(self):
        return self._y_accel

    def get_x_pts(self):
        return self._x_pts

    def get_y_pts(self):
        return self._y_pts
