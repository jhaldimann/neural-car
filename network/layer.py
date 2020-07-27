from network.neuron import Neuron
import random as rd

class Layer:
    def __init__(self, num_neurons, af, is_start=False):
        self.nodes = []
        if not is_start:
            for i in range(num_neurons):
                self.nodes.append(Neuron(bias=rd.random(), af=af))

