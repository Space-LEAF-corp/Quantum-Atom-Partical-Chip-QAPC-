"""
Toy simulator producing phase-lock traces for the quantum atom chip concept.
This is non-physical, illustrative, and cannot be used for deployment.
"""

import math
from typing import List, Tuple
from qatom_core import Ring, lock_condition, envelope_stationary

def simulate(inner: Ring, middle: Ring, theta_star: float, T: float, dt: float, tol_phase: float) -> List[Tuple[float, bool, bool]]:
    t = 0.0
    result = []
    while t <= T:
        lc = lock_condition(inner, middle, theta_star, t, tol_phase)
        st = envelope_stationary(inner, middle, theta_star, t, tol_phase)
        result.append((t, lc, st))
        t += dt
    return result

if __name__ == "__main__":
    inner = Ring(m=1, omega=2*math.pi*1e9, phi=0.0)   # example GHz class
    middle = Ring(m=1, omega=0.0, phi=0.0)            # fixed lock
    data = simulate(inner, middle, theta_star=math.pi/2, T=1e-6, dt=1e-9, tol_phase=0.05)
    locks = sum(1 for _, lc, _ in data if lc)
    still = sum(1 for _, _, st in data if st)
    print({"samples": len(data), "locks": locks, "stationary": still})


---
