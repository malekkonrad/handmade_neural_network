import numpy as np
import abc
from numpy import ndarray

from library.parameters import ParametersInitialize, WeightedInput
from library.activation import ActivationFunction, Sigmoid



class Layer(abc.ABC):
    """
    Layer Prototype.

    :param self.neurons: - int - how many neurons layer has
    :param self.activation: - callable - variable contating activation function of specific layer
    :param self.parameters: - list[ndarray] - list containing two ndarrays - Weights and Biases
    :param self.parameters_gradients: - sss - sssss
    :param first_activation: - bool - variable, that enables us to identify if we need to setup layer or not
    """

    def __init__(self, neurons: int, activation: ActivationFunction = Sigmoid) -> None:
        self.neurons: int = neurons
        self.activation: callable = activation
        self.parameters: list[np.ndarray] = []
        self.parameters_gradients: list[np.ndarray] = []
        self.first_activation: bool = True
        

    def feedforward(self, input_data: ndarray) -> ndarray:
        """
        Method, which computes A^(l) = act_fun(W*A^(l-1) + B)

        :param input_data: - actual ndarray of computing data
        :return: - ndarray containing data after computing weighted input and putting it in activation data - transferring to next layer.
        """

        # setup layers - we need to know the input_ to layer to properly initialize it.
        if self.first_activation:
            self._setup_layer(input_data)
            self.first_activation = False

        return self._compute_output(input_data)
        

    def backpropagate(self, output_data: ndarray) -> ndarray:
        """
        Method which takes error (delta = ( delta Loss/ delta avtivation ) * activation_prime( weighted_input )) from previous layer 
        and computes gradients from parameters in current layer and error that will be passed to next layer and so on.

        :param output_data:  - error from previous layer, necesery to compute gradients of parameters
        :return: ndarray of error
        """
        # save for use in private method _compute_gradients()
        self.output_data = output_data
        self.gradient = self._compute_gradients(output_data)

        # the key method is _compute_parameters_gradients() which saves parameters gradients that we need to change to optimize our Neural Network
        # self.paremters_gradients = self._compute_parameters_gradients()
        
        return self.gradient

    


    # abstract methods:


    @abc.abstractmethod
    def _setup_layer(self, input_data: ndarray) -> None:
        """ Abstract method, specific for every child class of Layer - every type of layer needs to be initilized differently. """

    @abc.abstractmethod
    def _compute_output(self, input_data: ndarray) -> ndarray:
        """ Computes operation for each layer. """

    @abc.abstractmethod
    def _compute_gradients(self):
        """ Computes gradient of loss function relative to input_data. """

    @abc.abstractmethod
    def _compute_parameters_gradients(self):
        """ COmputes gradients of parameters in current layer (weights and biases). """


class Dense(Layer):
    """
    Fully connected layer - most commonly used in Neural Networks.
    """

    def __init__(self, neurons: int, activation: ActivationFunction = Sigmoid) -> None:
        super().__init__(neurons, activation)

    def _setup_layer(self, input_data: ndarray) -> None:
        self.parameters = ParametersInitialize.glorot_weight_initializer(input_data, self.neurons)
        # TODO: dropout
    
    def _compute_output(self, input_data: ndarray) -> ndarray:
        # Computing weigthed input to next layer.
        self.__w_i = WeightedInput(self.parameters)       # Instance of class WeightedInput - enables to handle weight and biases
        self.weighted_input = self.__w_i.feedforward(input_data)

        # Activation function
        self.output = self.activation.feedforward(self.weighted_input)

        return self.output
    
    def _compute_gradients(self, error: ndarray) -> ndarray:
        error = self.activation.backpropagate(error)
        error = self.__w_i.backpropagate(error)
        self.parameters_gradients = self.__w_i.parameters_gradients
        return error
        

    def _compute_parameters_gradients(self):
        pass


class Conv(Layer):
    pass