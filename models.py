
import numpy as np
from keras.datasets import mnist
import matplotlib.pyplot as plt


from library.neural_network import NeuralNetwork
from library.activation import Sigmoid, Linear, Tanh
from library.layers import Dense
from library.loss import MeanSquaredError, SoftmaxCrossEntropyLoss
from library.trainer import Trainer
from library.optimizer import SGD

from library.help_functions import plot_digit, softmax


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
# model = NeuralNetwork(
#     layers=[Dense(neurons=89,
#                    activation=Tanh()),
#             Dense(neurons=10,
#                    activation=Linear())],
#     loss=SoftmaxCrossEntropyLoss(),
#     seed=20190501
# )


# model_3
# model = NeuralNetwork(
#     layers=[Dense(neurons=784, activation=Tanh()),
#             Dense(neurons=89, activation=Tanh()), 
#             Dense(neurons=10, activation=Linear())],
#     loss=SoftmaxCrossEntropyLoss(),
#     seed=20190501
# )


# # # Trener
# trainer = Trainer(model, SGD(0.1))
# trainer.fit(X_train, y_train, X_test, y_test,
#             epochs=50,
#             eval_every=10,
#             seed=20190119,
#             batch_size=60)



# calc_accuracy_model(model, X_test)





"""saving """
import pickle
# with open('model_1.pkl', 'wb') as file:
#     pickle.dump(model, file)

# print(y_train[0])


"""loading module"""
with open('model_1.pkl', 'rb') as file:
    model = pickle.load(file)








import numpy as np
from PIL import Image



def predict():
    some_digit = convert_to_array()
    arr = model.predict(some_digit)
    predicted_number = np.argmax(arr)
    print(f'\nPredicted number: {predicted_number}\n')
    procents = softmax(arr)[0]
    for i, proc in enumerate(procents):
        print(f'{i} -> {(proc * 100):.3f}%')
    
    return (predicted_number, procents[predicted_number])
    # plot_digit(some_digit)


def convert_to_array():
    # Załaduj obrazek i przekonwertuj na skalę szarości (opcjonalnie)
    image = Image.open('drawing.png').convert('L')
    # Przekształć obrazek na tablicę NumPy
    image_array = np.array(image)
    image_array = 255 - image_array

    # Spłaszcz tablicę 28x28 na 1x784
    flattened_array = image_array.flatten()

    # Jeśli potrzebujesz tablicy 1x784, dodaj dodatkowy wymiar
    flattened_array = flattened_array.reshape(1, -1)

    # print(flattened_array.shape)

    some_digit = flattened_array
    return some_digit






# some_digit = X_test[10]
# plot_digit(some_digit)
# print(some_digit)