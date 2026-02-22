import numpy as np
import pandas as pd

from simulation import run_simulation
from analysis.performance_metrics import (
    calculate_overshoot,
    calculate_settling_time
)

# PID parameter ranges
kp_values = [0.5, 1.0, 2.0, 3.0]
ki_values = [0.1, 0.5, 1.0]
kd_values = [0.0, 0.1]

results = []

print("Starting PID sweep...")

for kp in kp_values:
    for ki in ki_values:
        for kd in kd_values:
            t, v = run_simulation(kp=kp, ki=ki, kd=kd)

            overshoot = calculate_overshoot(v, target=5.0)
            settling_time = calculate_settling_time(t, v, target=5.0)

            results.append({
                "Kp": kp,
                "Ki": ki,
                "Kd": kd,
                "Overshoot (%)": overshoot,
                "Settling Time (s)": settling_time
            })

results_df = pd.DataFrame(results)

# Save CSV in root directory
results_df.to_csv("pid_sweep_results.csv", index=False)

print("PID sweep completed.")
print("Results saved to pid_sweep_results.csv")
