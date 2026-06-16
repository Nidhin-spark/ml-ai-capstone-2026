# Datasheet for BBO Capstone Project Dataset

## Motivation

This dataset documents 10 rounds of sequential black-box optimization across 8 unknown functions using a Gaussian Process surrogate with UCB acquisition. It captures iterative decision-making under uncertainty with limited query budgets.

Primary purpose: Understanding optimization strategy under uncertainty
Secondary purposes: Validating surrogate models, studying exploration-exploitation, demonstrating transparent ML workflows
Context: Imperial College London, Professional Certificate in ML & AI, Stage 2 Capstone Project (Modules 12-25)

## Composition

Core data: 80 total observations (10 rounds × 8 functions)

Function | Dimensions | Queries | Outputs
F1-F2 | 2D | 10 each | 10 each
F3 | 3D | 10 | 10
F4-F5 | 4D | 10 each | 10 each
F6 | 5D | 10 | 10
F7 | 6D | 10 | 10
F8 | 8D | 10 | 10

Format:
- Inputs: Hyphen-separated decimals, 6 decimal places (e.g., 0.450000-0.550000)
- Range: [0.0, 1.0] per dimension
- Outputs: Scalar floating-point values (range varies by function)
- Missing data: None (all queries evaluated)
- Quality: Exact oracle responses; no approximation or filtering

## Collection Process

Queries selected using Gaussian Process with UCB acquisition function. Strategy evolved:

Rounds 1-3 (Exploration): High UCB beta (2.5-3.5), broad coverage

Rounds 4-7 (Adaptation): Per-function beta tuning (1.0-3.5), tight clusters around improvements (F5, F7); broader for stalled functions (F1, F6)

Rounds 8-10 (Exploitation + Risk Management): Low beta for high-ROI functions (F5, F7); higher beta for plateaus (F1, F6); occasional off-model sanity checks

Timeline: Week 1 Module 12 to Week 10 Module 20 (10 weeks, one query per function per week)

## Preprocessing & Uses

Preprocessing: None. Raw oracle outputs retained to preserve function behavior.

Intended uses:
- Studying optimization under uncertainty
- Validating surrogate model assumptions
- Teaching exploration-exploitation trade-offs
- Analyzing sampling bias and coverage

Inappropriate uses:
- Claiming ground-truth function forms (functions unknown)
- Generalizing to real-world without revalidation
- Using as benchmark for hyperparameter optimization
- Inferring function properties with high confidence (sparse 8D)

## Distribution & Maintenance

Location: Public GitHub repository
Curator: Nidhin
Status: Complete (10 rounds submitted)
Updates: None planned (historical record)
Support: Via GitHub issues

## Limitations & Biases

Sampling bias: 60% of queries in [0.3, 0.7]; boundaries underexplored - may miss boundary optima

High-dimensional sparsity: F8 (8D) has only 10 points - extreme uncertainty in unexplored regions

Function-dependent structure: F5/F7 have dense exploratory data; F1/F6 have clustered data - different dataset characteristics per function

Single trajectory: One optimization path per function - no statistical robustness; results may not generalize

Temporal bias: Recent queries may be more representative due to strategy evolution

Selection bias: Queries chosen by model trained on accumulated data (not random)

## Conclusion

This dataset demonstrates transparent, iterative black-box optimization. Primary value is reproducibility and pedagogical clarity rather than optimal function values. Users should acknowledge sampling biases, especially in high-dimensional spaces, and treat insights as hypotheses.

For full context, see the accompanying Model Card.
