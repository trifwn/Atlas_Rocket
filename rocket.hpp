#ifndef ROCKET_HPP
#define ROCKET_HPP

#include "parachutes.hpp"
#include "ignition.hpp"

class Rocket{
public:
	Rocket(IgnitionControl ig, Parachutes p);
	void countDownBeforeLaunch();
	void startLaunch();
	void getDataFromSensors();
	void sendDataEveryToAll();
	void sendDataToGround();

private:
protected:
};


#endif
