/*
 * Example to demonstrate thread definition, semaphores, and thread sleep.
 */
#include <LoRa.h>
#include "PowerDueLED.h"
#include "Ml.h"
#include "Time.h"


// fixed parameters
#define FREQUENCY         915E6   // 915MHz
#define BANDWIDTH         125000  // 125kHz bandwidth
#define SLEEPTIME         4000    // 4 seconds

// vary these parameters
#define TX_POWER          6   // valid values are from 6 to 20
#define SPREADING_FACTOR  10    // valid values are 7, 8, 9 or 10
#define PASSWORD          "-3,0,-2,7,4,0,12,13,9,9,4,14,10,10,16,12,24,24,9,13,12,27,27,30,30,29,20,34,18,22,37,33,40,42,24,34,45,40,29,40,36,48,46,35,53,51,40,44,41,43,56,61,52,51,57,62,56,59,54,59,57,64,64,70,58,69,67,73,67,61,78,79,82,69,78,72,76,86,86,87,71,79,86,73,79,82,87,91,85,99,94,98,85,92,99,104,106,92,106,98"

int analog_read_value;

void setup() {
  
  pd_rgb_led_init();
  pd_rgb_led(PD_OFF);

  LoRa.setPins(58, 59, 51);
  LoRa.begin(FREQUENCY);
  
  LoRa.setTxPower(TX_POWER);
  LoRa.setSpreadingFactor(SPREADING_FACTOR);
  LoRa.setSignalBandwidth(BANDWIDTH);
  
  SerialUSB.begin(9600);
  while(!SerialUSB){
  }
  SerialUSB.print("Enter Threshold CIE : ");
   
}
void loop() {
  float cie = 0.5;
  float inpu;
  float rate;
  byte incomingByte = 0;
  int flg = 0;
  
  if(SerialUSB.available() > 0) {
    incomingByte = SerialUSB.read();
    inpu = (int)incomingByte-48;
    rate = inpu/10;
    SerialUSB.print("Rate set to : ");
    SerialUSB.println(rate);
    flg = 1;
  }

  if(flg==1){
    //noInterrupts();
    //delay(1000);
    Ml ml;
    ml.clear_all();
    //ml.append(200);
    //ml.append(100);
    //ml.append(300);
    //ml.sample(100,75);
    ml.sample_sensor(100,75);
    SerialUSB.println("Begin");
    pd_rgb_led(PD_RED);
    
    ml.regression(cie,rate);
    //LoRa.beginPacket();
    //LoRa.print(PASSWORD);
    //LoRa.endPacket();
    
    pd_rgb_led(PD_OFF);
    SerialUSB.println("Done");
    
    //interrupts();
  }

}
