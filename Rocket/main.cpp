/*

Here goes the arduino code

*/ 


#include "parachutes.hpp" 
#include "rocket.hpp"

int main(){
	Parachute *chute = new Parachute(1050.2); 
	Rocket *rocket = new Rocket(0.0,chute);
	while(true){
		
	}
	return 0;
}
