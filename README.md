# MQLPY - Modular Algorithmic Trading for Python

```cpp
// Switching Flight Modes 

const int PWM_PIN = 2; // The PWM signal goes to pin 2 

const int RELAY_PIN = 8; // The relay signal goes to pin 8 

const int OUTPUT_PIN = 10; // The algorithms go to pin 10 

unsigned long PWM;

void setup() {

    pinMode(PWM_PIN, INPUT); // The PWM signal is assigned as an input 

    PWM = pulseIn(PWM_PIN, HIGH);

    pinMode(RELAY_PIN, OUTPUT); // The relay signal is assigned as an output 

    pinMode(OUTPUT_PIN, OUTPUT); // The algorithms are assigned as an output 

    digitalWrite(RELAY_PIN, HIGH); // input taken from RC (pilot) by default 

}

void loop() {

    if (PWM < 1500) {

        digitalWrite(RELAY_PIN, LOW); // Input taken from Arduino if operator switches flight mode 

        Altitude Hold Algorithm

        Stabiliser Algorithm

    }

}

// Altitude Hold 

#include <PID_v1.h>

double altitude() {

    assign Echo pin of HC - SR04 to pin 15 of 2n d PCA9685

    assign Trig pin of HC - SR04 to pin 14 of 2n d PCA9685

    long duration; // Variable for the duration of sound wave travel 

    int distance; // Variable for the distance measurement 

    pinMode(trigPin, OUTPUT); // Sets the trigPin as an OUTPUT 

    pinMode(echoPin, INPUT); // Sets the echoPin as an INPUT 

    digitalWrite(trigPin, LOW); // Clears the trigPin condition 

    delayMicroseconds(2);

    digitalWrite(trigPin, HIGH);

    delayMicroseconds(10); // Sets the trigPin HIGH (ACTIVE) for 10 microseconds 

    digitalWrite(trigPin, LOW); // Reads echoPin, returns the sound wave travel time in microseconds 

    duration = pulseIn(echoPin, HIGH);

    distance = duration * 0.034 / 2; // Calculates the distance 

}

double Setpoint_A, Input_A, Output_A; // Define Variables we'll be connecting to 

PID Alt_PID( & Input_A, & Output_A, & Setpoint_A, 70, 110, 5, DIRECT); // Specify links and initial tuning parameters 

void setup() {

    Input_A = altitude();

    Setpoint_A = altitude(); // Initialize the variables we're linked to 

    Alt_PID.SetMode(AUTOMATIC)
}; // Turn the PID on 

void loop() {

    while (PWM < 1500) {

        Input_A = altitude();

        if (error = 0 or passes Setpoint_A) {

            integral = 0;

        }

        if (error > 1.0 or error < 0.1) {

            integral = 0; // Prevents the integral from building up 

        }

        Alt_PID.Compute();

        analogWrite(OUTPUT_PIN, Output_A);

    }

}

// Stabiliser 

double Setpoint_X, Input_X, Output_X;

double Setpoint_Y, Input_Y, Output_Y;

PID X_PID( & Input_X, & Output_X, & Setpoint_X, 70, 110, 5, DIRECT);

PID Y_PID( & Input_Y, & Output_Y, & Setpoint_Y, 70, 110, 5, DIRECT);

void setup() {

    Input_X = Roll; // Roll in radians 

    Input_Y = Pitch; // Pitch in radians 

    Setpoint_X = 0;

    Setpoint_Y = 0;

    X_PID.SetMode(AUTOMATIC);

    Y_PID.SetMode(AUTOMATIC);

}

void loop() {

    while (PWM < 1500) {

        Input_X = Roll;

        Input_Y = Pitch;

        if (error = 0 or passes Setpoint_X or passes Setpoint_Y) {

            integral = 0;

        }

        if (error > 1.0 or error < 0.1) {

            integral = 0;

        }

        X_PID.Compute();

        Y_PID.Compute();

        analogWrite(OUTPUT_PIN, Output_X);

        analogWrite(OUTPUT_PIN, Output_Y);

    }

}
```
