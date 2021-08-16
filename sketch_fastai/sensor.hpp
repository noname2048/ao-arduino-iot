#pragma once
#include <stdlib.h>
#include <Arduino.h>
#include <DHT.h>

#define DATA_PIN 8
#define DHT_TYPE 22

float temperature = 1000.0f;
float humidity = 1000.0f;
char buf[30];

DHT dhtSensor(DATA_PIN, DHT_TYPE);

void sensorInit() {
    dhtSensor.begin();
}

void sensorRead() {
    temperature = dhtSensor.readTemperature();
    humidity = dhtSensor.readHumidity();

    int t1 = temperature;
    int t2 = (int)(temperature * 100) % 100;
    int h1 = humidity;
    int h2 = (int)(humidity * 100) % 100;

    memset(buf, 0, sizeof(buf));
    sprintf(buf, "T%02d.%02d,H%02d.%02d", t1, t2, h1, h2);
    Serial.println(buf);
}

char* getSensorDataStr() {
    return buf;
}
