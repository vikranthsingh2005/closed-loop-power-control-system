import numpy as np

class DCPowerStage:
    """
    First-order DC power stage model:
    dV/dt = (1/RC)(Vin - Vout)
    """

    def __init__(self, R=1.0, C=0.01):
        self.R = R
        self.C = C
        self.Vout = 0.0

    def step(self, Vin, dt):
        dVdt = (1 / (self.R * self.C)) * (Vin - self.Vout)
        self.Vout += dVdt * dt
        return self.Vout
