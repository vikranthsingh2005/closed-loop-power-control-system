import numpy as np


def calculate_overshoot(response, target):
    peak = np.max(response)
    overshoot = ((peak - target) / target) * 100
    return max(0, overshoot)


def calculate_settling_time(time, response, target, tolerance=0.02):
    lower_bound = target * (1 - tolerance)
    upper_bound = target * (1 + tolerance)

    for i in range(len(response)):
        if np.all((response[i:] >= lower_bound) &
                  (response[i:] <= upper_bound)):
            return time[i]

    return np.nan
