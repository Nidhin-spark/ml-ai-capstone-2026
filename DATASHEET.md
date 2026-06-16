Datasheet for BBO Capstone Project Dataset

Motivation

Why was the dataset created?

This dataset documents the iterative query history and function evaluations from a
10-round Black-Box Optimization (BBO) capstone project. It captures the sequential
decision-making process of optimizing eight unknown functions using a Gaussian
Process surrogate model with Upper Confidence Bound acquisition function.

What task or purpose does it support?


Primary purpose: Understanding optimization strategy under uncertainty with
limited query budgets
Secondary purposes: Validating surrogate modelling approaches, studying
exploration-exploitation trade-offs, demonstrating transparency in ML workflow
Research context: Imperial College London, Professional Certificate in ML & AI,
Stage 2 Capstone Project (Modules 12-25)



Composition

What does the dataset contain?

Core data: 80 total observations (10 rounds × 8 functions)


Per function: 10 query points and their corresponding scalar outputs
Format: Parameter vectors (dimensions 2-8) → Scalar performance values


Data structure per function:

Function 1 (2D):   10 queries → 10 outputs
Function 2 (2D):   10 queries → 10 outputs
Function 3 (3D):   10 queries → 10 outputs
Function 4 (4D):   10 queries → 10 outputs
Function 5 (4D):   10 queries → 10 outputs
Function 6 (5D):   10 queries → 10 outputs
Function 7 (6D):   10 queries → 10 outputs
Function 8 (8D):   10 queries → 10 outputs

Instances and Missing Data


Total instances: 80 query-response pairs
Missing data: None. All queries were evaluated; no failed submissions.
Gaps: By design, functions 1-8 are unknown (no ground truth provided)
Data quality: All outputs are exact oracle responses; no approximation or
filtering applied


Data Format


Input format: Hyphen-separated decimal strings, 6 decimal places

Example: 0.450000-0.550000 (2D function)
Range: [0.0, 1.0] per dimension



Output format: Scalar floating-point values (range varies by function)
Storage: Raw CSV or JSON (structure TBD by developer)



Collection Process

How were the queries generated?

Queries were selected using a Gaussian Process surrogate model with Upper Confidence
Bound (UCB) acquisition function. Selection strategy evolved across 10 rounds:

Round 1-3 (Exploration phase):


High UCB beta values (2.5-3.5)
Broad coverage of [0, 1]^d
Goal: understand basic function landscape


Round 4-7 (Adaptation phase):


Function-specific beta adjustment
Clustering around improving regions
Goal: balance continued exploration with exploitation


Round 8-10 (Exploitation + Risk Management):


Low beta for high-ROI functions (F5, F7)
Higher beta for plateau functions (F1, F6)
Occasional off-model sanity checks
Goal: maximize best-known value while hedging against overconfidence


Time Frame


Start: Week 1 of Module 12
End: Week 10 of Module 20
Frequency: One query per function per week
Total duration: 10 weeks


Annotated Strategy

Each query includes implicit metadata:


Which round (1-10)
Which strategy phase (exploration / adaptation / exploitation)
Reasoning based on prior observations
Full documentation in accompanying model card



Preprocessing and Uses

Preprocessing Steps

None applied. Raw oracle outputs are retained unmodified to preserve original
function behavior.

Intended Uses


✓ Studying optimization under uncertainty
✓ Validating surrogate model assumptions
✓ Teaching exploration-exploitation trade-offs
✓ Analyzing sampling bias and coverage
✓ Documenting transparent ML process


Inappropriate Uses


✗ Claiming ground-truth function forms (functions remain unknown)
✗ Generalizing strategy to real-world applications without revalidation
✗ Using as benchmark for hyperparameter optimization (synthetic, limited scope)
✗ Inferring function properties with high confidence (sparse 8D data)



Distribution and Maintenance

Availability

Located in public GitHub repository



Curator: Nidhin
Current status: Complete (10 rounds submitted)
Updates: No further updates planned; dataset is historical record
Support: Available for clarification via GitHub issues or direct contact



Limitations and Biases

Known Limitations


Sampling bias: 60% of queries concentrated in [0.3, 0.7]; boundaries underexplored
High-dimensional sparsity: F8 has only 10 points in 8-dimensional space
Function-dependent structure: F5/F7 have dense, exploratory data; F1/F6 have
clustered data
Single optimization trajectory: Each function has one optimization path, not
multiple runs for statistical robustness


Potential Biases


Regional bias: Strategy converged to middle of search space after observing
early success there; may miss boundary optima
Temporal bias: Recent queries may be more representative than early ones due
to strategy evolution
Selection bias: Queries chosen by model trained on accumulated data (not random)



Conclusion

This dataset documents a transparent, iterative approach to black-box optimization.
Its primary value lies in reproducibility and pedagogical clarity rather than
achieving optimal function values. Users should be aware of sampling biases,
especially in high-dimensional spaces, and treat insights as hypotheses rather
than ground truth.

For full context, see the accompanying Model Card and GitHub repository.
