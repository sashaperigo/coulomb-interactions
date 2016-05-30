import math
from matplotlib import pyplot

from charge import Charge

K = 8.85e-12
NUM_POINTS = 15
COLORS = ['r', 'g', 'b']

# def get_vector_components(magnitude, angle):
#     """ Takes the magnitude and direction of a vector and
#         returns the x and y components of that vector. 
#     """
#     x = magnitude * math.cos(angle)
#     y = magnitude * math.cos(angle)
#     return [x, y]

# def get_vector_magnitude(x, y):
#     """ Returns the magnitude of a vector given its x and
#         y components.
#     """
#     return math.sqrt(x ** 2 + y ** 2)
    
# def get_vector_direction(x, y):
#     """ Returns the directional angle of a vector given its
#         x and y components.
#     """
#     return math.arctan(float(x) / float(y))


def get_distance(first, second):
    """ Takes two Charge objects and returns the distance
        between the two.
    """
    x_dist = first.get_x_pos() - second.get_x_pos()
    y_dist = first.get_y_pos() - second.get_y_pos()
    return math.sqrt(x_dist ** 2 + y_dist ** 2)

    
def get_angle(first, second):
    x_dist = first.get_x_pos() - second.get_x_pos()
    y_dist = first.get_y_pos() - second.get_y_pos()
    if y_dist == 0:
        return 0
    if x_dist == 0:
        return float(math.pi) / 2
    return math.atan(float(x_dist) / y_dist)

   
def coulomb_force(first, second):
    """ Takes two Charge objects as parameters and returns
        the magnitude of the force between the two.
    """
    r = get_distance(first, second)
    return (K * math.fabs(first.get_charge()) * math.fabs(second.get_charge())) / r ** 2

   
def calculate_net_force(charges, probe):
    """ Calculates the net force on a probe charge from all
        of the other charges in the environment. Sets the 
        force attribute on the probe charge element.
    """
    net_x_force = 0
    net_y_force = 0
    for charge in charges:
        if charge is not probe:
            angle = get_angle(probe, charge)
            magnitude = coulomb_force(probe, charge)
            net_x_force += magnitude * math.cos(angle)
            net_y_force += magnitude * math.sin(angle)
    probe.set_force(net_x_force, net_y_force)

  
def calculate_accel(probe):
    mass = probe.get_mass()
    x_accel = float(probe.get_x_force()) / mass
    y_accel = float(probe.get_y_force()) / mass
    probe.set_accel(x_accel, y_accel)
    

def get_point_at_time(charges, t):
    for charge in charges:
        calculate_net_force(charges, charge)
        calculate_accel(charge)

        x = charge.get_x_pos() + charge.get_x_vel() * t + 0.5 * charge.get_x_accel() * (t ** 2)
        y = charge.get_y_pos() + charge.get_y_vel() * t + 0.5 * charge.get_y_accel() * (t ** 2)

        charge.add_x_pt(x)
        charge.add_y_pt(y)

    for charge in charges:
        charge.set_x_pos(charge.get_x_pts()[-1])
        charge.set_y_pos(charge.get_y_pts()[-1])


def get_points(charges, time):
    step = float(time) / (NUM_POINTS - 1)
    for i in range(0, NUM_POINTS):
        get_point_at_time(charges, step * i)


def plot_trajectory(charge, color):
    print charge.get_x_pts()
    print charge.get_y_pts()
    print '\n'
    pyplot.plot(charge.get_x_pts(), charge.get_y_pts(), color=color, marker='o')


# def hello():
#     print "Welcome fam"


# def get_ordinal(i):
#     assert(i >= 1 and i <= 3)
#     if i == 1: return "first"
#     if i == 2: return "second"
#     if i == 3: return "third"


# def read_charge_info(i):
#     ith = get_ordinal(i)

#     print "Enter the initial x position for the %s charge: " % ith
#     x_pos = raw_input()
#     print "Enter the initial y position for the %s charge: " % ith
#     y_pos = raw_input()
#     print "Enter the initial velocity (mps) in the x direction for the %s charge: " % ith
#     x_vel = raw_input()
#     print "Enter the initial velocity (mps) in the y direction for the %s charge: " % ith
#     y_vel = raw_input()
#     print "Enter the mass (kg) of the %s charge: " % ith
#     mass = raw_input()
#     print "Enter the charge (C) of the %s charge: " % ith
#     charge = raw_input()

#     return Charge(x_pos, y_pos, x_vel, y_vel, mass, charge)


# def read_time():
#     print "Enter the time in seconds that "
#     return time

# hello()
charges = []
# for i in range(0, 3):
#     charges.add(read_charge_info())
# time = read_time()
charge_1 = Charge(1e-12, 1e-12, 0, 0, 9.1e-31, -1.6e-19)
charge_2 = Charge(0, 1e-12, 0, 0, 9.1e-31, -1.6e-19)
charge_3 = Charge(1e-12, 0, 0, 0, 9.1e-31, -1.6e-19)

charges.append(charge_1)
charges.append(charge_2)
charges.append(charge_3)
time = 5

get_points(charges, time)

for i, charge in enumerate(charges):
    plot_trajectory(charge, COLORS[i])

pyplot.title("Charge Trajectories After %d Seconds" % time)
# pyplot.legend()
pyplot.show()
