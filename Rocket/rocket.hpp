#ifndef ROCKET_HPP
#define ROCKET_HPP

#include "parachutes.hpp" 

class Rocket{
public:
	Rocket(double start_height, Parachute *p);

	void countDownBeforeLaunch();
	void startLaunch();
	void getDataFromSensors();
	void sendDataEveryToAll();
	void sendDataToGround();

protected:
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
};
 
#endif
