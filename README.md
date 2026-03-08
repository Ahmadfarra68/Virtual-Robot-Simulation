Virtual Robot Simulation
Student Name: Ahmad AlFarra
Course: Robotics Programming
Project Type: Individual

1. Project Overview
This project involves designing and implementing a virtual autonomous robot using Python. The robot operates in a simulated 2D grid-based environment, making decisions based on virtual sensor inputs to reach a defined goal while avoiding obstacles .

2. Core Requirements Implemented2D Environment: A 10x10 coordinate-based map featuring boundaries and obstacles .Robot Model: Tracks position $(x, y)$, orientation, and internal states (Moving, Idle, Avoiding) .Movement System: Defined commands for forward motion and turning with integrated collision prevention .Simulation Loop: Step-by-step execution with clear updates of the robot's state per step .

3. Extension Tracks (Chosen TWO)In addition to core requirements, I have implemented the following extensions:Extension A: Path Planning: Implementation of the $A^*$ Search Algorithm to allow the robot to autonomously find the most efficient path to the target .Extension C: Finite State Machine (FSM): The robot's behavior is managed through clearly defined states: IDLE, PLANNING, MOVING, and FINISHED .

4. Algorithm & LogicThe robot follows a logic-based control system:Sensing: The robot checks for obstacles or boundaries in its next potential position.Decision-Making: Based on sensor data, the robot either moves forward or transitions to a "Planning" state to recalculate its path using $A^*$ logic .Execution: Updates coordinates and orientation based on the calculated path.

5. How to Run
Ensure you have Python 3.x installed.

Navigate to the project folder.

Run the following command:

Bash
python robot_sim.py
