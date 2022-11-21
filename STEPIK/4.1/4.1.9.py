from typing import Any


class Layer:

    def __init__(self):
        self.next_layer = None
        self.name = 'Layer'

    def __call__(self, new_layer: "Layer"):
        self.next_layer = new_layer
        return new_layer


class Input(Layer):

    def __init__(self, inputs: int):
        super().__init__()
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):

    def __init__(self, inputs, outputs: int, activation: str):
        super().__init__()
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = 'Dense'


class NetworkIterator:

    def __init__(self, network: Any):
        self.network = network

    def __iter__(self):
        lay = self.network
        while lay is not None:
            yield lay
            lay = lay.next_layer


nt = Input(12)
layer = nt(Dense(nt.inputs, 1024, 'relu1'))
layer = layer(Dense(layer.inputs, 2048, 'relu2'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

n = 0

for x in NetworkIterator(nt):

    assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
    n += 1

assert n == 4, "итератор перебрал неверное число слоев"