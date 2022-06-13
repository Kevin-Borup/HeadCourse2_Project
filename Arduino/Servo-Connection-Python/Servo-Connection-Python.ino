#include <Servo.h>
Servo gate;
int gateDegrees;

void setup() {
  // put your setup code here, to run once:
  gate.attach(2);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    gateDegrees = Serial.parseInt();
    gate.write(gateDegrees);
  }
  delay(1);
}
