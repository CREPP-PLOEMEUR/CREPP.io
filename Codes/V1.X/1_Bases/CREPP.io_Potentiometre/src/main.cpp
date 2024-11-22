/*!
CREPP.io code
Ce code permet de tester le bon fonctionnement du potentiomètre
Ne pas oublier de mettre le jumper associé (ADC0)
*/
#include <Arduino.h> 

#define POT A0
#define ADC_RESOLUTION 10 //10Bits de résolution => 1024 valeurs possibles
/*
Résolution de l'ADC (Analog to Digital Converter) : 
r = VCC / ( (2^ADC_RESOLUTION) - 1) = 3.3 / ( (2^10) - 1) = 3.3 / 1023 = 0,00322580645161 V
*/
#define ADC_MIN_VALUE 0.00322580645161


void setup() 
{
    Serial.begin(MONITOR_SPEED);         //Initialise la communication série
    pinMode(D4, OUTPUT); //Configure la broche D4 en sortie
    pinMode(POT, INPUT); //Broche en entrée

}

void loop() 
{ 
  
  uint16_t rawValue = analogRead(POT);            //Lecture de la valeur
  float voltage = rawValue * ADC_MIN_VALUE;
  Serial.println(" - Tension : "+String(voltage)+" V"); //Affichage de la valeur sur le port série

  delay(100); //Rafraîchissement de la valeur toutes les 100 ms
  Serial.print("Valeur analogique : ");
  Serial.println(rawValue); // Affiche la valeur lue
          
  if(rawValue >= 700)
  {
    digitalWrite(D4, LOW);
  }
  else {
    digitalWrite(D4, HIGH); 
  }
}
