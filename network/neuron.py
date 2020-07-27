class Neuron:
    def __init__(self, bias=None, value=None, af=None):
        self.bias = bias
        self.value = value
        self.af = af
        self.active = False

    def set_bias(self, bias):
        self.bias = bias

    def set_active(self, active):
        self.active = active

    def set_value(self, value):
        self.value = value

    def activation_function(self):
        self.active = self.af()
