#include <Arduino.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 64 // OLED display height, in pixels

#define OLED_RESET     -1 //reset pin
#define SCREEN_ADDRESS 0x3C ///Sometimes 0x3D ou 0x3F

#include <Wire.h>

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void scan()
{
  byte error, address;
  int nDevices;
     
  Serial.println("Scanning...");
     
  nDevices = 0;
  for(address = 1; address < 127; address++ )
  {
    Wire.beginTransmission(address);
    error = Wire.endTransmission();
     
    if (error == 0)
    {
      Serial.print("I2C device found at address 0x");
      if (address<16) {
        Serial.print("0");
      }
      Serial.print(address,HEX);
      Serial.println("  !");
      nDevices++;
    }
    else if (error==4)
    {
      Serial.print("Unknow error at address 0x");
      if (address<16) {
        Serial.print("0");
      } 
      Serial.println(address,HEX);
    }    
  }
  if (nDevices == 0) {
    Serial.println("No I2C devices found\n");
  }
  else {
    Serial.println("done\n");
  }
  delay(5000);
}

void setup() {
  
  Serial.begin(9600);
  Wire.begin();
  delay(100);
  Serial.println("Scanning...");
  scan(); //Check if any I2C device is connected
  
  display.begin();
  display.display(); //Display Adafruit symbol
  delay(500); 
  display.clearDisplay(); //Clear screen

  display.setTextSize(1);               //Size factor
  display.setTextColor(SSD1306_WHITE);  //White text
  display.setCursor(0, 0);              //Set cursor to (0,0)
  
  display.println("CREPP.io OLED");
  display.display();
  Serial.println("END");
}

void loop() 
{
  
}
