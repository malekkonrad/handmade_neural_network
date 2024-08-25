import numpy as np
from numpy import ndarray
import abc

from library.neural_network import NeuralNetwork
from library.optimizer import Optimizer, SGD

from library.help_functions import permute_data

class Trainer:
    """ Teach Neural Network. """

    def __init__(self, network: NeuralNetwork, optimizer: Optimizer) -> None:
        
        self.network = network
        self.optimizer = optimizer
        setattr(self.optimizer, 'network', self.network)


    def fit(self, X_train: ndarray, y_train: ndarray, X_test: ndarray, y_test: ndarray, epochs: int = 100, eval_every: int = 10, batch_size: int = 32, seed: int = 1, restart: bool = True) -> None:
        np.random.seed(seed)

        if restart:
            for layer in self.network.layers:
                layer.first_activation = True
            
        for e in range(epochs):

            X_train, y_train = permute_data(X_train, y_train)
            batch_generator = self.generate_batches(X_train, y_train, batch_size)

            for ii, (X_batch, y_batch) in enumerate(batch_generator):
                self.network.train_batch(X_batch, y_batch)
                self.optimizer.step()
            
            if (e+1) % eval_every == 0:
                test_preds = self.network.feedforward(X_test)
                loss = self.network.loss.feedforward(test_preds, y_test)
                print(f"kontrolna wartość straty po {e+1} epokach wynois {loss:.3f}")

    
    def generate_batches(self,
                         X: ndarray,
                         y: ndarray,
                         size: int = 32):

        assert X.shape[0] == y.shape[0], \
        '''
        features and target must have the same number of rows, instead
        features has {0} and target has {1}
        '''.format(X.shape[0], y.shape[0])

        N = X.shape[0]

        for ii in range(0, N, size):
            X_batch, y_batch = X[ii:ii+size], y[ii:ii+size]

            yield X_batch, y_batch