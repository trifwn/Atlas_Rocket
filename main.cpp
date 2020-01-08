#include <iostream>
#include "parachutes.hpp"
#include "ignition.hpp"
#include "rocket.hpp"

int main(){
	Parachute chute = new Parachute();
	IgnitionControl ignSys = new IgnitionControl();
	Rocket rocket = new Rocket(chute,ignSys);
	while(){

	}
	return 0;
}
