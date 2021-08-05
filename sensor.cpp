#include "sensor.h"

DHT dhtSensor(DATA_PIN, DHT_TYPE);

float temperature = 1000.0f;
float humidity = 1000.0f;
char buf[30];

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
