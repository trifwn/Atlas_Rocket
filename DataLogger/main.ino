/*

Here goes the arduino code

*/ 

// #include <iostream>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#include <rocket.h>
#include <defaults.h>

Adafruit_BME280 bme;
Adafruit_BNO055 bno = Adafruit_BNO055(55, 0x28);

void setup(){
	Wire.begin(); // Init I2C bus
	Serial.begin(115200); // Init serial bus
	
	// Initialize the sensors
    if (! bme.begin(0x77, &Wire)) {
        Serial.println("Could not find a valid BME280 sensor, check wiring!");
        while (1) delay(10);
    }

    if(!bno.begin()){
		/* There was a problem detecting the BNO055 ... check your connections */
		Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
		while(1);
	}
	
	delay(1000);

	bno.setExtCrystalUse(true);
}
void loop(){

}
// int main(){ 
// 	Rocket *rocket;
// 	rocket = new Rocket(0.0,100.0);
// 	while(true){
		
// 	}
// 	return 0;
// }