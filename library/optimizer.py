import numpy as np
from numpy import ndarray
import abc



class Optimizer(abc.ABC):
    """ Prototype class for different optimizers. """

    def __init__(self, learning_rate: float = 0.01) -> None:

        self.learning_rate = learning_rate
    
    @abc.abstractmethod
    def step(self):
        """ """



class SGD(Optimizer):
    """ Stochastic Gradient Descendant. """
    
    def step(self):
        
        for (parameter, parameter_gradient) in zip(self.network.parameters(), self.network.parameters_gradients()):
            parameter -= self.learning_rate * parameter_gradient


