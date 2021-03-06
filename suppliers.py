import salabim as sim
from operator import itemgetter
from globals import *

import crayons

verbose = VERBOSE_ALL or VERBOSE_SUPPLIERS


class takeGenerator(sim.Component):
    # def __init__(self, resource, n_supplied=1):
    def __init__(self, config={}):
        sim.Component.__init__(self)

        # Attach the config dict to self
        self.config = config

    def process(self):

        # Destructure config
        arrival_dist, resource, n_supplied = itemgetter(
            'arrival_dist', 'resource', 'n_supplied')(self.config)

        # Generate objects
        i = 0
        while i > -1:
            if i < 1:
                # TAKE(self.config)  # remove
                yield self.hold(arrival_dist.sample())
            else:
                TAKE(self.config)
                yield self.hold(arrival_dist.sample())
            i += 1


class TAKE(sim.Component):
    def __init__(self, config={}):
        sim.Component.__init__(self)
        self.config = config

    def process(self):

        # Destructure config
        resource, n_supplied = itemgetter(
            'resource', 'n_supplied')(self.config)
        if verbose:
            print(crayons.green(
                f'TAKE arrived, supplying {n_supplied} resources'))
        resource.set_capacity(resource.capacity() + n_supplied)
        # self.resource.set_capacity(self.resource.capacity() + 0)
        yield self.hold()


# class ERT(sim.Component):
#     def __init__(self, queue, reload_time):
#         sim.Component.__init__(self)
#         self.queue = queue
#         self.reload_time = reload_time

#     def process(self):
#         while True:
#             while len(self.queue) == 0:
#                 yield self.passivate()
#             self.customer = self.queue.pop()
#             yield self.hold(self.reload_time)
#             self.customer.activate()
