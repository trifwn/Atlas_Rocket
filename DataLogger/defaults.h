#ifndef	DEFAULTS_H
#define	DEFAULTS_H

// Pin mappings on Arduino Micro
#define ARD_PIN_0   0 
#define ARD_PIN_TX ARD_PIN_0
#define ARD_PIN_1   1 
#define ARD_PIN_RX ARD_PIN_1
#define ARD_PIN_2   2 
#define ARD_SDA  ARD_PIN_2
#define ARD_PIN_3   3 
#define ARD_SCL  ARD_PIN_3 
#define ARD_PIN_4   4
#define ARD_PIN_5   5
#define ARD_PIN_6   6
#define ARD_PIN_7   7
#define ARD_PIN_8   8
#define ARD_PIN_9   9
#define ARD_PIN_10  10
#define ARD_PIN_11  11
#define ARD_PIN_12  12
#define ARD_PIN_13  13
#define ARD_PIN_14  14
#define ARD_PIN_15  15
#define ARD_PIN_16  16
#define ARD_PIN_17  17
#define ARD_PIN_A0  A0
#define ARD_PIN_A1  A1
#define ARD_PIN_A2  A2 
#define ARD_PIN_A3  A3
#define ARD_PIN_A4  A4
#define ARD_PIN_A5  A5

#define	ARD_MISO  ARD_PIN_14
#define	ARD_SCK	  ARD_PIN_15
#define	ARD_MOSI  ARD_PIN_16
#define	ARD_SS  ARD_PIN_17

// Adafruit BME280
#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_SDI BME_MOSI
#define BME_CS 10

// Adafruit Ultimate GPS


// Adafruit BNO055


/* Set the delay between fresh samples */
#define BNO055_SAMPLERATE_DELAY_MS (100)

#endif // DEFAULTS_H