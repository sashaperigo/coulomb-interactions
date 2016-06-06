from environment import Environment

environ = Environment()
environ.add_electron(0, 0, 0, 0)
environ.add_electron(0, 1, 0, 0)
environ.add_electron(1, 0, 0, 0)
environ.plot_charges(1)
