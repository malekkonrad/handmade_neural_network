import numpy as np
from scipy.special import logsumexp


def permute_data(X, y):
    perm = np.random.permutation(X.shape[0])
    return X[perm], y[perm]

def softmax(x, axis=None):
    return np.exp(x - logsumexp(x, axis=axis, keepdims=True))



def normalize(a: np.ndarray):
    other = 1 - a
    return np.concatenate([a, other], axis=1)


def unnormalize(a: np.ndarray):
    return a[np.newaxis, 0]