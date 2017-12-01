/*
 * Example to demonstrate thread definition, semaphores, and thread sleep.
 */
#include <FreeRTOS_ARM.h>
#include "PowerDueLED.h"
#include "Ml.h"
#include "Time.h"

void setup() {
    pd_rgb_led_init();
  pd_rgb_led(PD_OFF);
  SerialUSB.begin(9600);
  while(!SerialUSB){
  }
  SerialUSB.print("Enter Threshold CIE : ");
}
void loop() {
  float cie = 0.00005;
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
    ml.sample(100,75);
    SerialUSB.println("Begin");
    pd_rgb_led(PD_RED);
    ml.regression(cie,rate);
    pd_rgb_led(PD_OFF);
    SerialUSB.println("Done");
    //interrupts();
  }

}
