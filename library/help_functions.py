import numpy as np
from scipy.special import logsumexp


def permute_data(X, y):
    perm = np.random.permutation(X.shape[0])
    return X[perm], y[perm]

def softmax(x, axis=None):
    return np.exp(x - logsumexp(x, axis=axis, keepdims=True))