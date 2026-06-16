# Model Card: BBO Capstone Optimization Strategy

## Overview

Name: Adaptive Gaussian Process + UCB Optimization Strategy
Type: Surrogate-based black-box optimization
Version: 1.0 (10 rounds, 80 evaluations)
Developer: Nidhin
Date: 16/6/26

## Intended Use

Primary: Maximizing unknown functions with expensive evaluation; sequential decision-making under uncertainty; educational study of exploration-exploitation.

Unsuitable: Real-world optimization without revalidation; high-stakes applications; assuming generalizability beyond synthetic functions.

## Details

Strategy: Gaussian Process surrogate with RBF kernel + Upper Confidence Bound acquisition function + adaptive function-specific tuning.

Evolution:
- Rounds 1-3 (Exploration): High UCB beta (2.5-3.5), wide coverage
- Rounds 4-7 (Adaptation): Per-function beta tuning (1.0-3.5), tight clusters around improvements (F5, F7); broader for stalled (F1, F6)
- Rounds 8-10 (Exploitation): Conservative beta (1.0-2.0) for improving functions; exploratory (3.0+) for stalled; occasional off-model sanity checks

Technical:
- GP kernel: RBF, lengthscale 0.2 to 0.5-1.0
- Noise assumption: 1e-6 to 0.01
- UCB formula: mu(x) + beta * sigma(x)
- Beta schedule: F1=3.0, F2-F4=2.0, F5/F7=1.0-1.5, F6=2.5
- Candidate pool: 5000 random points, top-ranked selected

## Performance

Function | Dim | Round 1 | Round 10 | Improvement | Strategy
F1 | 2D | 0.0 | 0.0 | 0% | Exploration
F2 | 2D | 0.847 | 0.912 | 7.7% | Balanced
F3 | 3D | -0.476 | -0.196 | +62% | Exploitation
F4 | 4D | -24.5 | -18.2 | +25.7% | Balanced
F5 | 4D | 984 | 1258 | +27.9% | Exploitation
F6 | 5D | -0.342 | -0.289 | +15.5% | Exploration
F7 | 6D | 0.679 | 0.825 | +21.5% | Exploitation
F8 | 8D | 7.28 | 7.95 | +9.2% | Balanced

Improvement rates: F5/F7 (80-90%), F2-F4/F6 (40-60%), F1/F8 (less than 30%).

## Assumptions & Limitations

Core Assumptions:
1. Smoothness: GP assumes local correlation (valid for F3-F5, F7; invalid for F1, F8)
2. Exploitable structure: Functions contain patterns (valid for F5, F7; questionable for F1, F6)

Limitations:
1. High-dimensional sparsity: F8 (8D) with only 10 points - extreme uncertainty in unexplored regions
2. Sampling bias: 60% of queries in [0.3, 0.7]; boundaries underexplored - may miss optima
3. Single trajectory: No statistical robustness; results may not generalize
4. Limited budget: 10 queries insufficient for convergence

Failure modes: Overconfidence on F1 (not truly explorable); underfitting F8 (cannot capture 8D structure); oscillation between high/low beta.

## Ethical Considerations

This card documents what works, when it fails, assumptions that break, and biases that could mislead. Users can make informed decisions about applicability. Transparency enables reproducibility, adaptation, and critique. Encourages appropriate skepticism: treat results as hypotheses, acknowledge that 10 rounds is exploratory, recognize high-dimensional challenges.

## Future Work

- Run multiple trials for statistical robustness
- Bayesian optimization of hyperparameters
- Sparse GP for higher dimensions
- Explicit uncertainty quantification
- Curriculum learning
