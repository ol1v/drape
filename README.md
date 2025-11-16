# DRAPE: A simple heuristic metric for detection performance
<p align="center"><img src=logo_small.png></p>

**DRAPE** stands for **D**etection **R**eliability **A**nd **P**recision **E**fficiency which is basically a unified index (score) that quantifies:

- **Reliability**: Are the detections actually finding true attacks? (TP)
- **Precision Efficiency**: Are they doing so with minimal noise? (FP)

The algorithm outputs a simple heuristic metric to score detection performance using TP/FP counts. The index score can be either negative or positive with the extremes implying the following characteristics:

- Negative = noisy, unreliable detection.
- Positive = precise, efficient, valuable detection.

The index is a composite measure of the individual TP/FP data points which can be used to measure detection/rule performance over time.

DRAPE reveals whether a rule is _signal-dominant_ (+) or _noise-dominant_ (–) by inspecting the number of its TP and FPs alerts over a period of time.

## How does it work? 
The formula rewards rules that spots a decent amount of threats (TP) with good precision, while penalizing noisy rules, especially those that haven't yet "proven" themselves with enough TPs.

The formula captures the real-world tradeoff between TP and FP figures better than precision or simple raw counts. Most single-number metrics are either:

- too forgiving of noise (TP-heavy rules look great even when they're a FP factory), or
- too punishing (precision destroys high-value, high-volume rules).

DRAPE models that tradeoff how detection engineers think in practice:

- High TP → good
- High precision → better
- Extremely noisy rules → bad
- Slight noise on high-value rules → acceptable

This mirrors actual triage experience so I encourage you to try it out.

## Implementations
- Python: [drapeindex.py](drapeindex.py)
- Splunk (SPL): [drapeindex.spl](/drapeindex.spl)

### Outpout Sample (v1.0)
<p align="center"><img src=drapev1_output.png></p>

## More details
Intro blog post on Detect.FYI website: 

