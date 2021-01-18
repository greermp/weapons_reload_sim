import salabim as sim

# DDG
DDG_ARRIVAL_DIST = sim.Normal(10, 1)
DDG_N_CONSUMED = 36


# TAKEs
TAKE_ARRIVAL_DIST = sim.Normal(1000, 10)
TAKE_N_SUPPLIED = 5

# ERTs
NUM_FAST_ERT = 3
NUM_SLOW_ERT = 3

FAST_ERT_RELOAD_TIME = 15
SLOW_ERT_RELOAD_TIME = 20