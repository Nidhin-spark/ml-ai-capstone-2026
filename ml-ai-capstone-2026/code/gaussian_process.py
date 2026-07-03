import numpy as np
from scipy.spatial.distance import cdist

class SimpleGaussianProcess:
    """Minimal Gaussian Process for BBO."""
    
    def __init__(self, length_scale=0.2, noise=0.01):
        self.X = None
        self.y = None
        self.length_scale = length_scale
        self.noise = noise
    
    def fit(self, X, y):
        """Fit GP to observed data."""
        self.X = np.array(X)
        self.y = np.array(y)
    
    def predict(self, X_test):
        """Return mean and std predictions."""
        if self.X is None:
            return np.zeros(len(X_test)), np.ones(len(X_test))
        
        # RBF kernel distances
        distances = cdist(X_test, self.X, metric='euclidean')
        K = np.exp(-distances**2 / (2 * self.length_scale**2))
        
        # Weighted average as mean
        mean = np.dot(K, self.y) / K.sum(axis=1)
        
        # Uncertainty based on distance to nearest point
        min_dist = distances.min(axis=1)
        std = np.exp(-min_dist / self.length_scale)
        
        return mean, std
