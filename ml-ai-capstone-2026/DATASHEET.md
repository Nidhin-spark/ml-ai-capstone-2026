# Data Composition

## Overview
13 weeks of black-box function optimization. 8 functions, 2D to 8D dimensionality, total 104 queries.

## Functions
| Function | Dimension | Type | Best Found |
|----------|-----------|------|-----------|
| F1 | 2D | Unimodal | ~0 |
| F2 | 2D | Noisy | 0.912 |
| F3 | 3D | Drug discovery | -0.196 |
| F4 | 4D | Warehouse placement | -18.2 |
| F5 | 4D | Chemical yield | 8662 |
| F6 | 5D | Recipe optimization | -0.47 |
| F7 | 6D | Hyperparameter tuning | 0.825 |
| F8 | 8D | High-dimensional | 9.79 |

## Data Format
- Inputs: [0,1] normalized parameters per function dimension
- Outputs: Single scalar per query
- Structure: JSON per week, combined CSV file

## Limitations
- Only 13 samples per function (sparse for high-dimensional)
- Black-box functions (unknown structure)
- No ground truth optima available
- ~60% of queries clustered in [0.3, 0.7] range

## Appropriate Uses
- Portfolio example of Bayesian optimization
- Demonstrating per-function adaptive strategies
- Teaching exploration-exploitation trade-offs
