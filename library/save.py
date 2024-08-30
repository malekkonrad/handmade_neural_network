import pickle
import datetime

# from library.neural_network import NeuralNetwork


def save_model(model):
    # with open(f'model_.pkl', 'wb') as outp:
    pass

class NN:
    def __init__(self, arr) -> None:
        self.param = arr

class Company(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

# with open('company_data.pkl', 'wb') as outp:
#     company1 = Company('banana', 40)
#     pickle.dump(company1, outp, pickle.HIGHEST_PROTOCOL)

#     company2 = Company('spam', 42)
#     pickle.dump(company2, outp, pickle.HIGHEST_PROTOCOL)

#     arr = [1,2,3,4]
#     nn = NN(arr)
#     pickle.dump(nn, outp, pickle.HIGHEST_PROTOCOL)

# del company1
# del company2
# del nn

# with open('company_data.pkl', 'rb') as inp:
#     company1 = pickle.load(inp)
#     print(company1.name)  # -> banana
#     print(company1.value)  # -> 40

#     company2 = pickle.load(inp)
#     print(company2.name) # -> spam
#     print(company2.value)  # -> 42

#     nnn = pickle.load(inp)
#     print(nnn.param)


print(datetime.datetime.today())
