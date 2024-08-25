import numpy as np
import abc
from numpy import ndarray

class ActivationFunction(abc.ABC):
    """
    Interface class.
    """

    def feedforward(self, input_data: ndarray):
        """
        Applies selected activation function to whole array of weighted input computed previously.
        """
        self.x = input_data
        
        # compute and save for later - it will be used in function computing gradient.
        self.output = self._compute_output()

        return self.output

    def backpropagate(self, output_data: ndarray) -> ndarray:
        """
        Method to get rest of the needed equation parts.
        """

        # Save output_data in every instance of child class to be able to use it in private method _compute_gradient()
        self.output_data = output_data
        self.output_data = self._compute_gradient()
        
        return self.output_data

    @abc.abstractmethod
    def _compute_output(self):
        """ Computes the activation function itself. """

    @abc.abstractmethod
    def _compute_gradient(self):
        """ Computes gradient of input data. """
        



class Sigmoid(ActivationFunction):
    """ Sigmoid activation function. """

    def _compute_output(self):
        return 1 / (1 + np.exp(-self.x))
    
    def _compute_gradient(self):
        sigmoid_prime = self.output * (1 - self.output)
        self.loss_gradient = self.output_data * sigmoid_prime
        return self.loss_gradient



class ReLU(ActivationFunction):
    pass


class LeakyReLU(ActivationFunction):
    pass


class Tanh(ActivationFunction):
    pass


class Linear(ActivationFunction):
    pass


class Softmax(ActivationFunction):
    pass