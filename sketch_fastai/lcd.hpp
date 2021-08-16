#pragma once
#include <Arduino.h>
#include <LiquidCrystal_I2C.h>
#include <Wire.h>

LiquidCrystal_I2C lcd(0x27, 20, 2);

void lcdInit() {
    lcd.init();
    lcd.backlight();
}

void lcdPrint(int line, const char* str) {
    lcd.setCursor(0, line);
    lcd.print(str);
}

