
import numpy as np
from keras.datasets import mnist



from library.neural_network import NeuralNetwork
from library.activation import Sigmoid, Linear, Tanh
from library.layers import Dense
from library.loss import MeanSquaredError, SoftmaxCrossEntropyLoss
from library.trainer import Trainer
from library.optimizer import SGD



(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train, X_test = X_train - np.mean(X_train), X_test - np.mean(X_train)

# Normalizacja danych
X_train = X_train / 255.0
X_test = X_test / 255.0

# Przekształcanie danych do formatu 2D
X_train = X_train.reshape(X_train.shape[0], -1)
X_test = X_test.reshape(X_test.shape[0], -1)

# One-hot encoding etykiet
num_classes = 10
y_train = np.eye(num_classes)[y_train]
y_test = np.eye(num_classes)[y_test]




def calc_accuracy_model(model, test_set):
    return print(f'''The model validation accuracy is: {np.equal(np.argmax(model.feedforward(test_set), axis=1), np.argmax(y_test, axis=1)).sum() * 100.0 / test_set.shape[0]:.2f}%''')



# model_1
# model = NeuralNetwork(
#     layers=[Dense(neurons=89,
#                    activation=Sigmoid()),
#             Dense(neurons=10,
#                    activation=Sigmoid())],
#     loss=MeanSquaredError(),
#     seed=20190501
# )

# model_2
model = NeuralNetwork(
    layers=[Dense(neurons=89,
                   activation=Tanh()),
            Dense(neurons=10,
                   activation=Linear())],
    loss=SoftmaxCrossEntropyLoss(),
    seed=20190501
)

# Trener
trainer = Trainer(model, SGD(0.1))
trainer.fit(X_train, y_train, X_test, y_test,
            epochs=50,
            eval_every=10,
            seed=20190119,
            batch_size=60)



calc_accuracy_model(model, X_test)