#ifndef PARACHUTES_CLASS
#define PARACHUTES_CLASS

/* There will be an instance of the class in the main file. 
 * This class will have 2 functions and will only be called 
 * when needed -> downfall state + the required height 
 *
 * Obviously, we'll implement the function in another file
 * */
#include "rocket.hpp"

class Parachute: public Rocket{
public:
	Parachute(double h){ 
		this->openHeight = h;
		state = false;
	}
	friend Parachute & operator = (const Parachute &p){
		this->openHeight = p.openHeight;
		this->state = p.state; 
	}
	void controlChutesLaunch(){
		if(state){
			if(height <= openHeight){
				openSmallP();
				openMainP();
			}
		}
	}

	void checkState(){
		if(velocity <= 0)  // Considering velocity is positive going up 
			state = false;
	}
private:
	int openHeight;
	bool state;
	// Helping functions
	void openSmallP(); // Will deploy the small parachute of 
	void openMainP();
};

#endif
