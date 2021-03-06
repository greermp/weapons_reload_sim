import salabim as sim

# Simulation Controls
TRACE = False
SIM_LENGTH = 5000
SIM_SPEED = 250

# Debugging
VERBOSE_ALL = 0
VERBOSE_BASE = 0
VERBOSE_CONSUMERS = 0
VERBOSE_SUPPLIERS = 0

# DDG
DDG_ARRIVAL_DIST = sim.Uniform(60, 110)
DDG_N_CONSUMED_DIST = sim.Uniform(20, 30)


# TAKEs
# TAKE_ARRIVAL_DIST = sim.Uniform(800, 1000)
TAKE_ARRIVAL_DIST = sim.Normal(800, 200)
TAKE_N_SUPPLIED = 200

# ERTs
NUM_FAST_ERT = 3
NUM_SLOW_ERT = 3

FAST_ERT_RELOAD_TIME = 15
SLOW_ERT_RELOAD_TIME = 30
