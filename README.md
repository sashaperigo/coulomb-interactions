# Coulomb Interactions

Exports a small API to plot Coulomb interactions between charged particles. Play with it for yourself in the iPython Notebook!

### About the API

#### Create the Environment

In order to plot point charges, you must first create an instance of the Environment class. Set the result equal to a variable name of your choosing!

`e = Environment()`

#### Add three point charges

Add three particles to the environment using some combination of the following three functions:

`e.add_electron(x_pos, y_pos, x_vel, y_vel)`

`e.add_proton(x_pos, y_pos, x_vel, y_vel)`

`e.add_charge(x_pos, y_pos, x_vel, y_vel, mass, charge)`

The parameters `x_pos`, `y_pos`, `x_vel`, and `y_vel` represent x position, y position, x velocity, and y velocity. These measurements are in <strong>micrometers</strong> and <strong>micrometers per second</strong> for ease of plotting, as at the charge level, a meter is rather far. You can use the `add_proton()` and `add_electron()` functions to add a proton or an electron to the environment. If you would rather add a point charge with a custom mass and charge you can, just use the `add_charge()` function and specify the weight in kg and the charge in Coulombs as the fifth and sixth arguments.

Some important notes: 
- No two charged particles can overlap in space. The program will throw an error and exit if you try to add to charges at the exact same location. 
- All masses must be positive! The program will throw an error and exit if you input a negative mass.
- You must add at least three charges to the environment. If you add more than three charges, extra charges will be ignored.

#### Plot over time

Use the following function to plot your charge configuration:

`e.plot_charges(time, True)`

The time parameter takes the amount of time you would like to plot over, in seconds.
