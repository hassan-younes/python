# Robotic Arm Forward Kinematics

## Overview
This repository contains a Python implementation for **forward kinematics of a 6-DOF robotic arm** using the [Modern Robotics library](https://pypi.org/project/modern-robotics/). 

The project calculates the end-effector pose in both **space frame** and **body frame**, and verifies their equivalence within a specified numerical tolerance.  

This is ideal for learning:
- Robot kinematics
- Manipulator analysis
- Mechatronics engineering applications

---

## Features
- Compute **forward kinematics** using **Space Frame representation**.
- Compute **forward kinematics** using **Body Frame representation**.
- Verify the results using a **numerical tolerance**.
- Easily adaptable for different robots by updating:
  - `M` (home configuration)
  - `Slist` (space frame screw axes)
  - `Blist` (body frame screw axes)
  - `thetalist` (joint angles)

---

## Requirements
- Python 3.7+
- [NumPy](https://numpy.org/)
- [Modern Robotics Python library](https://pypi.org/project/modern-robotics/)

Install dependencies via pip:

```bash
pip install numpy modern_robotics
