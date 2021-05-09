# MQLPY - Modular Algorithmic Trading for Python

```cpp
// INITIAL SETUP 

// Call relevant MPU6050 and Servo libraries 

// define the 2 servo motors 

Servo Servo1

Servo Servo2

// Begin the serial monitor 

// Define the pins of the servo and gyro sensor 

// Initialise the gyro and input gyro offsets 

MAIN PROGRAM LOOP

// Get pitch, and roll values from the MPU6050 

// Convert pitch, roll values to radians 

Pitch = Pitch * 180 / pi

Roll = Roll * 180 / pi

// Set some constant that increases by 1 every iteration 

J = J++

// Wait for the first 300 recordings to have taken place (Initial values can be inaccurate) 

IF J > 300

// Average the next 300 recordings and store this value as a variable (drone must be level) 

NormalPitch = ∑pitch / 300

NormalRoll = ∑Roll / 300

// All values taken after the first 600 are compared to the normal orientation 

IF J > 600

PitchDiff = NormalPitch + Pitch

RollDiff = NormalRoll + Roll

// Map the values of the MPU6050 from -90 to 90 to 0 to 180 

Servo1Value = Map(PitchDiff, -90, 90, 0, 180)

Servo2Value = Map(RollDiff, -90, 90, 0, 180)

// Input mapped values to the servos 

Servo1(Servo1Value)

Servo2(Servo2Value)
```
