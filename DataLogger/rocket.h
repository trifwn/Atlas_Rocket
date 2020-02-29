#ifndef ROCKET_HPP
#define ROCKET_HPP

#include "Arduino.h"

class Rocket{
public:
	Rocket(double startHeight,double openHeightP);
	void countDownBeforeLaunch();
	void startLaunch();
	void getDataFromSensors();
	void sendDataEveryToAll();
	void sendDataToGround();

	void checkState();

	void controlChuteLaunch();
private:
	bool state; // true for falling state
	double height; // the height of the rocket
	double velocity; // velocity of the rocket every moment
	
	// BME 
	double temperatureBME;
	double pressure;
	double altitude;
	double humidity; 

	// BNO 
	double theta;
	double phi;
	
	// GPS
	double latitude;
	double longitude;

	double maxHeight;

	// Parachute
	double openHeightP;
	bool isParOpen;
	
	void openPar(); // Will deploy the small parachute of  
};
 
#endif
