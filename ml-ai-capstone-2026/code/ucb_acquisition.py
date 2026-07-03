import numpy as np

class UCB:
    """Upper Confidence Bound acquisition function."""
    
    def __init__(self, beta=2.5):
        self.beta = beta
    
    def evaluate(self, mean, std):
        """UCB = mean + beta * std"""
        return mean + self.beta * std
    
    def select_next_point(self, candidates, gp):
        """Select next point from candidates using UCB."""
        mean, std = gp.predict(candidates)
        ucb_scores = self.evaluate(mean, std)
        next_idx = np.argmax(ucb_scores)
        return candidates[next_idx]
