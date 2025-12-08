import math
from src.qatom_core import Ring, lock_condition, envelope_stationary

def test_lock_condition_basic():
    inner = Ring(m=1, omega=0.0, phi=0.0)
    middle = Ring(m=1, omega=0.0, phi=0.0)
    assert lock_condition(inner, middle, theta_star=math.pi/2, t=0.0, tol_phase=1e-3)

def test_stationary_requires_small_frequency_gap():
    inner = Ring(m=1, omega=2*math.pi*1e9, phi=0.0)
    middle = Ring(m=1, omega=2*math.pi*1e9, phi=0.0)
    assert envelope_stationary(inner, middle, theta_star=0.0, t=0.0, tol_phase=0.05)


---
