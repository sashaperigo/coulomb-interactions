from matplotlib import pyplot
import sys

from charge import Charge
from constants import *

class Environment: 
    def __init__(self):
        self._charges = []
        self._time = 0
        self.NUM_POINTS_TO_PLOT = 1000
        self.NUM_CHARGES_TO_PLOT = 3
        self.COLORS = ['r', 'g', 'b']

    def _any_overlap(self, x_pos, y_pos):
        """ Returns True if any charge already in the environment
            overlaps with the new charge we are trying to add.
            False otherwise.
        """
        for charge in self._charges:
            if charge.get_x_pos() == x_pos and charge.get_y_pos() == y_pos:
                return True
        return False

    def add_proton(self, x_pos, y_pos, x_vel, y_vel):
        """ Adds a proton with the given position and velocity 
            to the environment. 
        """
        self.add_charge(x_pos, y_pos, x_vel, y_vel, PROTON_WEIGHT, ELEM_CHARGE)

    def add_electron(self, x_pos, y_pos, x_vel, y_vel):
        """ Adds an electron with the given position and velocity 
        to the environment.
        """
        self.add_charge(x_pos, y_pos, x_vel, y_vel, ELECTRON_WEIGHT, -ELEM_CHARGE)

    def add_charge(self, x_pos, y_pos, x_vel, y_vel, mass, charge):
        """ Adds a point charge with the given position,
            velocity, mass, and charge to the environment.

            Allows the users to add charges that are not
            just protons and electrons!
        """
        if self._any_overlap(x_pos, y_pos):
            sys.exit('There is already a charge at ({0}, {1}). '.format(x_pos, y_pos) + \
                     'No two points can overlap in space!')
        charge = Charge(x_pos, y_pos, x_vel, y_vel, mass, charge)
        self._charges.append(charge)

    def _calculate_net_force(self, probe):
        """ Calculates the net force on a probe charge from all
            of the other charges in the environment. Sets the 
            force attribute on the probe charge element.
        """
        net_x_force = 0
        net_y_force = 0
        for charge in self._charges:
            if charge is not probe:
                f = probe.coulomb_force(charge)
                net_x_force += f[0]
                net_y_force += f[1]
        probe.set_force(net_x_force, net_y_force)

    def _get_points(self, time):
        """ Calculates the location of each point charge at 
            NUM_POINTS_TO_PLOT different steps along the specified
            time interval.
        """
        step = float(time) / (self.NUM_POINTS_TO_PLOT - 1)
        for i in range(0, self.NUM_POINTS_TO_PLOT):
            t = step * i

            for charge in self._charges:
                self._calculate_net_force(charge)
                charge.set_accel()

                x = charge.get_x_pos() + charge.get_x_vel() * t + 0.5 * charge.get_x_accel() * (t ** 2)
                y = charge.get_y_pos() + charge.get_y_vel() * t + 0.5 * charge.get_y_accel() * (t ** 2)

                # Convert to micrometers for so our plot is prettier!
                charge.add_x_pt(float(x) / M_PER_MICROM)
                charge.add_y_pt(float(y) / M_PER_MICROM)

            # Update the current x and y positions of the charges.
            # It's important that we do this in a separate loop, 
            # so that we don't mess up the initial calculations!
            for charge in self._charges:
                new_x = charge.get_x_pts()[-1]
                new_y = charge.get_y_pts()[-1]

                # Convert back to meters
                charge.set_x_pos(new_x * M_PER_MICROM)
                charge.set_y_pos(new_y * M_PER_MICROM)

    def _plot_trajectory(self, charge, color):
        """ Plots the trajectory of one point charge.
        """
        x_pts = charge.get_x_pts()
        y_pts = charge.get_y_pts()
        pyplot.plot(x_pts, y_pts, color=color)

    def plot_charges(self, time, nb=False):
        """ Plots the interactions of the first three points
            added to the environment.
        """
        self._get_points(time)
        for i in range(0, self.NUM_CHARGES_TO_PLOT):
            self._plot_trajectory(self._charges[i], self.COLORS[i])

        ax = pyplot.gca()
        ax.set_xlim([-5, 5])
        ax.set_ylim([-5, 5])
        
        # Set correct size for iPython Notebook
        if nb:
            plot = pyplot.gcf()
            plot.set_size_inches((15, 10))

        if time == 1:
            pyplot.title("Charge Trajectories After 1 Second")
        else:
            pyplot.title("Charge Trajectories After %d Seconds" % time)
        
        pyplot.xlabel("X Position Over Time (micrometers)")
        pyplot.ylabel("Y Position Over Time (micrometers)")
        pyplot.show()
