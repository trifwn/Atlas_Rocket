#ifndef ROCKET_HPP
#define ROCKET_HPP

class Rocket{
public:
	Rocket(double startHeight,double openHeightP){
		this->height = startHeight; 
		this->openHeightP = openHeightP;
	}


	void countDownBeforeLaunch();
	void startLaunch();
	void getDataFromSensors();
	void sendDataEveryToAll();
	void sendDataToGround();

	void checkState(){
		if(velocity <= 0.0)  // Considering velocity is positive going up 
			state = false;
	}

	void controlChuteLaunch(){
		// If we are falling, 
		// and parachute isn't open 
		// and our height is less than the required state
		// Then open parachute and change the flag to true
		if(height <= openHeightP && !isParOpen && state){
				openPar();
				isParOpen = true;
		}
	}
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
