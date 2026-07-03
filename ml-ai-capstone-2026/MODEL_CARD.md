# Model Card: Adaptive Bayesian Optimization

## Approach
Gaussian Process surrogate with UCB acquisition function. Tuned β values per function based on improvement patterns.


## Technical Details
- Surrogate: Gaussian Process, RBF kernel
- Acquisition: UCB with adaptive β
  - β=1.5 for improving functions (F5, F7)
  - β=3.0 for stalled functions (F1, F6)  
  - β=2.0 for balanced functions (F2-F4)
  - 

## Strategy
- **Weeks 1-3:** Random exploration (60% explore, 40% exploit)
- **Weeks 4-6:** Center-point and symmetric value testing
- **Weeks 7-9:** GP-guided with hyperparameter tuning
- **Weeks 10-13:** Exploit high-ROI regions, explore boundaries of stalled functions
- 

## Performance
- F5, F7: Strong improvements (28%, 21%)
- F3, F4: Moderate improvements (62%, 26%)
- F1, F6: Plateaued (found local optima early)
- F8: Slow improvement due to high dimensionality
- 

## Key Assumption
Functions exhibit local smoothness (nearby parameters → correlated outputs). Violated in narrow-peak regions like F1.


## Real-World Use
Practical for expensive-to-evaluate functions: drug discovery, hyperparameter tuning, engineering optimization.
