import numpy as np
import matplotlib.pyplot as plt

from system_model.power_stage import DCPowerStage
from control.pid_controller import PIDController


def run_simulation(Kp=5, Ki=50, Kd=0.01, setpoint=5.0,
                   R=1.0, C=0.05,
                   dt=0.001, t_end=1.0,
                   plot=False):

    time = np.arange(0, t_end, dt)

    power_stage = DCPowerStage(R=R, C=C)
    controller = PIDController(Kp=Kp, Ki=Ki, Kd=Kd, setpoint=setpoint)

    voltage_history = []

    for t in time:
        Vin = controller.compute(power_stage.Vout, dt)
        Vout = power_stage.step(Vin, dt)
        voltage_history.append(Vout)

    voltage_history = np.array(voltage_history)

    if plot:
        plt.figure()
        plt.plot(time, voltage_history)
        plt.title("Closed-Loop Voltage Response")
        plt.xlabel("Time (s)")
        plt.ylabel("Output Voltage (V)")
        plt.grid()
        plt.savefig("voltage_response.png")
        plt.show()

    return time, voltage_history


# Only run when executed directly
if __name__ == "__main__":
    run_simulation(plot=True)
