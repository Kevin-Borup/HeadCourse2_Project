#include <Servo.h>
Servo gate;

void setup() {
  // put your setup code here, to run once:
  gate.attach(2);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    int gateDegrees = Serial.read();
    Serial.write(gateDegrees);
    gate.write(gateDegrees);
  }
}
