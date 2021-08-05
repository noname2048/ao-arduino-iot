#include "sensor.h"

void setup() {
  Serial.begin(9600);
  sensorInit();
}

void loop() {
  delay(3000);
  sensorRead();
}
