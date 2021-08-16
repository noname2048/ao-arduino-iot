#pragma once
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

void cmd2esp(String cmd, unsigned long timeout) {
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

String getdomain() {
    char tempBuf[40];
    sprintf(tempBuf, "AT+CIPDOMAIN=\"%s\"", DOMAIN_NAME);
    Serial1.println(tempBuf);
    unsigned long s = millis();
    
    char result[120];
    int tempIdx = 0;
    while (millis() - s < 6000) {
        if (Serial1.available() > 0) {
            char k = Serial1.read();
            Serial.print(k);
            result[tempIdx++] = k;
        }
    }

    int findIdx = 0;
    for (findIdx = 0; findIdx < tempIdx; findIdx++) {
        if (result[findIdx] == ':') {
            findIdx++;
            break;
        }
    }

    char ipInfo[30] = "";
    int copyIdx = 0;
    while(findIdx < tempIdx) {
        if(result[findIdx] == '\n' ||  result[findIdx] == '\0') {
            break;
        }
        ipInfo[copyIdx] = result[findIdx];

        findIdx++;
        copyIdx++;
    }

    ipInfo[++copyIdx] = '\0';
    if (findIdx < tempIdx) {
        return String(ipInfo);
    }
    else {
        return String("");
    }
}

int veri(const char* a, const char* b, int n) {
    int i = 0;
    for (i = 0; i < n; i++) {
        if (a[i] != '\0' && b[i] != '\0' && a[i] != b[i]) {
            Serial.println(a[i], b[i]);
        }
    }
    
    if (i == n) {
        return -1;
    }
    else return i;
}

void connect() {
    char tempBuf[80];

    delay(2000);
    lcdPrint(0, "init WIFI 1/6");
    Serial.println("init WIFI 1/6");
    cmd2esp("AT", 500); // \r\n, OK\n

    lcdPrint(0, "init WIFI 2/6");
    Serial.println("init WIFI 2/6");
    cmd2esp("AT+CWMODE=1", 500);

    lcdPrint(0, "init WIFI 3/6");
    Serial.println("init WIFI 3/6");
    sprintf(tempBuf, "AT+CWJAP=\"%s\",\"%s\"", WIFI_NAME, WIFI_PASSWORD);
    cmd2esp(tempBuf, 9000);

    lcdPrint(0, "init WIFI 4/6");
    Serial.println("init WIFI 4/6");
    String a = getdomain();
    Serial.println(a);
    int b = veri(a.c_str(), UDP_IP, strlen(a.c_str()));
    Serial.println(b);

    lcdPrint(0, "init WIFI 5/6");
    Serial.println("init WIFI 5/6");
    char what[80];
    strcpy(what, a.c_str());
    sprintf(tempBuf, "AT+CIPSTART=\"UDP\",\"%s\",%d", UDP_IP, UDP_PORT);
    // sprintf(tempBuf, "AT+CIPSTART=\"UDP\",\"%s\",%d", UDP_IP, UDP_PORT);
    cmd2esp(tempBuf, 5000);

    lcdPrint(0, "init WIFI 6/6");
    Serial.println("init WIFI 6/6");
}
