# DRAPE Index
![test](logo2.png)
DRAPE stands for Detection Reliability And Precision Efficiency which is basically a unified index (score) that quantifies:
Reliability → Are the detections actually finding true attacks? (TP)
Precision Efficiency → Are they doing so with minimal noise? (FP)

The index score can be either negative or positive with the extremes implying the following characteristics:
Negative = noisy, unreliable detection.
Positive = precise, efficient, valuable detection.

The index is a composite measure of the individual TP/FP data points which can be used to measure detection/rule performance over time.
DRAPE reveals whether a rule is signal-dominant (+) or noise-dominant (–) by inspecting the number of its TP and FPs alerts over a period of time.
