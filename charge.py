class Charge:
    """ Abstraction for a charged particle. Has position, 
        velocity, mass, and charge attributes.
    """
    def __init__(self, x_pos, y_pos, x_vel, y_vel, mass, charge,):
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._x_vel = x_vel
        self._y_vel = y_vel
        self._mass = mass
        self._charge = charge
        self._x_force = None
        self._y_force = None
        self._x_accel = None
        self._y_accel = None
        self._x_pts = []
        self._y_pts = []

    def __repr__(self):
        return 'Charge(x_pos={0}, y_pos={1}, x_vel={2}, y_vel={3} '.format(self._x_pos, self._y_pos, self._x_vel, self._y_vel) + \
            'mass={0}, charge={1}, x_force={2}, y_force={3}, '.format(self._mass, self._charge, self._x_force, self._y_force) + \
            'x_accel={0}, y_accel={1})'.format(self._x_accel, self._y_accel)

    def get_x_pos(self):
        return self._x_pos

    def set_x_pos(self, x_pos):
        self._x_pos = x_pos

    def set_y_pos(self, y_pos):
        self._y_pos = y_pos
    
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

    def set_force(self, x_force, y_force):
        self._x_force = x_force
        self._y_force = y_force
    
    def get_x_accel(self):
        return self._x_accel
    
    def get_y_accel(self):
        return self._y_accel

    def set_accel(self, x_accel, y_accel):
        self._x_accel = x_accel
        self._y_accel = y_accel

    def get_x_pts(self):
        return self._x_pts

    def get_y_pts(self):
        return self._y_pts

    def add_x_pt(self, pt):
        self._x_pts.append(pt)

    def add_y_pt(self, pt):
        self._y_pts.append(pt)
