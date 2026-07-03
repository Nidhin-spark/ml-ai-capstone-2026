import numpy as np
import json
import os
from gaussian_process import SimpleGaussianProcess
from ucb_acquisition import UCB

class BayesianOptimizer:
    """Main optimization loop."""
    
    def __init__(self, num_functions=8):
        self.gps = {f'F{i+1}': SimpleGaussianProcess() for i in range(num_functions)}
        self.ucbs = {f'F{i+1}': UCB(beta=2.5) for i in range(num_functions)}
        self.history = {f'F{i+1}': {'inputs': [], 'outputs': []} for i in range(num_functions)}
    
    def fit_week_data(self, week_dir):
        """Fit GPs after receiving week results."""
        if os.path.exists(f'{week_dir}/outputs.json'):
            with open(f'{week_dir}/outputs.json') as f:
                outputs = json.load(f)
            with open(f'{week_dir}/inputs.json') as f:
                inputs = json.load(f)
            
            for func in self.gps.keys():
                if func in inputs and func in outputs:
                    inp = [inputs[func]]
                    out = [outputs[func]]
                    self.history[func]['inputs'].extend(inp)
                    self.history[func]['outputs'].extend(out)
                    self.gps[func].fit(self.history[func]['inputs'], 
                                      self.history[func]['outputs'])
    
    def get_next_queries(self, num_candidates=1000):
        """Generate next week's queries using GP + UCB."""
        next_queries = {}
        
        for func_name, gp in self.gps.items():
            # Generate random candidates
            func_dim = 2 + (list(self.gps.keys()).index(func_name) % 7)  # 2D to 8D
            candidates = np.random.uniform(0, 1, (num_candidates, func_dim))
            
            # Select via UCB
            next_point = self.ucbs[func_name].select_next_point(candidates, gp)
            next_queries[func_name] = next_point.tolist()
        
        return next_queries

if __name__ == '__main__':
    print("BBO Optimizer initialized. Use with week-by-week data.")
