#include "Arduino.h"
#include "rocket.h"

Rocket::Rocket(double startHeight,double openHeightP){
    this->height = startHeight; 
	this->openHeightP = openHeightP;
}
void Rocket::checkState(){
	if(velocity <= 0.0)  // Considering velocity is positive going up 
		state = false;
}

void Rocket::controlChuteLaunch(){
    // If we are falling, 
    // and parachute isn't open 
    // and our height is less than the required state
    // Then open parachute and change the flag to true
    if(height <= openHeightP && !isParOpen && state){
            openPar();
            isParOpen = true;
    }
}