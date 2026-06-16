Model Card: BBO Capstone Optimization Strategy

Overview

Name: Adaptive Gaussian Process + UCB Optimization Strategy

Type: Surrogate-based black-box optimization

Version: 1.0 (10 rounds, 80 total evaluations)

Developer: Nidhin

Date: 16/6/26

Documentation date: Module 21.2 Capstone


Intended Use

Primary Use Cases


✓ Maximizing unknown functions when evaluation is expensive
✓ Sequential decision-making under uncertainty
✓ Educational study of exploration-exploitation trade-offs
✓ Demonstrating transparent ML workflow


Unsuitable Use Cases


✗ Real-world optimization without significant revalidation
✗ High-stakes applications (medical, safety-critical)
✗ Replacing rigorous experimental design in practice
✗ Assuming generalizability beyond synthetic functions



Details

Strategy Overview

The approach combines three elements:


Surrogate Model: Gaussian Process with RBF kernel
Acquisition Function: Upper Confidence Bound (UCB)
Adaptive Meta-Strategy: Function-specific tuning based on observed behavior


Evolution Across 10 Rounds

Rounds 1-3: Broad Exploration


Objective: Understand basic landscape
UCB beta: High (2.5-3.5) to encourage uncertainty-driven sampling
Query pattern: Wide distribution across [0, 1]^d
Result: Identified improving vs stalled functions


Rounds 4-7: Adaptive Differentiation


Objective: Refine per-function strategy
UCB beta: Adjusted per function (1.0-3.5)
Query pattern: Tight clusters around improvements (F5, F7); broader for stalled (F1, F6)
Result: Clear separation between high-ROI and low-ROI regions


Rounds 8-10: Exploitation + Risk Management


Objective: Maximize best-known value while hedging overconfidence
UCB beta: Conservative (1.0-2.0) for improving functions; exploratory (3.0+) for
stalled ones
Query pattern: Local refinement around peaks; occasional off-model sanity checks
Result: Achieved best-known values; identified model limitations


Technical Details

Gaussian Process Configuration:


Kernel: RBF (Radial Basis Function)
Lengthscale: 0.2 (initial); 0.5-1.0 (later rounds, function-dependent)
Noise assumption: 1e-6 (early rounds) → 0.01 (later rounds)
Optimization: Fit to all available observations each round


Acquisition Function:


Type: Upper Confidence Bound (UCB)
Formula: μ(x) + β·σ(x)
Beta schedule: Per-function, adaptive

F1 (plateau): β = 3.0 (exploration)
F2-F4 (mixed): β = 2.0 (balanced)
F5, F7 (improving): β = 1.0-1.5 (exploitation)
F6 (plateau): β = 2.5 (moderate exploration)



Candidate pool: 5000 random points, UCB-scored, top-ranked selected


Meta-Strategy Logic:

if function shows consistent improvement:
    decrease beta (exploit promising region)
elif function shows plateau despite varied attempts:
    increase beta (explore new regions)
else (mixed signals):
    maintain balanced beta


Performance

Results Summary

FunctionDimRound 1 BestRound 10 BestImprovementStrategyF12D~0.0~0.00%Exploration (plateau)F22D0.8470.9127.7%BalancedF33D-0.476-0.196+62%ExploitationF44D-24.5-18.2+25.7%BalancedF54D9841258+27.9%ExploitationF65D-0.342-0.289+15.5%ExplorationF76D0.6790.825+21.5%ExploitationF88D7.287.95+9.2%Balanced

Metrics


Primary metric: Best-known value per function (absolute improvement)
Secondary metric: Improvement rate (% of queries beating previous best)

F5, F7: 80-90% improvement rate
F2-F4, F6: 40-60% improvement rate
F1, F8: <30% improvement rate



Tertiary metric: Sample efficiency (improvement per query)


What These Metrics Represent


High improvement rate indicates well-understood function landscape
Low improvement rate indicates plateau or model mismatch
Absolute improvement varies by function scale; percentage improvement is more comparable



Assumptions and Limitations

Core Assumptions


Smoothness: GP assumes local smoothness (nearby points correlate)

Valid for: F3, F4, F5, F7
Invalid for: F1 (extremely narrow peak), F8 (sparse 8D coverage)



Stationarity: Function properties remain stable across rounds

Valid assumption; no evidence of drift
Irrelevant for static functions, but noted



Exploitable structure: Functions contain patterns worth finding

Valid for: F5, F7 (clear improvement trajectory)
Questionable for: F1, F6 (minimal responsiveness)





Known Limitations


High-dimensional sparsity: F8 (8D) has only 10 observations

Consequence: Extreme uncertainty in unexplored regions
Risk: Apparent improvements may be noise, not structure



Sampling bias: 60% of queries in [0.3, 0.7]; boundaries underexplored

Consequence: May miss boundary optima
Risk: Strategy overfits to middle region



Single trajectory: One optimization path per function

Consequence: No statistical robustness or confidence intervals
Risk: Results may not generalize; lucky/unlucky runs indistinguishable



Limited query budget: 10 queries insufficient for rigorous optimization

Consequence: Early stops likely; full convergence unlikely
Risk: Reported optima are not true function maxima





Failure Modes


Overconfidence on F1: Model assumes F1 is explorable; it may not be
Underfitting F8: Model cannot capture 8D structure with 10 points
Getting stuck: High-beta/low-beta switching could oscillate rather than converge



Ethical Considerations

Transparency as Trust-Building

This model card documents:


✓ What the approach does
✓ When it works and when it doesn't
✓ Assumptions that might fail
✓ Sampling biases that could mislead


Why this matters: Users can make informed decisions about when (and when not)
to apply the strategy. Hiding limitations would create false confidence.

Reproducibility and Real-World Adaptation

By documenting:


The exact UCB beta schedule
The acquisition function details
The hyperparameter choices
The strategy evolution


...other researchers can:


Reproduce results (verify claims)
Adapt to new functions (transfer learning)
Improve the approach (build on weaknesses)
Critique methodology (identify flaws)


Appropriate Skepticism

This model card encourages users to:


Treat results as hypotheses, not facts
Test applicability before real-world deployment
Acknowledge that 10 rounds is exploratory, not conclusive
Recognize high-dimensional challenges



Improvements and Future Work

Potential Enhancements


Run multiple trials per function to assess statistical robustness
Implement Bayesian optimization for hyperparameter tuning itself
Use sparse GP approximations for higher-dimensional functions
Add explicit uncertainty quantification in query selection
Implement curriculum learning (start simple, increase difficulty)


Why Current Structure is Sufficient

For an educational capstone project, the current model card is sufficient because:


It documents what was actually done (not idealized claims)
It acknowledges limitations honestly
It provides enough detail for peer review and reproduction
It supports learning about uncertainty in optimization


Adding extensive simulation studies or statistical analysis would exceed the scope
of a 10-round capstone; this card appropriately reflects that scope.
