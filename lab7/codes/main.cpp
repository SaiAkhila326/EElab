#include "Arduino.h"

const int clockPin = 3;  // Pin for clock signal

void setup() {
    pinMode(clockPin, OUTPUT);
}

void loop() {
    digitalWrite(clockPin, HIGH);
    delay(1000);  // Adjust delay for visible frequency on CRO (1Hz for slow counting)
    
    digitalWrite(clockPin, LOW);
    delay(1000);  // Same delay to produce a square wave
}

