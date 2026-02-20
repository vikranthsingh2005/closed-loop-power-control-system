import numpy as np
import matplotlib.pyplot as plt

from system_model.power_stage import DCPowerStage
from control.pid_controller import PIDController

# Simulation parameters
dt = 0.001
t_end = 1.0
time = np.arange(0, t_end, dt)

# Initialize system
power_stage = DCPowerStage(R=1.0, C=0.05)
controller = PIDController(Kp=5, Ki=50, Kd=0.01, setpoint=5)

voltage_history = []
control_history = []

for t in time:
    Vin = controller.compute(power_stage.Vout, dt)
    Vout = power_stage.step(Vin, dt)

    voltage_history.append(Vout)
    control_history.append(Vin)

plt.figure()
plt.plot(time, voltage_history)
plt.title("Closed-Loop Voltage Response")
plt.xlabel("Time (s)")
plt.ylabel("Output Voltage (V)")
plt.grid()
plt.savefig("voltage_response.png")
plt.show()
