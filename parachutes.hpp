#ifndef PARACHUTES_CLASS
#define PARACHUTES_CLASS

/* There will be an instance of the class in the main file. 
 * This class will have 2 functions and will only be called 
 * when needed -> downfall state + the required height 
 *
 * Obviously, we'll implement the function in another file
 * */
#include "rocket.hpp"

class Parachutes: public Rocket{
public:
	Parachutes(double initial_height){
		this->height = initial_height;
		state = false;
	}
	// Some getters and setters
	// These are for safety, to be able to control from GROUND STATION (probably)
	bool getState(){
		return state;
	}
	bool setState(bool s){  // In case the sensors fail
		this->state = s;
	}
	double getHeight(){
		return height;
	}
	double setHeight(double h){ // Maybe have velocity here instead, we'll see
		this->height = h;
	}

	void controlChutesLaunch(double h,double v/*, ... ,*/){
		// Gets live feed from sensors
		// if velocity is zero , set state to true
		if(state){ // Since we will run everything once we don't need a while here
			// need data ... 
			// if condition 1
		}
	}
private:
	bool state; // true for falling state
	double height; // the height of the rocket
	double velocity; // velocity of the rocket every moment

	// Helping functions
	void openSmallP(); // Will deploy the small parachute of 
	void openMainP();
};

#endif
