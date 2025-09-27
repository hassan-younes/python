# Robotic Arm Forward Kinematics using Modern Robotics
# Author: Hassan younes
# Date: 2025-09-20
# Description:
# This script computes the forward kinematics of a 6-DOF robotic arm
# using both Space Frame and Body Frame representations.
# It also checks if the two results match within a specified tolerance.

import modern_robotics as mr
import numpy as np
import math

# -------------------------
# Define robot parameters
# -------------------------

# Home configuration of the end-effector (M matrix)
M = [
    [1, 0, 0, 3.73205],
    [0, 1, 0, 0],
    [0, 0, 1, 2.73205],
    [0, 0, 0, 1]
]

# Screw axes in the space frame (Slist)
Slist = [
    [0,   0,   0,    0,    0,   0],
    [0,   1,   1,    1,    0,   0],
    [1,   0,   0,    0,    0,   1],
    [0,   0,   1.00, -0.73, 0,   0],
    [-1,  0,   0,    0,    0,  -3.73],
    [0,   1,   2.73, 3.73, 1,   0]
]

# Screw axes in the body frame (Blist)
Blist = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
    [0, 2.73, 3.73, 2, 0, 0],
    [2.73, 0.00, 0, 0, 0, 0],
    [0, -2.73, -1, 0, 1, 0]
]

# Joint angles (in radians)
pi = math.pi
thetalist = np.array([-pi/2, pi/2, pi/3, -pi/4, 1, pi/6])

# -------------------------
# Compute Forward Kinematics
# -------------------------

# Using Space Frame representation
T1 = mr.FKinSpace(M, Slist, thetalist)

# Using Body Frame representation
T2 = mr.FKinBody(M, Blist, thetalist)

# -------------------------
# Print Results
# -------------------------
print("Forward Kinematics (Space Frame) T1:")
print(T1, "\n")

print("Forward Kinematics (Body Frame) T2:")
print(T2, "\n")

# Check if the two matrices are equal within a tolerance
tolerance = 0.01
if np.allclose(T1, T2, atol=tolerance):
    print(f"T1 and T2 match within tolerance {tolerance}")
else:
    print(f"T1 and T2 do NOT match within tolerance {tolerance}")

# Optional: show element-wise differences
diff = np.abs(T1 - T2)
print("\nElement-wise differences:")
print(diff)
