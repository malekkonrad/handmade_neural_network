import numpy as np
from numpy import ndarray
import abc

from library.help_functions import softmax

class Loss(abc.ABC):
    """
    Parent class representing different how we compute loss/cost of Neural Network.

    :param: self.loss_value - float - 
    :param: self.loss_gradient - ndarray
    """
    
    def feedforward(self, prediction: ndarray, target: ndarray) -> float:
        """
        Computing loss/cost.
        
        :param: prediciton - ndarray containing the results - activations from the last layer (output layer)
        :param: target - ndarray containing expectations of what we want
        :return: float number representing how far we are from our target
        """

        # We save them because they will be used in private functions.
        self.prediction = prediction        
        self.target = target

        # Compute and save for later.
        self.loss_value = self._compute_loss()
        
        return self.loss_value
    
    def backpropagate(self) -> ndarray:
        """
        Compute gradient of the loss value with respect to the input to the loss function.

        error^(L) (of layer L) = ( delta L / delta a^(L, j) ) * activation function prime ( weighted input )
        In this function we compute the first part of this equation and send it backward (by function backpropagate) to compute the rest of the gradients.
        """
        self.loss_gradient = self._compute_loss_gradient()

        return self.loss_gradient


    @abc.abstractmethod
    def _compute_loss(self):
        """ Computes the loss value with respect to specific Loss function. """
    
    @abc.abstractmethod
    def _compute_loss_gradient(self):
        """ Private function to compute gradient of the loss value based on chosen function. """




class MeanSquaredError(Loss):
    """
    Child class of Loss. 
    MSE - Mean Squared Error 
    """

    def _compute_loss(self) -> float:
        return np.sum(np.power(self.prediction - self.target, 2)) / self.prediction.shape[0]
    
    def _compute_loss_gradient(self) -> ndarray:
        return 2 * (self.prediction - self.target) / self.prediction.shape[0]
    
    
class BinaryCrossEntropyLoss(Loss):
    pass


class SoftmaxCrossEntropyLoss(Loss):
    def __init__(self, eps: float = 1e-9) -> None:
        super().__init__()
        self.eps = eps
        self.single_output = False
    
    def _compute_loss(self):
        softmax_predicitons = softmax(self.prediction, axis=1)

        # clipping the softmax output to prevent numeric instability
        self.softmax_predicitons = np.clip(softmax_predicitons, self.eps, 1 - self.eps)

        # actual loss computation
        softmax_cross_entropy_loss = (
            -1.0 * self.target * np.log(self.softmax_predicitons) - \
                (1.0 - self.target) * np.log(1 - self.softmax_predicitons)
        )

        return np.sum(softmax_cross_entropy_loss) 
    
    def _compute_loss_gradient(self):
        return (self.softmax_predicitons - self.target) 


