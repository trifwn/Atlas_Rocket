#ifndef __ROCKET_HPP__
#define __ROCKET_HPP__

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#include "Arduino.h"

class Rocket{
public:
	Rocket();
	void initializeSensors();
	void findSensorsID();
	void checkCalibration();
	void getCalibrationResults();
	void storingCalibrationToEEPROM();
	void getNewSensorEvent();
	void takeTemperature();

	void countDownBeforeLaunch();
	void startLaunch();
	void getDataFromSensors();
	void sendDataEveryToAll();
	void sendDataToGround();
	
	void checkState();

	void controlChuteLaunch();

	/*  Displays some basic information on this sensor from 
	the unified sensor API sensor_t type  */
	void displaySensorDetails(void);

	/* Display some basic info about the sensor status */
	void displaySensorStatus(void);

	/* Display sensor calibration status  */
	void displayCalStatus(void);

	void printEventBNO(sensors_event_t* event);

	void printValuesBME();

	// Getters and Setters
	int8_t getTemperatureBNO(){
		return temperatureBNO;
	}
private:
	// Functions

	// Variables we are using 

	// Sensors 
	Adafruit_BME280 bme;
	Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

	int eeAddress = 0;
    long bnoID;
    bool foundCalib = false;

    adafruit_bno055_offsets_t calibrationData;
    adafruit_bno055_offsets_t newCalib;
	sensor_t sensor;
	sensors_event_t event;
	

	bool state; // true for falling state
	double height; // the height of the rocket
	double velocity; // velocity of the rocket every moment
	
	// BME 
	double temperatureBME;
	double pressureBME;
	double altitudeBME;
	double humidityBME; 	

	// BNO 
	double thetaBNO;
	double phiBNO;
	double altitudeBNO;
	int8_t temperatureBNO;
	
	// GPS
	double latitudeGPS;
	double longitudeGPS;

	double maxHeight;

	// Parachute
	double openHeightP;
	bool isParOpen;
	
	void openPar(); // Will deploy the small parachute of  

};
 
#endif
