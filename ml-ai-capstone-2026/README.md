# BBO Capstone Project - Black Box Optimization

## Overview
Optimized 8 unknown functions over 13 weeks using Bayesian optimization with Gaussian Process surrogates and adaptive per-function strategies.

## Key Results
- F5: Improved 28% (984 → 8662)
- F7: Improved 21% (0.679 → 0.825)  
- F3: Improved 62% (-0.476 → -0.196)
- F4: Improved 25.7% (-24.5 → -18.2)

## Strategy
**Weeks 1-3:** Exploration - tested broad parameter ranges to understand landscapes.
**Weeks 4-9:** Adaptive learning - used Gaussian Process to predict good regions, different β values per function.
**Weeks 10-13:** Exploitation - locked into high-ROI functions, refined uncertainties.

## Repository Structure
- `code/`: Python implementation (GP, UCB, optimizer)
- `data/`: Week-by-week inputs and outputs
- `notebooks/`: 13 Jupyter notebooks with analysis
- `results/`: Performance summaries

## Key Learning
Started with random exploration, evolved to systematic GP-guided strategy. Learned early that treating each function differently (not one-size-fits-all) made a real difference in results.

See `notebooks/` for week-by-week analysis.
