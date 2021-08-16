#include "sensor.hpp"
#include "lcd.hpp"
#include "wifi.hpp"

int progress = 0;
char progressBuf[30] = "";

void setup() {
  Serial.begin(9600);
  Serial1.begin(9600);
  Serial.println("FASTAPI_UDP START");
  sensorInit();
  lcdInit();
  connect();
}

void loop() {
  progress += 1;
  
  delay(15000);
  sensorRead();
  lcdPrint(0, getSensorDataStr());

  sprintf(progressBuf, "%d", progress);
  lcdPrint(1, progressBuf);

  sendData(getSensorDataStr());
}

// AT
// AT+CWMODE=1
// AT+CWJAP?
// AT+CWJAP=
// AT+CIFSR
// AT+CIPSTART="UDP"
