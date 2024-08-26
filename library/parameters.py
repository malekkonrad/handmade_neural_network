import numpy as np
from numpy import ndarray



class ParametersInitialize:
    """ Different methods to initialize parameters. It will be used for each layer. """
    
    @staticmethod
    def default_weight_initializer(input_data: ndarray, neurons: int) -> list[ndarray]:
        """
        Initialize each weight and biases using a Gaussian distribution with mean 0
        and standard deviation 1 over the square root of the number of
        weights/biases connecting to the same neuron.
        """
        parameters: list[ndarray] = [] 
        
        # weights
        parameters.append(np.random.normal(loc=0, scale=1, size=(input_data.shape[1], neurons)))

        #biases
        parameters.append(np.random.normal(loc=0, scale=1, size=(1, neurons)))

        return parameters

    @staticmethod
    def glorot_weight_initializer(input_data: ndarray, neurons: int) -> list[ndarray]:
        """
        Every layer has a num_in of neurons (input neurons) and num_out (output neurons).
        Glorot's initializing = 2 / ( num_in + num_out)
        """
        scale = 2/(input_data.shape[1] + neurons)           # where input_data.shape[1] = num_in and neurons = num_out      #maybe change?
        parameters: list[ndarray] = [] 
        # weights
        parameters.append(np.random.normal(loc=0, scale=scale, size=(input_data.shape[1], neurons)))
        #biases
        parameters.append(np.random.normal(loc=0, scale=scale, size=(1, neurons)))

        return parameters
    

    @staticmethod
    def he_weight_initializer():
        pass

    @staticmethod
    def leCun_weight_initializer():
        pass
    


class WeightedInput:
    """ 
    Class responisble for computing weighted input, which will be sent to activation function.
    Z = W * A + B
    """

    def __init__(self, parameters: list[ndarray]) -> None:
        """
        :param parameters: - list of numpy's arrays, where parameters[0] - array of weight, parameters[1] - array of biases.
        """
        self.parameters: list[ndarray] = parameters
        self.parameters_gradients: list[ndarray] = []

    
    def feedforward(self, input_data: ndarray) -> ndarray:
        """ uzupełnic"""
        self.input_data = input_data
        self.output = self._compute_weights()
        self.output = self._compute_biases()
        return self.output

    def backpropagate(self, error: ndarray) -> ndarray: 
        """ 
        Computes needed gradients for weights and biases.
         
        :param error: - actual error in the layer
        """

        # Compute gradients for weights -> delta Cost/ delta weights = activation_from_previous_layer * actual_error        where activation_from_previous_layer is self.input_data
        gradient_weights = self._compute_gradient_weights(error)
        self.parameters_gradients.append(gradient_weights)

        # Compute gradients for biases -> delta Cost/ delta biases = error 
        gradient_biases = self._compute_gradient_biases(error)
        self.parameters_gradients.append(gradient_biases)

        # Compute error so it will be passed to next layer in going backward
        updated_error = self._compute_error_to_pass(error)
        
        return updated_error

        


        
    def _compute_weights(self):
        return np.matmul(self.input_data, self.parameters[0])

    def _compute_biases(self):
        return self.output + self.parameters[1]


    def _compute_gradient_weights(self, error):
        return np.matmul(self.input_data.transpose(1, 0), error)        # we need to transpose it to be able to multiply this (in equation is the same)
    
    def _compute_error_to_pass(self, error):
        return np.matmul(error, self.parameters[0].transpose(1, 0))     # muliply by weights of actual layer
    
    def _compute_gradient_biases(self, error):
        output_grad_reshape = np.sum(error, axis=0).reshape(1, -1)
        param_grad = np.ones_like(self.parameters[1])
        return param_grad * output_grad_reshape
