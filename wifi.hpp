#include <Arduino.h>
#include "lcd.hpp"
#include "secret.hpp"

void pc2esp() {
    if (Serial.available() > 0) {
        Serial1.print((char)Serial.read());
    }
}

void esp2pc() {
    if (Serial1.available() > 0) {
        Serial.print((char)Serial1.read());
    }
}

/* 명령을 보내고 500ms 만큼 기다리는 함수
*/
void cmd2esp(char* cmd, unsigned long timeout) {
    Serial1.println(cmd);
    unsigned long s = millis();
    while (millis() - s < timeout) {
        esp2pc();
    }
}

void sendData(char* data) {
    char dBuf[30];
    sprintf(dBuf, "AT+CIPSEND=%d", strlen(data));
    cmd2esp(dBuf, 500);
    Serial1.println(data);
    cmd2esp(data, 1000);
}

void connect() {
    char tempBuf[80];

    delay(2000);
    lcdPrint(0, "init WIFI 1/5");
    cmd2esp("AT", 500); // \r\n, OK\n
    lcdPrint(0, "init WIFI 2/5");
    cmd2esp("AT+CWMODE=1", 500);
    lcdPrint(0, "init WIFI 3/5");
    sprintf(tempBuf, "AT+CWJAP=\"%s\",\"%s\"", WIFI_NAME, WIFI_PASSWORD);
    cmd2esp(tempBuf, 5000);
    lcdPrint(0, "init WIFI 4/5");
    sprintf(tempBuf, "AT+CIPSTART=\"UDP\",\"%s\",%s", UDP_IP, UDP_PORT);
    cmd2esp(tempBuf, 5000);
    lcdPrint(0, "init WIFI 5/5");
}
