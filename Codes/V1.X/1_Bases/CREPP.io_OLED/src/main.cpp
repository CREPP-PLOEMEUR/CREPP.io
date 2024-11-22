/*
 * This program is free software; you can redistribute it and/or
 * modify without any restriction
 * 
 * This file write text on OLED screen
 */

/*
 *   Libraries
 */
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
/*
 *   Macros
 */
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

#define OLED_RESET     -1 //reset pin
#define SCREEN_ADDRESS 0x3C ///Sometimes 0x3D ou 0x3F


Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void setup() 
{
  
  Serial.begin(MONITOR_SPEED);      

  bool status_OLED = display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS);
   if (!status_OLED) 
  {
    Serial.println("Could not find a valid OLED sensor, check wiring!");
  }
  else
  {
    Serial.println("Found a valid OLED sensor");
  }
  delay(100);
  display.clearDisplay();
  display.setRotation(2);
  display.setTextSize(1);               //Size factor
  display.setCursor(0, 0);              //Set cursor to (0,0)
  display.setTextColor(SSD1306_WHITE);  //White text
  display.println("OLED : OK");
  display.display();
}

void loop() 
{
  
}
