// Arduino Headers 
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#include <rocket.h>
#include <defaults.h>

Rocket *rocket;

void setup(){
    Wire.begin(); // Init I2C bus
    Serial.begin(115200); // Init serial bus
    
    rocket = new Rocket(); 
    rocket->initializeSensors();
    EEPROM.get(rocket->eeAddress, rocket->bnoID);
    
    rocket->findSensorsID();
    delay(1000);

    /* Display some basic information on this sensor */
    rocket->displaySensorDetails();

    /* Optional: Display current status */
    rocket->displaySensorStatus();

    rocket->checkCalibration();
    rocket->getCalibrationResults();
    delay(500);
}

void loop(){
    rocket->getNewSensorEvent();
    
    rocket->takeTemperature();

    Serial.print(F("temperature: "));
    Serial.println(rocket->getTemperatureBNO());

    /* Optional: Display calibration status */
    rocket->displayCalStatus();

    /* Optional: Display sensor status (debug only) */
    //displaySensorStatus();

    /* New line for the next sample */
    Serial.println("");

    /* Wait the specified delay before requesting new data */
    delay(BNO055_SAMPLERATE_DELAY_MS);

    rocket->printValuesBME();
}