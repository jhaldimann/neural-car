from network.layer import Layer

class Network:
    def __init__(self, start_layer, end_layer, af, num_hidden_layers=1):
        self.start_layer = start_layer
        self.end_layer = end_layer
        self.hidden_layers = []

        num_neurons = round(len(self.start_layer) * .66 + len(end_layer))
        for i in range(num_hidden_layers):
            self.hidden_layers.append(Layer(num_neurons, af))
