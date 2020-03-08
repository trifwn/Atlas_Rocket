// Arduino Headers 
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <TinyGPS.h>
#include <SoftwareSerial.h>

#include <rocket.h>
#include <defaults.h>

Rocket *rocket;
// The serial connection to the GPS module
SoftwareSerial ss(4, 3);

void setup(){
    Wire.begin(); // Init I2C bus
    Serial.begin(115200); // Init serial bus
    ss.begin(GPSBaud);
    
    rocket = new Rocket(); 
    rocket->initializeSensors();
    EEPROM.get(rocket->eeAddress, rocket->bnoID);
    
    rocket->findSensorsID();
    delay(1000);

    /* Display some basic information on this sensor */
    rocket->displayDetailsBNO();

    /* Optional: Display current status */
    rocket->displayStatusBNO();

    rocket->checkCalibration();
    rocket->getCalibrationResults();
    delay(500);
}

void loop(){
    rocket->getNewSensorEvent();
    
    rocket->takeTemperatureBNO();

    Serial.print(F("Board temperature: "));
    Serial.println(rocket->getBoardTemperature());

    /* Optional: Display calibration status */
    rocket->displayCalStatus();

    /* Optional: Display sensor status (debug only) */
    //rocket->displayStatusBNO();

    /* New line for the next sample */
    Serial.println("");

    /* Wait the specified delay before requesting new data */
    delay(BNO055_SAMPLERATE_DELAY_MS);

    rocket->printValuesBME();

    rocket->printValuesGPS();
    
    smartdelay(GPS_SAMPLERATE_DELAY_MS);
}