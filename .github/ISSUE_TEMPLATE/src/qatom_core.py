"""
Quantum Atom Chip — invariant definitions
SPDX-License-Identifier: Stewardship-1.0+NWR
Copyright (c) Leif

This module encodes minimal invariants for a gyroscopic time-bubble around a single quantum emitter.
Changing these invariants requires explicit steward consent.
"""

from dataclasses import dataclass
import math

@dataclass(frozen=True)
class Ring:
    m: int            # azimuthal mode
    omega: float      # angular frequency (rad/s)
    phi: float        # phase (rad)

@dataclass(frozen=True)
class LockConfig:
    theta_star: float # merge angle (rad)
    tol_phase: float  # max phase drift allowed (rad)
    tol_angle: float  # max angular drift allowed (rad)

def phase(ring: Ring, theta: float, t: float) -> float:
    return ring.m * theta - ring.omega * t + ring.phi

def lock_condition(inner: Ring, middle: Ring, theta_star: float, t: float, tol_phase: float) -> bool:
    """Local stationarity: inner vs middle phase alignment within tolerance."""
    dphi = abs(phase(inner, theta_star, t) - phase(middle, theta_star, t))
    return dphi <= tol_phase

def envelope_stationary(inner: Ring, middle: Ring, theta_star: float, t: float, tol_phase: float) -> bool:
    """Approximate stillness: time derivative near zero via phase cancellation."""
    # derivative proxy: |omega_inner - omega_middle| small when aligned
    return abs(inner.omega - middle.omega) < (tol_phase * 1.0) and lock_condition(inner, middle, theta_star, t, tol_phase)


---
