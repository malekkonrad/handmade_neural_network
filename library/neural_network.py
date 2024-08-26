import numpy as np
from numpy import ndarray

from library.layers import Layer    # do uzupełnienia
from library.loss import Loss       # do uzupełnienia


class NeuralNetwork:
    """
    Main class on which we build our models.
    """

    def __init__(self, layers: list[Layer], loss: Loss, seed: int = 1) -> None:
        """
        :param layers: - list of layers
        :param loss: - function, which enables us to compute loss/cost of neural network.
        :param seed: - seed to initialize parameters
        :return: nothing
        """
        self.layers = layers
        self.loss = loss
        self.seed = seed        # może dodać setattr(layer, "seed", self.seed)
    
    def feedforward(self, input_data: ndarray) -> ndarray:
        """ 
        Computes calculation of appling operations and passing forward results and in the end returning predictions 
        
        :param input_data: - outdoor data from datasets
        :return predicitons: - from our Neural Network
        """

        self.input_to_pass = input_data
        for layer in self.layers:
            self.input_to_pass = layer.feedforward(self.input_to_pass)
        
        return self.input_to_pass       # returns ours predicitons


    def backpropagate(self, loss_gradient: ndarray) -> None:
        """
        Computes gradients 
        """
        self.error = loss_gradient
        for layer in reversed(self.layers):
            self.error = layer.backpropagate(self.error)
        
        return None

    def train_batch(self, x_batch: ndarray, y_batch: ndarray) -> float:
        """ 
        Uses feedforward i backpropagate methods to train small batch.
        """

        predictions = self.feedforward(x_batch)
        loss = self.loss.feedforward(predictions, y_batch)
        self.backpropagate(self.loss.backpropagate())

        return loss
        

    def parameters(self):
        for layer in self.layers:
            yield from layer.parameters

    def parameters_gradients(self):
        for layer in self.layers:
            yield from layer.parameters_gradients
