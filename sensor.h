#include <stdlib.h>
#include <Arduino.h>
#include <DHT.h>

#define DATA_PIN 8
#define DHT_TYPE 22

void sensorInit();
void sensorRead();

struct sensorData {
    float temperature;
    float humidity;

    sensorData(float t, float h): temperature(t), humidity(h) {};
};
