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
	int8_t getTemperature(){
		return temperature;
	}
private:
	bool state; // true for falling state
	double height; // the height of the rocket
	double velocity; // velocity of the rocket every moment
	
	/* BME */
	Adafruit_BME280 bme;
	double temperature;
	double pressure;
	double altitude;
	double humidity; 	

	/* BNO  */
	Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);
	adafruit_bno055_offsets_t calibrationData;
    adafruit_bno055_offsets_t newCalib;
	sensor_t sensor;
	sensors_event_t event;
	int eeAddress = 0;
    long bnoID;
    bool foundCalib = false;
	uint8_t system;
	uint8_t gyroscope;
	uint8_t acceleration;
	uint8_t magnetometer;
	double orientation_x,orientation_y,orientation_z;
	double acceleration_x,acceleration_y,acceleration_z;
	double magnetic_x,magnetic_y,magnetic_z;
	double gyro_x,gyro_y,gyro_z;
	
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
